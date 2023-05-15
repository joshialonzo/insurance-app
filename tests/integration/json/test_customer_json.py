from insurance.models import Customer
from insurance.repository.storage.json import JsonStorage
from insurance.services import create_customer
from tests.integration.json.utils import json_database


def test_create_customer_with_line(json_database):
    database = json_database
