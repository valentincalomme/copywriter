"""Command line application."""

import typer

from copywriter import __doc__, __version__

app = typer.Typer()


@app.command()
def about() -> None:
    """Display copywriter's tagline."""
    typer.echo(__doc__)


@app.command()
def version() -> None:
    """Display copywriter's version."""
    typer.echo(__version__)
