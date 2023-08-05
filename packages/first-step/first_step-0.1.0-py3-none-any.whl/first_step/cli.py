import click

from .increment import increment


@click.command()
@click.argument("number", type=int)
def cli(number: int):
    click.echo(
        "{} has become {}!".format(
            click.style(number, bold=True),
            click.style(increment(number), bold=True, fg="green"),
        )
    )
