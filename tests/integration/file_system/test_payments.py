from insurance.repository.sanitizers import (
    DateSanitizer, DecimalSanitizer,
    IntegerSanitizer, WordSanitizer,
)
from insurance.repository.file_system import Storage
from insurance.models import Agent, Customer, Policy
from insurance.services import (
    create_customer,
    create_agent,
    create_payment,
    create_policy,
    create_validity,
)


def get_first_line():
    """Retrieve first line from file"""
    file = "payments.csv"
    storage = Storage(file=file)
    lines = storage.file_path_lines()
    first_line = lines[0]
    return first_line


def test_create_customer_with_line():
    # retrieve first line from file
    first_line = get_first_line()

    # create customer with line
    _, _, _, customer_name, *_ = first_line
    customer = create_customer(customer_name)
    assert isinstance(customer, Customer)
    assert customer.name == customer_name
    assert customer.number == 0


def test_create_agent_with_line():
    # retrieve first line from file
    first_line = get_first_line()

    # create agent with line
    agent_number, agent_name, *_ = first_line
    agent = create_agent(agent_name, agent_number)
    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number


def test_create_policy_with_line():
    # retrieve first line from file
    first_line = get_first_line()

    # create policy with line
    _, _, policy_number, customer_name, periodicity, *_ = first_line
    customer = Customer(name=customer_name)
    sanitizer = WordSanitizer(field="periodicity", data=periodicity)
    cleaned_periodicity = sanitizer.sanitize()
    policy = create_policy(policy_number, customer, cleaned_periodicity)
    assert isinstance(policy, Policy)
    assert policy.number == policy_number
    assert policy.customer == customer
    assert policy.periodicity == cleaned_periodicity


def test_create_validity_with_line():
    # retrieve first line from file
    first_line = get_first_line()

    # create validity with line
    (
        _, _, policy_number, customer_name,
        periodicity, _, _,
        start_date, end_date, *_
    ) = first_line
    customer = Customer(name=customer_name)

    cleaned_periodicity = WordSanitizer(
        field="periodicity",
        data=periodicity
    ).sanitize()
    cleaned_start_date = DateSanitizer(data=start_date).sanitize()
    cleaned_end_date = DateSanitizer(data=end_date).sanitize()

    policy = Policy(
        number=policy_number,
        customer=customer,
        periodicity=cleaned_periodicity
    )
    validity = create_validity(policy, cleaned_start_date, cleaned_end_date)
    assert validity.policy == policy
    assert validity.start_date == cleaned_start_date
    assert validity.end_date == cleaned_end_date


def test_create_payment_with_line():
    # retrieve first line from file
    first_line = get_first_line()

    # retrieve fields from first line
    (
        agent_number, agent_name,
        policy_number, policy_holder,
        periodicity, status, payment_amount,
        payment_date, validity_start, validity_end,
        payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number
    ) = first_line

    # create agent with line
    agent = Agent(name=agent_name, number=agent_number)

    # create customer with line
    customer = Customer(name=policy_holder)

    # create policy with line
    cleaned_periodicity = WordSanitizer(
        field="periodicity",
        data=periodicity
    ).sanitize()
    policy = Policy(
        number=policy_number,
        customer=customer,
        periodicity=cleaned_periodicity
    )

    # create validity with line
    cleaned_start_date = DateSanitizer(data=validity_start).sanitize()
    cleaned_end_date = DateSanitizer(data=validity_end).sanitize()
    validity = create_validity(policy, cleaned_start_date, cleaned_end_date)

    # create payment with line
    cleaned_payment_amount = DecimalSanitizer(payment_amount).sanitize()
    cleaned_payment_date = DateSanitizer(data=payment_date).sanitize()
    cleaned_status = WordSanitizer(field="status", data=status).sanitize()
    cleaned_payment_method = WordSanitizer(
        field="payment_method",
        data=payment_method,
    ).sanitize()
    cleaned_surcharge_amount = DecimalSanitizer(surcharge_amount).sanitize()
    cleaned_issuance_fee = DecimalSanitizer(issuance_fee).sanitize()
    cleaned_amount_tax = DecimalSanitizer(amount_tax).sanitize()
    cleaned_net_amount = DecimalSanitizer(net_amount).sanitize()
    cleaned_endorsement_number = IntegerSanitizer(endorsement_number).sanitize()
    payment = create_payment(
        cleaned_payment_amount, validity, agent,
        cleaned_payment_date, cleaned_status, cleaned_payment_method,
        cleaned_surcharge_amount, cleaned_issuance_fee,
        cleaned_amount_tax, cleaned_net_amount, cleaned_endorsement_number,
    )
    assert payment.validity == validity
    assert payment.agent == agent
    assert payment.payment_amount == cleaned_payment_amount
    assert payment.date == cleaned_payment_date
    assert payment.status == cleaned_status
    assert payment.payment_method == cleaned_payment_method
    assert payment.surcharge_amount == cleaned_surcharge_amount
    assert payment.issuance_fee == cleaned_issuance_fee
    assert payment.amount_tax == cleaned_amount_tax
    assert payment.endorsement_number == cleaned_endorsement_number
