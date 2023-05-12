"""This module provides the Insurance CLI."""
# insurance/ui/cli.py

from typing import Optional

import typer

from insurance import __app_name__, __version__


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(
            f"{__app_name__} version {__version__}"
        )
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return None
