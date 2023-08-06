import click
from ..utils import red, RunError
import logging
import os
from ..run.commands import cmd_run
from ..run.run import AeroRun, RunState, FileNotSupported, BATCH_DEC, RESOURCE_DEC

logger = logging.getLogger(__name__)


@click.group(help="Resume a flow")
def resume():
    pass


@resume.command(help="Resume a flow locally")
@click.argument('filename')
@click.option("--step", type=str, default=None)
@click.option("--origin-run-id", type=str, default=None)
@click.option("--args", default=None,
              help="Flow arguments, must be presented as a quoted string, eg "
                   "'--arg1 arg1 --arg2 arg2'")
def local(filename, step, origin_run_id, args):
    cmd_run(filename, args, RunState.LOCAL, resume=True, step=step, from_run_id=origin_run_id)


@resume.command(help="Resume a flow in the cloud")
@click.argument('filename')
@click.option("--step", type=str, default=None)
@click.option("--origin-run-id", type=str, default=None)
@click.option("--cpu", type=int, default=None)
@click.option("--memory", type=int, default=None)
@click.option("--args", default=None,
              help="Flow arguments, must be presented as a quoted string, eg "
                   "'--arg1 arg1 --arg2 arg2'")
def cloud(filename, step, origin_run_id, cpu, memory, args):
    cmd_run(filename, args, RunState.CLOUD, cpu, memory, resume=True, step=step, from_run_id=origin_run_id)
