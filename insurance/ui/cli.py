"""This module provides the Insurance CLI."""
# insurance/ui/cli.py

from pathlib import Path
from typing import Optional

import typer

from insurance import (
    ERRORS,
    __app_name__,
    __version__,
    config,
)
from insurance.repository.storage import (
    json as json_database,
)


app = typer.Typer()


@app.command()
def init(
    db_path: Optional[str] = typer.Option(
        str(json_database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="Path to the Insurance database location?",
    ),
) -> None:
    """Initialize the Insurance database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f"Creating config file failed with \"{ERRORS[app_init_error]}\"",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = json_database.init_database(Path(db_path))

    if db_init_error:
        typer.secho(
            f"Creating database failed with \"{ERRORS[db_init_error]}\"",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"The Insurance database is {db_path}",
            fg=typer.colors.GREEN,
        )


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
    ),
) -> None:
    return None
