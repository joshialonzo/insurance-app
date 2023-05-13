from insurance.models import Customer
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_customer


def test_create_customer_without_number():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer without a number
    policy_holder = "John Doe"
    storage, customer = create_customer(storage, policy_holder)

    assert isinstance(customer, Customer)
    assert customer.name == policy_holder
    assert customer.number == 0
    assert len(storage.get_customers()) == 1


def test_create_customer_with_number():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_holder = "John Doe"
    customer_number = 123456789
    storage, customer = create_customer(
        storage, policy_holder, customer_number
    )

    assert isinstance(customer, Customer)
    assert customer.name == policy_holder
    assert customer.number == customer_number
    assert len(storage.get_customers()) == 1


def test_create_customer_with_idempotency():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_holder = "John Doe"
    create_customer(storage, policy_holder)
    create_customer(storage, policy_holder)

    assert len(storage.get_customers()) == 1
