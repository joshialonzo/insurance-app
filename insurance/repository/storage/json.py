"""This module provides the Insurance database functionality."""

# insurance/repository/storage/json.py

import configparser
from pathlib import Path

from insurance import DB_WRITE_ERROR, SUCCESS


DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_insurance.json"
)


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the Insurance database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    """Create the Insurance database."""
    try:
        db_path.write_text("[]")  # Empty payments list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
