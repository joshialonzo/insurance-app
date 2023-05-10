from decimal import Decimal

from insurance.repository.sanitizers import WordSanitizer
from insurance.repository.sanitizers.csv.file_sanitizer import (
    PaymentsFileSanitizer,
)
from insurance.repository.input.file_system import FileSystem
from insurance.models import Agent, Customer, Policy
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import (
    create_customer,
    create_agent,
    create_payment,
    create_policy,
    create_validity,
    register_payment_lines,
)


def get_first_line():
    """Retrieve first line from file"""
    file = "payments.csv"
    file_system = FileSystem(file=file)
    lines = file_system.file_path_lines()
    first_line = lines[0]
    return first_line


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


def test_create_agent_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve first line from file
    first_line = get_first_line()

    # create agent with line
    agent_number, agent_name, *_ = first_line
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
    )

    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number
    assert len(storage.get_agents()) == 1


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


def test_create_payment_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve fields from first line
    first_line = get_first_line()
    (
        agent_number, agent_name,
        policy_number, policy_holder,
        periodicity, status, payment_amount,
        payment_date, validity_start, validity_end,
        payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number
    ) = first_line

    # create agent, customer, policy, validity, payment
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
    )
    storage, customer = create_customer(storage, policy_holder)
    storage, policy = create_policy(
        storage,
        policy_number,
        customer,
        periodicity,
    )
    storage, validity = create_validity(
        storage,
        policy,
        validity_start,
        validity_end,
    )
    storage, payment = create_payment(
        storage,
        payment_amount, validity, agent,
        payment_date, status,
        payment_method, net_amount,
        surcharge_amount, issuance_fee,
        amount_tax, endorsement_number,
    )

    # assert payment fields
    assert payment.validity == validity
    assert payment.agent == agent
    assert payment.payment_amount == Decimal("792.64")
    assert payment.date == "2023-04-05"
    assert payment.status == "normal"
    assert payment.payment_method == "credit"
    assert payment.surcharge_amount == 0
    assert payment.issuance_fee == 0
    assert payment.amount_tax == Decimal("109.33")
    assert payment.endorsement_number == 279484
    assert len(storage.get_payments()) == 1


def test_create_payment_with_lines():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve all the lines from file
    file = "payments.csv"
    file_system = FileSystem(file=file)
    lines = file_system.file_path_lines()
    sanitized_lines = PaymentsFileSanitizer(lines=lines).sanitize()

    # save all the lines in memory
    storage, registered = register_payment_lines(storage, sanitized_lines)

    # assert all the lines were saved
    assert len(registered) == 134
    assert len(storage.get_payments()) == 134
