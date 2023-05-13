from insurance.repository.storage.memory import MemoryStorage
from insurance.services import (
    create_customer,
    create_policy,
    create_validity
)


def test_create_validity():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_number = 123456789
    policy_holder = "John Doe"
    storage, customer = create_customer(
        storage,
        policy_holder,
    )

    # create a policy with a number
    periodicity = "monthly"
    storage, policy = create_policy(
        storage,
        policy_number,
        customer,
        periodicity,
    )

    # create a validity
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    storage, validity = create_validity(
        storage,
        policy,
        start_date,
        end_date,
    )

    assert validity.policy == policy
    assert validity.start_date == "2021-01-01"
    assert validity.end_date == "2021-12-31"
    assert len(storage.get_validities()) == 1


def test_create_validity_with_idempotency():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_number = 123456789
    policy_holder = "John Doe"
    storage, customer = create_customer(
        storage,
        policy_holder,
    )

    # create a policy with a number
    periodicity = "monthly"
    storage, policy = create_policy(
        storage,
        policy_number,
        customer,
        periodicity,
    )

    # create a validity
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    storage, _ = create_validity(
        storage,
        policy,
        start_date,
        end_date,
    )
    storage, validity = create_validity(
        storage,
        policy,
        start_date,
        end_date,
    )

    assert validity.policy == policy
    assert validity.start_date == "2021-01-01"
    assert validity.end_date == "2021-12-31"
    assert len(storage.get_validities()) == 1
