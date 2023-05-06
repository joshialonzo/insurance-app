from insurance.models import Agent, Customer, Policy
from insurance.services import (
    create_customer,
    create_agent,
    create_policy,
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


def test_create_agent_with_number():
    agent_number = 123456789
    agent_name = "John Doe"
    agent = create_agent(agent_name, agent_number)
    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number


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
