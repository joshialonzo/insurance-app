from insurance.models import Policy
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_customer, create_policy


def test_create_policy_with_number():
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
        customer,
        policy_number,
        periodicity,
    )

    assert isinstance(policy, Policy)
    assert policy.number == policy_number
    assert policy.customer == customer
    assert policy.periodicity == periodicity
    assert len(storage.get_policies()) == 1


def test_create_policy_with_idempotency():
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
    storage, _ = create_policy(
        storage,
        customer,
        policy_number,
        periodicity,
    )
    storage, policy = create_policy(
        storage,
        customer,
        policy_number,
        periodicity,
    )

    assert isinstance(policy, Policy)
    assert policy.number == policy_number
    assert policy.customer == customer
    assert policy.periodicity == periodicity
    assert len(storage.get_policies()) == 1
