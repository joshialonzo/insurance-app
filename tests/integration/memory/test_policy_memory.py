from insurance.models import Customer, Policy
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_policy
from insurance.repository.sanitizers import WordSanitizer

from tests.integration.memory.utils import get_first_line


def test_create_policy_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve first line from file
    first_line = get_first_line()

    # create policy with line
    _, _, policy_number, customer_name, periodicity, *_ = first_line
    customer = Customer(name=customer_name)
    sanitizer = WordSanitizer(field="periodicity", data=periodicity)
    cleaned_periodicity = sanitizer.sanitize()
    storage, policy = create_policy(storage, customer, policy_number, cleaned_periodicity)

    assert isinstance(policy, Policy)
    assert policy.number == policy_number
    assert policy.customer == customer
    assert policy.periodicity == cleaned_periodicity
    assert len(storage.get_policies()) == 1
