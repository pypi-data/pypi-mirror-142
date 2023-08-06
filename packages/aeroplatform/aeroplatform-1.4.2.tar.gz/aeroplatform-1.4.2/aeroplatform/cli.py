import click
import os
import logging
import sys
from .account.commands import account
from .run.commands import run, cleanup_run
from .schedule.commands import schedule, cleanup_scheduler
from .resume.commands import resume
from .configure.commands import configure, cleanup_install
import signal

logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

logger = logging.getLogger(__name__)


def signal_handler(sig, frame):
    logger.debug("SIGINT detected, cleaning up active runs")
    cleanup_run()
    cleanup_scheduler()
    cleanup_install()
    sys.exit(0)


@click.group()
def cli():
    logging.basicConfig(stream=sys.stdout, level=os.environ.get('LOGLEVEL', 'INFO').upper(),
                        format='%(filename)s %(lineno)d: %(message)s')
    signal.signal(signal.SIGINT, signal_handler)
    pass


cli.add_command(account)
cli.add_command(run)
cli.add_command(resume)
cli.add_command(schedule)
cli.add_command(configure)


if __name__ == '__main__':
    cli()
