from insurance.models import (Agent, Customer, Policy)


def create_customer(policy_holder, customer_number=0):
    return Customer(policy_holder, customer_number)


def create_agent(agent_number, agent_name):
    return Agent(agent_number, agent_name)


def create_policy(policy_number, customer, periodicity):
    return Policy(policy_number, customer, periodicity)


def create_validity():
    pass


def create_payment():
    pass


def create_customer_agent_policy_and_payment(line: list):
    (
        agent_number, agent_name,
        policy_number, policy_holder,
        periodicity, status, payment_amount,
        payment_date, validity_start, validity_end,
        payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number
    ) = line
    customer = create_customer(policy_holder)
    agent = create_agent(agent_number, agent_name)
    policy = create_policy(
        policy_number, customer,
        periodicity
    )
    validity = create_validity(
        policy, validity_start, validity_end,
    )
    payment = create_payment(
        payment_amount,
        validity, payment_date, status,
        payment_method, surcharge_amount,
        issuance_fee, amount_tax,
        endorsement_number,
        net_amount,
    )
    return (customer, agent, policy, validity, payment)
