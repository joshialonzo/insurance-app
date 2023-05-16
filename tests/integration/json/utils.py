from pathlib import Path

import pytest

from insurance.repository.storage.json import JsonStorage


@pytest.fixture
def json_database():
    path = Path.home().joinpath("test_insurance.json")
    storage = JsonStorage(db_path=path)
    storage.create_file()
    yield storage
    storage.remove_file()
