from insurance.models import Customer
from insurance.services import create_customer


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
