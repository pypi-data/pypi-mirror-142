import click
import logging
from .configure import CondaInstaller, CONDA, SystemNotReady, SystemNotSupported, InstallFailed, ShellNotSupported
from ..utils import RunError


logger = logging.getLogger(__name__)


def cleanup_install():
    CondaInstaller.kill()


@click.command(help="Configure system to run Aero")
def configure():
    click.echo('Checking system for conda...')
    if CondaInstaller.check_installed(CONDA):
        click.echo('conda installed, system configured')
        return
    else:
        click.echo('conda not installed, attempting conda install')
        inst = CondaInstaller()

        try:
            ret = inst.install_conda()
            if ret != 0:
                click.echo(f'Sorry, there was an error')
            else:
                click.echo(f'Configuration complete, please close shell and reopen')

        except SystemNotSupported as e:
            click.echo(f'Configure command does not support {e.system} {e.machine}')
            click.echo(f'Please install conda manually.')

        except SystemNotReady as e:
            click.echo(f'System does not have {e.missing}, please install this for configure to work')

        except InstallFailed as e:
            click.echo(f'Install failed: {e.cmd} returned with error {e.ret}')

        except ShellNotSupported as e:
            click.echo(f'Configure command does not support shell: {e.shell}')
            click.echo(f'Please install conda manually.')
