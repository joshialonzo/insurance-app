from decimal import Decimal

from insurance.models import (
    Agent, Customer,
    Payment, Policy, Validity,
)
from insurance.services import (
    create_customer,
    create_agent,
    create_payment,
    create_policy,
    create_validity,
)


def test_create_customer_without_number():
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    assert isinstance(customer, Customer)
    assert customer.name == policy_holder
    assert customer.number == 0


def test_create_customer_with_number():
    policy_holder = "John Doe"
    customer_number = 123456789
    customer = create_customer(policy_holder, customer_number)
    assert isinstance(customer, Customer)
    assert customer.name == policy_holder
    assert customer.number == customer_number


def test_create_customer_with_idempotency():
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    Customer.register(customer)
    Customer.register(customer)
    assert len(Customer.all()) == 1


def test_create_agent_with_number():
    agent_number = 123456789
    agent_name = "John Doe"
    agent = create_agent(agent_name, agent_number)
    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number


def test_create_agent_with_idempotency():
    agent_number = 123456789
    agent_name = "John Doe"
    agent = create_agent(agent_name, agent_number)
    Agent.register(agent)
    Agent.register(agent)
    assert len(Agent.all()) == 1


def test_create_policy_with_number():
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    assert isinstance(policy, Policy)
    assert policy.number == policy_number
    assert policy.customer == customer
    assert policy.periodicity == periodicity


def test_create_policy_with_idempotency():
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    Policy.register(policy)
    Policy.register(policy)
    assert len(Policy.all()) == 1


def test_create_validity():
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    validity = create_validity(policy, start_date, end_date)
    assert validity.policy == policy
    assert validity.start_date == "2021-01-01"
    assert validity.end_date == "2021-12-31"


def test_create_validity_with_idempotency():
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    validity = create_validity(policy, start_date, end_date)
    Validity.register(validity)
    Validity.register(validity)
    assert len(Validity.all()) == 1


def test_create_payment():
    agent_number = 123456789
    agent_name = "John Doe"
    agent = create_agent(agent_name, agent_number)
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    validity = create_validity(policy, start_date, end_date)
    payment_amount = 100
    payment_date = "01/01/2021"
    status = "PAGO NORM."
    payment_method = "TARJ.CRED."
    surcharge_amount = 0
    issuance_fee = 0
    amount_tax = 0
    net_amount = 100
    endorsement_number = 0
    payment = create_payment(
        payment_amount,
        validity, agent,
        payment_date, status,
        payment_method,
        net_amount,
        surcharge_amount,
        issuance_fee,
        amount_tax,
        endorsement_number,
    )
    assert payment.payment_amount == Decimal(100)
    assert payment.validity == validity
    assert payment.date == "2021-01-01"
    assert payment.status == "normal"
    assert payment.payment_method == "credit"
    assert payment.surcharge_amount == 0
    assert payment.issuance_fee == 0
    assert payment.amount_tax == 0
    assert payment.net_amount == Decimal(100)
    assert payment.endorsement_number == 0


def test_create_payment_with_idempotency():
    agent_number = 123456789
    agent_name = "John Doe"
    agent = create_agent(agent_name, agent_number)
    policy_number = 123456789
    policy_holder = "John Doe"
    customer = create_customer(policy_holder)
    periodicity = "monthly"
    policy = create_policy(policy_number, customer, periodicity)
    start_date = "01/01/2021"
    end_date = "31/12/2021"
    validity = create_validity(policy, start_date, end_date)
    payment_amount = 100
    payment_date = "01/01/2021"
    status = "PAGO NORM."
    payment_method = "TARJ.CRED."
    surcharge_amount = 0
    issuance_fee = 0
    amount_tax = 0
    net_amount = 100
    endorsement_number = 0
    payment = create_payment(
        payment_amount,
        validity, agent,
        payment_date, status,
        payment_method, surcharge_amount,
        issuance_fee, amount_tax, net_amount,
        endorsement_number,
    )
    Payment.register(payment)
    Payment.register(payment)
    assert len(Payment.all()) == 1
