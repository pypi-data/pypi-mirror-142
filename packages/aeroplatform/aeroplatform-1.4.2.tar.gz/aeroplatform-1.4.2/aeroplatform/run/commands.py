import click
from ..utils import red, check_file_exists, RunError
import logging
import os
from .run import AeroRun, RunState, FileNotSupported, BATCH_DEC, RESOURCE_DEC

logger = logging.getLogger(__name__)


def cleanup_run():
    AeroRun.kill()


@click.group(help="Run flows")
def run():
    pass


@run.command(help="Run a flow locally")
@click.argument('filename')
@click.option("--args", default=None,
              help="Flow arguments, must be presented as a quoted string, eg "
                   "'--arg1 arg1 --arg2 arg2'")
def local(filename, args):
    cmd_run(filename, args, RunState.LOCAL)


@run.command(help="Run a flow in the cloud")
@click.argument('filename')
@click.option("--cpu", type=int, default=None)
@click.option("--memory", type=int, default=None)
@click.option("--args", default=None,
              help="Flow arguments, must be presented as a quoted string, eg "
                   "'--arg1 arg1 --arg2 arg2'")
def cloud(filename, cpu, memory, args):
    cmd_run(filename, args, RunState.CLOUD, cpu, memory)


def cmd_run(filename: str, args: str, run_state: RunState, cpu: int = None, mem: int = None,
            resume: bool = False, step: str = None, from_run_id: str = None):
    try:
        if check_file_exists(filename):                
            flow = AeroRun(filename, args, run_state, cpu, mem, resume, step, from_run_id)

            if not flow.check_parameters():
                warning = f'Warning, The args string passed does not appear to match the Parameters in {filename}' \
                          f' which means the Flow will likely fail, do you want to continue?'

                if not click.confirm(warning):
                    click.echo(red('Aborting...'))
                    return

            if flow.check_if_local_and_has_batch_decorator():

                warning = f'Warning, {BATCH_DEC} decorator detected in file and running local, please note some ' \
                            f'steps will use the cloud - do you want to continue?'
                if not click.confirm(warning):
                    click.echo(red('Aborting...'))
                    return

            if flow.check_if_local_and_has_resources_decorator():
                warning = f'Requested resources using {RESOURCE_DEC} may not match available system resources ' \
                            f'- flow may fail, do you want to continue?'
                if not click.confirm(warning):
                    click.echo(red('Aborting...'))
                    return

            r = flow.run()

            if r > 0:
                click.echo(f'Flow completed but there may have been errors: {r}')

        else:
            click.echo(red('File not found.'))
            return

    except FileNotSupported as e:
        click.echo(f'{e.filename}: {red(e.message)}!')
    except RunError:
        click.echo('There was an error running the flow.')
