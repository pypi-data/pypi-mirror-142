import click

"""
This module contains a default command line wrapper
for customers of zeit.shipit to use as entry point.

"""


@click.group()
@click.pass_context
@click.option("--debug/--no-debug", default=False)
def cli(ctx, debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command()
@click.argument("environment",)
@click.pass_context
def run(ctx, environment):
    ctx.obj.run_skaffold_run(environment)


@cli.command()
@click.option(
    "--version",
    type=str,
    default=None,
    help="""optionally set release version explicitly.
    If none is given the default is used.""",
)
@click.option(
    "--rebuild", is_flag=True, default=False, help="allow re-releasing existing tag"
)
@click.pass_context
@click.option(
    "--draft/--no-draft",
    default=False,
    help="only shows the changelog and builds the image but does not commit anything",
)
def release(ctx, version=None, rebuild=False, draft=False):
    ctx.obj.release(version=version, rebuild=rebuild, draft=draft)


@cli.command()
@click.option(
    "--version",
    type=str,
    default=None,
    help="""optionally set deployment version explicitly
        (i.e. to perform a rollback).
        If none is given the most recently released version is used.""",
)
@click.argument("environment",)
@click.pass_context
def deploy(ctx, environment, version=None):
    ctx.obj.deploy(environment)
