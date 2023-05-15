"""This module provides the Insurance database functionality."""

# insurance/repository/storage/json.py

import configparser
import json
from pathlib import Path
from typing import Any, Dict, NamedTuple

from insurance import (
    DB_READ_ERROR, DB_WRITE_ERROR,
    JSON_ERROR, SUCCESS,
)
from insurance.models import Customer
from insurance.repository.storage import Storage


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


class DBResponse(NamedTuple):
    """A database response."""
    data: Dict[str, Any]
    status: int


class JsonStorage(Storage):
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
    
    def create_file(self) -> None:
        with self._db_path.open("w") as db:
            schema = {
                "customers": {},
                "agents": {},
                "policies": {},
                "validities": {},
                "payments": {},
            }
            json.dump(schema, db, indent=4)

    def add_customer(self, customer: Customer) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                # customers
                customer_json: dict = customer.to_json()
                response: DBResponse = self.get_customers()
                customers_list: list = response.data
                customers_list.append(customer_json)
                # file content
                try:
                    file_content = json.load(db)
                    file_content["customers"] = customers_list
                    json.dump(file_content, db, indent=4)
                except json.JSONDecodeError:  # Catch wrong JSON format
                    return DBResponse(customers_list, JSON_ERROR)
            return DBResponse(customers_list, SUCCESS)
        except OSError:  # Catch file IO problems
            return DBResponse(customers_list, DB_WRITE_ERROR)

    def get_customers(self)-> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    data = json.load(db)
                    customers = data["customers"]
                    return DBResponse(
                        data=customers,
                        status=SUCCESS,
                    )
                except json.JSONDecodeError:
                    # Catch wrong JSON format
                    return DBResponse([], JSON_ERROR)
        except OSError:
            # Catch file IO problems
            return DBResponse([], DB_READ_ERROR)

    def add_agent(self, agent)-> DBResponse:
        pass

    def get_agents(self)-> DBResponse:
        pass

    def add_policy(self, policy)-> DBResponse:
        pass

    def get_policies(self)-> DBResponse:
        pass

    def add_validity(self, validity)-> DBResponse:
        pass

    def get_validities(self)-> DBResponse:
        pass

    def add_payment(self, payment)-> DBResponse:
        pass

    def get_payments()-> DBResponse:
        pass
