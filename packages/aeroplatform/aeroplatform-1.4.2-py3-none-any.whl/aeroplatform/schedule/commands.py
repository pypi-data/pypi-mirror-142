import click
import logging
from ..utils import DecoratorNotFoundException, check_file_exists, red, FileNotSupported, RunError
from .schedule import AeroScheduler, ScheduleDecoratorFormat


logger = logging.getLogger(__name__)


def cleanup_scheduler():
    AeroScheduler.kill()


@click.group(help="Schedule flows and inspect scheduled flows")
def schedule():
    pass


@schedule.command(help="Create a new scheduled Flow")
@click.argument('filename')
def create(filename):
    scheduler = _init_scheduler(filename)
    try:
        if scheduler:
            r = scheduler.create()
            if r > 0:
                click.echo(f'Task completed but there may have been errors: {r}')
        else:
            return

    except RunError:
        click.echo('There was an error creating the flow schedule.')


@schedule.command(help="View all runs of a Flow")
@click.argument('filename')
def inspect(filename):
    scheduler = _init_scheduler(filename)
    try:
        if scheduler:
            r = scheduler.inspect()
            if r > 0:
                click.echo(f'Task completed but there may have been errors: {r}')
        else:
            return

    except RunError:
        click.echo('There was an error inspecting the flow schedule.')


@schedule.command(help="Trigger a scheduled Flow to run immediately")
@click.argument('filename')
def trigger(filename):
    scheduler = _init_scheduler(filename)
    try:
        if scheduler:
            r = scheduler.trigger()
            if r > 0:
                click.echo(f'Task completed but there may have been errors: {r}')
        else:
            return

    except RunError:
        click.echo('There was an error triggering the scheduled flow.')


@schedule.command(help="View logs from a Flow")
@click.argument('filename')
def logs(filename):
    scheduler = _init_scheduler(filename)
    try:
        if scheduler:
            r = scheduler.logs()
            if r > 0:
                click.echo(f'Task completed but there may have been errors: {r}')
        else:
            return

    except RunError:
        click.echo('There was an error viewing logs for the schedule.')


@schedule.command(help="Remove a scheduled flow")
@click.argument('filename')
def remove(filename):
    scheduler = _init_scheduler(filename)
    try:
        if scheduler:
            r = scheduler.remove()
            if r > 0:
                click.echo(f'Task completed but there may have been errors: {r}')
        else:
            return

    except RunError:
        click.echo('There was an error removing the schedule.')


def _init_scheduler(filename: str) -> AeroScheduler:
    try:
        if not _check_file(filename):
            return None
        else:
            scheduler = AeroScheduler(filename)
            return scheduler

    except FileNotSupported as e:
        click.echo(f'{e.filename}: {red(e.message)}!')
    except DecoratorNotFoundException as e:
        click.echo(f'{e.decorator}: {red(e.message)}!')

    return None


def _check_file(filename: str) -> bool:
    if check_file_exists(filename):
        return True
    else:
        click.echo(red('File not found.'))

    return False
