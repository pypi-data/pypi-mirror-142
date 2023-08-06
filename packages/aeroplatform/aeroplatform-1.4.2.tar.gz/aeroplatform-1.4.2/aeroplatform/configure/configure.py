import platform
import logging
from ..utils import AeroProcessRunner, get_shell, get_supported_shells
from shutil import which
from typing import List
import os
from enum import Enum, unique

logger = logging.getLogger(__name__)

CONDA = 'conda'
CURL = 'curl'
WGET = 'wget'
DARWIN = 'Darwin'
MACOSX = 'MacOSX'
LINUX = 'Linux'
SYSTEMS = [DARWIN, LINUX]
MACHINES = ['x86', 'x86_64', 'armv7l', 'aarch64']
MINICONDA_SCRIPT_PREFACE = 'Miniconda3-latest'
MINICONDA_SCRIPT_LOCALE = f"{os.environ['HOME']}/tmp_aero/"
MINICONDA_INSTALL_LOCALE = f"{os.environ['HOME']}/miniconda"
MINICONDA_SCRIPT_NAME = 'miniconda.sh'
CONDA_URL_BASE = 'https://repo.anaconda.com/miniconda/'


class SystemNotSupported(Exception):

    def __init__(self, machine: str, system: str):
        super().__init__()
        self.machine = machine
        self.system = system


class SystemNotReady(Exception):

    def __init__(self, cmd: str):
        super().__init__()
        self.missing = cmd


class ShellNotSupported(Exception):

    def __init__(self, shell: str):
        super().__init__()
        self.shell = shell


class InstallFailed(Exception):

    def __init__(self, cmd: str, ret: int):
        super().__init__()
        self.cmd = cmd
        self.ret = ret


@unique
class InstallOrder(Enum):
    __order__ = 'PRE_INSTALL DOWNLOAD INSTALL CLEAN CONFIG INIT'
    PRE_INSTALL = 0
    DOWNLOAD = 1
    INSTALL = 2
    CLEAN = 3
    CONFIG = 4
    INIT = 5


class CondaInstaller(AeroProcessRunner):

    def __init__(self):
        super().__init__()
        self.system = None
        self.machine = None
        self.conda_script_name = None
        self._commands = [str() for s in InstallOrder]

    def install_conda(self):
        self.system = platform.system()
        self.machine = platform.machine()

        if self.system not in SYSTEMS or \
           self.machine not in MACHINES:
            raise SystemNotSupported(machine=self.machine, system=self.system)

        if self.system == DARWIN:
            self.system = MACOSX

        self.conda_script_name = f'{MINICONDA_SCRIPT_PREFACE}-{self.system}-{self.machine}.sh'
        logger.debug(f'Conda Target Script: {self.conda_script_name}')

        self._commands[InstallOrder.PRE_INSTALL.value] = ['mkdir', MINICONDA_SCRIPT_LOCALE]

        if self.system == MACOSX:
            self._commands[InstallOrder.DOWNLOAD.value] = self._get_install_conda_cmd_darwin(self.conda_script_name)
        elif self.system == LINUX:
            self._commands[InstallOrder.DOWNLOAD.value] = self._get_install_conda_cmd_linux(self.conda_script_name)

        self._commands[InstallOrder.INSTALL.value] = ['bash',
                                                      f'{MINICONDA_SCRIPT_LOCALE}{MINICONDA_SCRIPT_NAME}',
                                                      '-b', '-p', MINICONDA_INSTALL_LOCALE]

        self._commands[InstallOrder.CLEAN.value] = ['rm', '-rf', MINICONDA_SCRIPT_LOCALE]

        self._commands[InstallOrder.CONFIG.value] = [f'{MINICONDA_INSTALL_LOCALE}/bin/conda', 'config', '--set',
                                                     'auto_activate_base', 'false']
        shell = get_shell()
        if shell in get_supported_shells():
            self._commands[InstallOrder.INIT.value] = [f'{MINICONDA_INSTALL_LOCALE}/bin/conda', 'init', shell]
            return self._install_conda()
        else:
            raise ShellNotSupported(shell)

    def _install_conda(self):
        ret = 0
        for command_idx in InstallOrder:
            ret = self._run_blocking_process(cmd=self._commands[command_idx.value])
            if ret != 0:
                raise InstallFailed(cmd=self._commands[command_idx.value], ret=ret)

        return ret

    @classmethod
    def check_installed(cls, cmd: str) -> bool:
        return which(cmd) is not None

    @staticmethod
    def _get_install_conda_cmd_darwin(script_name: str) -> List:
        if CondaInstaller.check_installed(CURL):
            return [CURL, f'{CONDA_URL_BASE}{script_name}', '-o', f'{MINICONDA_SCRIPT_LOCALE}{MINICONDA_SCRIPT_NAME}']
        else:
            raise SystemNotReady(cmd=CURL)

    @staticmethod
    def _get_install_conda_cmd_linux(script_name: str) -> List:
        if CondaInstaller.check_installed(WGET):
            return [WGET, f'{CONDA_URL_BASE}{script_name}', '-O', f'{MINICONDA_SCRIPT_LOCALE}{MINICONDA_SCRIPT_NAME}']
        else:
            raise SystemNotReady(cmd=WGET)
