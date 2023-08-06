import click
from ..utils import red, SITE_BASE, print_welcome, cyan
from .account import Account, UserNotFound, IncorrectPassword, ProvisionError, ComputeStatus, FreeTrialEnded
import webbrowser
import logging
import time
from rich.console import Console

logger = logging.getLogger(__name__)


@click.group(help="Account management")
def account():
    pass


@account.command(help="Create an account")
def create():

    print_welcome()

    click.echo(f'CLI does not currently support Account creation.')
    click.echo(f'Please create an account on our website.')
    webbrowser.open(f'{SITE_BASE}/register')
    return


@account.command(help="Login to an account")
@click.option("--email", default=None,
              help="Email address")
@click.option("--password", default=None,
              help="Password")
def login(email, password):

    print_welcome()

    if not email:
        email = click.prompt("Email > ")

    if not password:
        password = click.prompt("Password > ", hide_input=True)

    try:
        user_account = Account(email, password)
        user_account.login()

    except UserNotFound:
        click.echo(red("User not found, check username"))
        return
    except IncorrectPassword:
        click.echo(red("Password not recognised"))
        return
    except FreeTrialEnded:
        click.echo(red("*** Your free trial of Aero has ended ***"))
        click.echo("If you're interesting in using our platform more, please sign up to hear from us: " + cyan("https://site.aeroplatform.co.uk"))
        return
    except Exception as e:
        click.echo(
            red("An error occured when attempting to log in, please try again"))
        return

    try:
        provision(user_account)

    except Exception as e:
        click.echo(
            "An error occured when attempting to provision, please try again")
        logger.debug(e)

    return


def provision(user_account):

    status = ComputeStatus.NO_VALUE
    is_first_provision = False

    console = Console()

    with console.status("[bold green]Logging in...") as status:
        while status != ComputeStatus.CREATED:
            status = user_account.provision(is_first_provision)
            logger.debug(f"Current Status is {status}")

            if status == ComputeStatus.INIT:
                logger.debug(f"Initialised Compute Environment Creation")
                console.print(
                    "Initialising Compute Environment, this might take a few minutes!")
                is_first_provision = True

            if status == ComputeStatus.CREATING:
                logger.debug(f"Creating Compute Environment...")
                is_first_provision = True

            if status == ComputeStatus.CREATED:
                break

            time.sleep(30)

        click.echo("")
        click.echo("Compute Environment Created")
        click.echo(
            f"You are now ready to run Flows with Aero. For some basic tutorials, visit: {SITE_BASE}/commands")
