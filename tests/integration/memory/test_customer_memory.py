from insurance.models import Customer
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_customer

from tests.integration.memory.utils import get_first_line


def test_create_customer_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve first line from file
    first_line = get_first_line()

    # create customer with line
    _, _, _, customer_name, *_ = first_line
    storage, customer = create_customer(
        storage,
        customer_name,
    )
    assert isinstance(customer, Customer)
    assert customer.name == customer_name
    assert customer.number == 0
    assert len(storage.get_customers()) == 1
