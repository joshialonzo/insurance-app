from decimal import Decimal

from insurance.models import (
    Agent, Customer,
    Payment, Policy, Validity,
)
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import register_payment_line
from insurance.services import register_payment_lines


def test_register_payment_line():
    # initialize the storage
    storage = MemoryStorage()

    line = [
        13496, # agent number
        "John Doe Agent", # agent name
        1018099, # policy number
        "John Doe Customer", # policy holder
        "MENSUAL S REC", # periodicity
        "PAGO NORM.", # status
        792.64, # payment amount
        "05/04/2023", # payment date
        "30/03/2023", # validity start
        "30/04/2023", # validity end
        "TARJ.CRED.", # payment method
        683.31, # net amount
        0, # surcharge amount
        0, # issuance fee
        109.33, # amount tax
        279484, # endorsement number
    ]

    (
        storage,
        customer,
        agent,
        policy,
        validity,
        payment,
    ) = register_payment_line(storage, line)

    assert isinstance(customer, Customer)
    assert isinstance(agent, Agent)
    assert isinstance(policy, Policy)
    assert isinstance(validity, Validity)
    assert isinstance(payment, Payment)
    assert customer.name == "John Doe Customer"
    assert customer.number == 0
    assert agent.name == "John Doe Agent"
    assert agent.number == 13496
    assert policy.number == 1018099
    assert policy.customer == customer
    assert policy.periodicity == "monthly"
    assert validity.policy == policy
    assert validity.start_date == "2023-03-30"
    assert validity.end_date == "2023-04-30"
    assert payment.payment_amount == Decimal("792.64")
    assert payment.validity == validity
    assert payment.agent == agent
    assert payment.date == "2023-04-05"
    assert payment.status == "normal"
    assert payment.payment_method == "credit"
    assert payment.net_amount == Decimal("683.31")
    assert payment.surcharge_amount == 0
    assert payment.issuance_fee == 0
    assert payment.amount_tax == Decimal("109.33")
    assert payment.endorsement_number == 279484
    assert len(storage.get_payments()) == 1


def test_register_payment_line_with_idempotency():
    # initialize the storage
    storage = MemoryStorage()

    line = [
        13496, # agent number
        "John Doe Agent", # agent name
        1018099, # policy number
        "John Doe Customer", # policy holder
        "MENSUAL S REC", # periodicity
        "PAGO NORM.", # status
        792.64, # payment amount
        "05/04/2023", # payment date
        "30/03/2023", # validity start
        "30/04/2023", # validity end
        "TARJ.CRED.", # payment method
        683.31, # net amount
        0, # surcharge amount
        0, # issuance fee
        109.33, # amount tax
        279484, # endorsement number
    ]
    
    storage, *_ = register_payment_line(storage, line)
    storage, *_ = register_payment_line(storage, line)

    assert len(storage.get_customers()) == 1
    assert len(storage.get_agents()) == 1
    assert len(storage.get_policies()) == 1
    assert len(storage.get_validities()) == 1
    assert len(storage.get_payments()) == 1


def test_register_payment_lines():
    # initialize the storage
    storage = MemoryStorage()

    line_1 = [
        13496, # agent number
        "John Doe Agent", # agent name
        1018099, # policy number
        "John Doe Customer", # policy holder
        "MENSUAL S REC", # periodicity
        "PAGO NORM.", # status
        792.64, # payment amount
        "05/04/2023", # payment date
        "30/03/2023", # validity start
        "30/04/2023", # validity end
        "TARJ.CRED.", # payment method
        683.31, # net amount
        0, # surcharge amount
        0, # issuance fee
        109.33, # amount tax
        279484, # endorsement number
    ]

    line_2 = [
        13495, # agent number
        "Juan Doe Agent", # agent name
        1018098, # policy number
        "Juan Doe Customer", # policy holder
        "MENSUAL S REC", # periodicity
        "PAGO NORM.", # status
        792.64, # payment amount
        "04/04/2023", # payment date
        "28/04/2023", # validity start
        "28/05/2023", # validity end
        "TARJ.CRED.", # payment method
        683.31, # net amount
        0, # surcharge amount
        0, # issuance fee
        109.33, # amount tax
        279484, # endorsement number
    ]

    storage, registered = register_payment_lines(
        storage, [line_1, line_2]
    )
    objects_1 = registered[0]
    customer_1 = objects_1[0]
    agent_1 = objects_1[1]
    policy_1 = objects_1[2]
    validity_1 = objects_1[3]
    payment_1 = objects_1[4]

    objects_2 = registered[1]
    customer_2 = objects_2[0]
    agent_2 = objects_2[1]
    policy_2 = objects_2[2]
    validity_2 = objects_2[3]
    payment_2 = objects_2[4]

    assert isinstance(customer_1, Customer)
    assert isinstance(agent_1, Agent)
    assert isinstance(policy_1, Policy)
    assert isinstance(validity_1, Validity)
    assert isinstance(payment_1, Payment)
    assert customer_1.name == "John Doe Customer"
    assert customer_1.number == 0
    assert agent_1.name == "John Doe Agent"
    assert agent_1.number == 13496
    assert policy_1.number == 1018099
    assert policy_1.customer == customer_1
    assert policy_1.periodicity == "monthly"
    assert validity_1.policy == policy_1
    assert validity_1.start_date == "2023-03-30"
    assert validity_1.end_date == "2023-04-30"
    assert payment_1.payment_amount == Decimal("792.64")
    assert payment_1.validity == validity_1
    assert payment_1.agent == agent_1
    assert payment_1.date == "2023-04-05"
    assert payment_1.status == "normal"
    assert payment_1.payment_method == "credit"
    assert payment_1.net_amount == Decimal("683.31")
    assert payment_1.surcharge_amount == 0
    assert payment_1.issuance_fee == 0
    assert payment_1.amount_tax == Decimal("109.33")
    assert payment_1.endorsement_number == 279484

    assert isinstance(customer_2, Customer)
    assert isinstance(agent_2, Agent)
    assert isinstance(policy_2, Policy)
    assert isinstance(validity_2, Validity)
    assert isinstance(payment_2, Payment)
    assert customer_2.name == "Juan Doe Customer"
    assert customer_2.number == 0
    assert agent_2.name == "Juan Doe Agent"
    assert agent_2.number == 13495
    assert policy_2.number == 1018098
    assert policy_2.customer == customer_2
    assert policy_2.periodicity == "monthly"
    assert validity_2.policy == policy_2
    assert validity_2.start_date == "2023-04-28"
    assert validity_2.end_date == "2023-05-28"
    assert payment_2.payment_amount == Decimal("792.64")
    assert payment_2.validity == validity_2
    assert payment_2.agent == agent_2
    assert payment_2.date == "2023-04-04"
    assert payment_2.status == "normal"
    assert payment_2.payment_method == "credit"
    assert payment_2.net_amount == Decimal("683.31")
    assert payment_2.surcharge_amount == 0
    assert payment_2.issuance_fee == 0
    assert payment_2.amount_tax == Decimal("109.33")
    assert payment_2.endorsement_number == 279484

    assert len(storage.get_payments()) == 2
