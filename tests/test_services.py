from decimal import Decimal

from insurance.models import (
    Agent, Customer,
    Payment, Policy, Validity,
)
from insurance.services import create_customer_agent_policy_and_payment


def test_create_customer_agent_policy_and_payment():
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
        customer,
        agent,
        policy,
        validity,
        payment,
    ) = create_customer_agent_policy_and_payment(line)
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
