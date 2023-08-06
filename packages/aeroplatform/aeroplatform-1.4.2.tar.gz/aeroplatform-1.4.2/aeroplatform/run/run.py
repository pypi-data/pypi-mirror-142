import os
import logging
from enum import Enum, unique
import subprocess
import re
import os.path
import psutil
import re
from ..utils import AeroProcessRunner, FileNotSupported, \
    Executable, DecoratorFormatter, CondaDecoratorFormat

logger = logging.getLogger(__name__)


class ParameterFormat(DecoratorFormatter):

    format = {
        Executable.PYTHON: "Parameter",
        Executable.R: "Parameter"
    }
    parameter_format = {
        Executable.PYTHON: "Parameter\('([\w]*)'",
        Executable.R: "Parameter\('([\w]*)'"
    }
    decorator = "Resources"

    def parse_parameter(self, line) -> str:
        match = re.search(self.parameter_format[self._executable], line)
        if match is not None:
            return match.group(1)
        else:
            return ""


class ResourceDecoratorFormat(DecoratorFormatter):

    format = {
        Executable.PYTHON: "@resources",
        Executable.R: "decorator.*resources"
    }
    resource_format = {
        Executable.PYTHON: f"@resources\(([^)]+)\)",
        Executable.R: "decorator\([^=]*,([^)]+)\)"
    }
    decorator = "Resources"

    def parse_resources(self, line):
        return re.search(self.resource_format[self._executable], line)


class BatchDecoratorForamt(DecoratorFormatter):

    format = {
        Executable.PYTHON: "@batch",
        Executable.R: "decorator.*batch"
    }
    decorator = "Batch"


BATCH_DEC = '@batch'
RESOURCE_DEC = '@resources'
CONDA_ENV = '--environment=conda'
MF_RUN = 'run'
MF_RESUME = 'resume'
BATCH_CMD = '--with batch'
RUN_ID_OPTION = "--origin-run-id"


@unique
class RunState(Enum):
    LOCAL = 0
    CLOUD = 1


class AeroRun(AeroProcessRunner):

    def __init__(self, filename: str, args: str, run_state: RunState, cpu: int = None, mem: int = None,
                 resume: bool = False, step: str = None, from_run_id: str = None):
        super().__init__()
        self._filename = filename
        self._args = args
        self._run_state = run_state
        self._cpu = cpu
        self._mem = mem
        self._resume = resume
        self._step = step
        self._from_run_id = from_run_id
        self._executable = self.get_executable(self._filename)

    def check_if_local_and_has_batch_decorator(self):
        batch_decorator = BatchDecoratorForamt(self._executable)
        return self._run_state == RunState.LOCAL and \
            AeroRun.check_for_decorator(self._filename, batch_decorator)

    def check_if_local_and_has_resources_decorator(self):
        return self._run_state == RunState.LOCAL and \
            not self.check_resources()

    def run(self):
        # Build command
        aero_cmd = [self._executable.value, self._filename]

        # Check if conda decorator was found, if so, add env
        if self.check_for_decorator(self._filename, CondaDecoratorFormat(self._executable)):
            aero_cmd.append(CONDA_ENV)

        if not self._resume:
            # Add metaflow run command
            aero_cmd.append(MF_RUN)
        else:
            # Add metaflow resume command
            aero_cmd.append(MF_RESUME)

            if self._step:
                aero_cmd.append(self._step)

            if self._from_run_id:
                aero_cmd.append(RUN_ID_OPTION)
                aero_cmd.append(self._from_run_id)

        # Add any user args
        if self._args:
            aero_cmd.extend(self._args.split(" "))

        # Check if run is cloud, if so check resources
        if self._run_state == RunState.CLOUD:
            cloud_cmd = BATCH_CMD
            if self._cpu or self._mem:
                cloud_cmd += ':'
                if self._cpu:
                    cloud_cmd += f'cpu={self._cpu},' if self._mem else f'cpu={self._cpu}'
                if self._mem:
                    cloud_cmd += f'memory={self._mem}'

            aero_cmd.extend(cloud_cmd.split(" "))

        return self._run_blocking_process(aero_cmd)

    def check_parameters(self) -> bool:
        param_list = []
        param_format = ParameterFormat(self._executable)

        with open(self._filename) as f:
            for line in f:
                if param_format.in_line(line):
                    li = line.strip()
                    if not li.startswith('#') and 'import' not in line:
                        # We have a Parameter in code, abort if args is None
                        if not self._args:
                            return False
                        param = param_format.parse_parameter(line)
                        if len(param) > 0:
                            param_list.append(param)

        arg_list = []

        args_split = self._args.split("--")
        for arg in args_split:
            if len(arg) > 0:
                split_split = arg.split(" ")
                arg_list.append(split_split[0])

        param_list.sort()
        arg_list.sort()

        logger.debug(f"Params: {param_list}")
        logger.debug(f"Args: {arg_list}")

        if arg_list == param_list:
            return True
        else:
            return False

    def check_resources(self) -> bool:
        memory = 0
        cpu = 0
        check_resources = False
        resource_decorator = ResourceDecoratorFormat(self._executable)

        with open(self._filename) as f:
            for line in f:
                if resource_decorator.in_line(line):
                    li = line.strip()
                    if not li.startswith('#'):
                        match = resource_decorator.parse_resources(line)

                        if match is not None:
                            req_res_str = match.group(1)
                            if req_res_str is not None:
                                req_res = [y.strip() for y in req_res_str.split(',')]

                                for res_str in req_res:
                                    try:
                                        res = res_str.split("=")

                                        if res[0] == 'memory':
                                            memory = max(int(res[1]), memory) # Can be multiple decorators per flow
                                            logger.debug(f"Detected resource request for memory: {memory}")
                                            check_resources = True
                                        elif res[0] == 'cpu':
                                            cpu = max(int(res[1]), cpu) # Can be multiple decorators per flow
                                            logger.debug(f"Detected resource request for cpu: {cpu}")
                                            check_resources = True
                                        else:
                                            logger.debug(f"Detected request for unknown resource")
                                            return True
                                    except Exception as e:
                                        logger.debug(f"Error parsing resources")
                                        return True

        if check_resources:
            num_cpu = psutil.cpu_count()
            free_mem = psutil.virtual_memory().free >> 20 # shift to MBs, think this is correct?

            if cpu != 0:
                logger.debug(f"Requested {cpu} cpus, system has {num_cpu}")

            if memory != 0:
                logger.debug(f"Requested memory is {memory}, system has {free_mem} free")

            if cpu != 0 and num_cpu < int(cpu):
                return False

            if memory != 0 and free_mem < int(memory):
                return False

        return True
