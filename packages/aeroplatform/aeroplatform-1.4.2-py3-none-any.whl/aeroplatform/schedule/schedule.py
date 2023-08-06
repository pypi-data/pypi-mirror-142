from ..utils import AeroProcessRunner, DecoratorFormatter, Executable, CondaDecoratorFormat
from ..run.run import CONDA_ENV
import subprocess
import logging

logger = logging.getLogger(__name__)

class ScheduleDecoratorFormat(DecoratorFormatter):

    format = {
        Executable.PYTHON: "@schedule",
        Executable.R: "decorator.*schedule"
    }
    decorator = "Schedule"

SCHEDULE_CMD = 'schedule'
SCHEDULE_CMD_CREATE = 'create'
SCHEDULE_CMD_LOGS = 'get-logs'
SCHEDULE_CMD_INSPECT = 'list-runs'
SCHEDULE_CMD_TRIGGER = 'trigger'
SCHEDULE_REMOVE_FLOW = "remove"


class AeroScheduler(AeroProcessRunner):

    def __init__(self, filename: str):
        super().__init__()
        self._filename = filename
        
        # Moved decorator check in ProcessRunner so we can 
        # base decorator checks based on executable
        decorator = ScheduleDecoratorFormat(self.get_executable(filename))

        if not self.check_for_decorator(
            filename, 
            decorator
        ):  
            # raises an exception
            decorator.raise_not_found()

    def create(self):
        return self._scheduler_run(SCHEDULE_CMD_CREATE)

    def trigger(self):
        return self._scheduler_run(SCHEDULE_CMD_TRIGGER)

    def inspect(self):
        return self._scheduler_run(SCHEDULE_CMD_INSPECT)

    def logs(self):
        return self._scheduler_run(SCHEDULE_CMD_LOGS)

    def remove(self):
        return self._scheduler_run(SCHEDULE_REMOVE_FLOW)

    def _scheduler_run(self, command: str):
        # Build command
        executable = self.get_executable(self._filename)
        aero_cmd = [executable.value, self._filename]

        if self.check_for_decorator(self._filename, CondaDecoratorFormat(executable)):
            aero_cmd.append(CONDA_ENV)

        aero_cmd.extend([SCHEDULE_CMD, command])

        return self._run_blocking_process(aero_cmd)
