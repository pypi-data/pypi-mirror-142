from enum import Enum
import click
import os
import re
import subprocess
import logging
from typing import List

logger = logging.getLogger(__name__)

def cyan(string: str):
    return click.style(string, fg='cyan')


def magenta(string: str):
    return click.style(string, fg='magenta')


def red(string: str):
    return click.style(string, fg='red')


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_BASE = "https://site.aeroplatform.co.uk"
TUTORIAL_PATH = "/commands"
NAME_LOWER = "aero"
NAME_UPPER = "Aero"
NAME_ASCII = cyan('\n'
                  ',adPPYYba,   ,adPPYba,  8b,dPPYba,   ,adPPYba, \n'  
                  '""     `Y8  a8P_____88  88P    "Y8  a8"     "8a\n'  
                  ',adPPPPP88  8PP"""""""  88          8b       d8\n'  
                  '88,    ,88  "8b,   ,aa  88          "8a,   ,a8"\n'  
                  '`"8bbdP"Y8   `"Ybbd8"   88           `"YbbdP"  \n')


def print_welcome():
    click.echo(NAME_ASCII)
    click.echo(f'Welcome to {magenta(NAME_UPPER)}!')
    click.echo("A Data Platform designed to put developers first.")
    click.echo(f"For more information, visit {cyan(SITE_BASE)}")


def check_file_exists(filename: str) -> bool:
    return os.path.isfile(filename)

class Executable(Enum):
    PYTHON = "python3"
    R = "Rscript"

class DecoratorNotFoundException(Exception):

    def __init__(self, message: str, decorator: str):
        super().__init__(message)
        self.message = message
        self.decorator = decorator

class DecoratorFormatter():

    format = {}
    decorator = "base"

    def __init__(self, executable: Executable):
        self._executable = executable

    def in_line(self, line: str):
        
        # If None, decorator not in line
        return re.search(self.format[self._executable], line) != None

    def raise_not_found(self):
        raise DecoratorNotFoundException(
            f"Decorator not found, please check documentation at {SITE_BASE}{TUTORIAL_PATH}", 
            self.decorator
        )

class CondaDecoratorFormat(DecoratorFormatter):

    format = {
        Executable.PYTHON: "@conda",
        Executable.R: r"\A(?!x)x" # a regex which can never match, R doesn't need --env=conda
    }
    decorator = "Conda"

def get_shell() -> str:
    try:
        return os.path.basename(os.environ['SHELL'])
    except KeyError:
        return ''


def get_supported_shells() -> List:
    return ['bash', 'fish', 'zsh', 'tcsh']


class FileNotSupported(Exception):

    def __init__(self, message: str, filename: str):
        super().__init__(message)
        self.message = message
        self.filename = filename


class RunError(Exception):
    ...


class AeroProcessRunner:

    ACTIVE_RUNS = []

    def __init__(self):
        self._sp = None

    def _run_blocking_process(self, cmd: List) -> int:
        logger.debug(f'Running blocking command: {cmd}')

        try:
            self._sp = subprocess.Popen(cmd)
        except Exception as e:
            logger.debug(f'Exception from Popen: {e}')
            raise RunError

        self._add_active_proc(self._sp)
        self._sp.wait()
        self._rem_active_proc(self._sp)

        return self._sp.returncode

    @classmethod
    def _add_active_proc(cls, proc: subprocess.Popen):
        cls.ACTIVE_RUNS.append(proc)

    @classmethod
    def _rem_active_proc(cls, proc: subprocess.Popen):
        try:
            cls.ACTIVE_RUNS.remove(proc)
        except ValueError:
            logger.debug("Tried to remove a proc that was not added")

    @classmethod
    def kill(cls):
        for proc in cls.ACTIVE_RUNS:
            logger.debug(f'Killing active process {proc}')
            proc.kill()

    @classmethod
    def get_executable(cls, filename: str) -> Executable:

        # Catching error like this allows us to not have a NOT_SUPPORTED executable type,
        # Else for the function to return an executable, we'd have to have a "None" enum
        try:
            _, file_extension = os.path.splitext(filename.lower())
            extensions = {
                ".py": Executable.PYTHON,
                ".r": Executable.R
            }

            return extensions[file_extension]
        except:
            raise FileNotSupported('Currently, only Python and R files are supported', filename)

    @classmethod
    def check_for_decorator(cls, filename: str, dec: DecoratorFormatter) -> bool:
        with open(filename) as f:
            for line in f:
                if dec.in_line(line):
                    li = line.strip()
                    if not li.startswith('#'):
                        logger.debug(f'{dec} is set')
                        return True
        return False
