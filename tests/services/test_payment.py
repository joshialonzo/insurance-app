from decimal import Decimal

from insurance.services import (
    create_customer,
    create_agent,
    create_payment,
    create_policy,
    create_validity,
)
from insurance.repository.storage.memory import MemoryStorage


def test_create_payment():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_number = 123456789
    policy_holder = "John Doe Customer"
    storage, customer = create_customer(
        storage,
        policy_holder,
    )

    # create an agent with a number
    agent_number = 123456789
    agent_name = "John Doe Agent"
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
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

    # create a payment
    payment_amount = 100
    payment_date = "01/01/2021"
    status = "PAGO NORM."
    payment_method = "TARJ.CRED."
    surcharge_amount = 0
    issuance_fee = 0
    amount_tax = 0
    net_amount = 100
    endorsement_number = 0
    storage, payment = create_payment(
        storage,
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
    assert len(storage.get_payments()) == 1


def test_create_payment_with_idempotency():
    # initialize the storage
    storage = MemoryStorage()

    # create a customer with a number
    policy_number = 123456789
    policy_holder = "John Doe Customer"
    storage, customer = create_customer(
        storage,
        policy_holder,
    )

    # create an agent with a number
    agent_number = 123456789
    agent_name = "John Doe Agent"
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
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

    # create a payment
    payment_amount = 100
    payment_date = "01/01/2021"
    status = "PAGO NORM."
    payment_method = "TARJ.CRED."
    surcharge_amount = 0
    issuance_fee = 0
    amount_tax = 0
    net_amount = 100
    endorsement_number = 0
    storage, _ = create_payment(
        storage,
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
    storage, payment = create_payment(
        storage,
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
    assert len(storage.get_payments()) == 1
