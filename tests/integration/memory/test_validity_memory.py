from insurance.repository.storage.memory import MemoryStorage
from insurance.services import (
    create_customer,
    create_policy,
    create_validity,
)

from tests.integration.memory.utils import get_first_line


def test_create_validity_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve first line from file
    first_line = get_first_line()

    # create validity with line
    policy_number = first_line[2]
    customer_name = first_line[3]
    periodicity = first_line[4]
    start_date = first_line[8]
    end_date = first_line[9]
    storage, customer = create_customer(
        storage,
        customer_name,
    )
    storage, policy = create_policy(
        storage,
        policy_number,
        customer,
        periodicity,
    )
    storage, validity = create_validity(
        storage,
        policy,
        start_date,
        end_date,
    )

    assert validity.policy == policy
    assert validity.start_date == "2023-03-30"
    assert validity.end_date == "2023-04-30"
    assert len(storage.get_validities()) == 1
