import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("dummy", short_help="CSPM dummy command for future usage")
@pass_environment
def cli(ctx):
    result = "CSPM dummy command for future usage."
    prismacloud.cli.output(result)