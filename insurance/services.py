from typing import Union

from insurance.models import (
    Agent,
    Customer,
    Payment,
    Policy,
    Validity,
)
from insurance.repository.sanitizers import (
    DateSanitizer,
    DecimalSanitizer,
    IntegerSanitizer,
    WordSanitizer,
)
from insurance.repository.storage import Storage


def create_customer(
        storage: Storage,
        policy_holder: str,
        customer_number: int = 0,
):
    # register a new customer in the storage
    customer = Customer(policy_holder, customer_number)
    storage.add_customer(customer)
    return storage, customer


def create_agent(
        storage: Storage,
        agent_name: str,
        agent_number: int,
):
    # register a new agent in the storage
    agent = Agent(agent_name, agent_number)
    storage.add_agent(agent)
    return storage, agent


def create_policy(
        storage: Storage,
        customer: Customer,
        policy_number: int,
        periodicity: str
):
    # need to sanitize periodicity
    kwargs = {"field": "periodicity", "data": periodicity}
    sanitizer = WordSanitizer(**kwargs)
    cleaned_periodicity = sanitizer.sanitize()

    # register a new policy in the storage
    policy = Policy(policy_number, customer, cleaned_periodicity)
    storage.add_policy(policy)
    return storage, policy


def create_validity(
        storage: Storage,
        policy: Policy,
        start_date: str,
        end_date: str,
    ):
    # need to sanitize start_date
    start_date_kwargs = {"data": start_date}
    start_date_sanitizer = DateSanitizer(**start_date_kwargs)
    cleaned_start_date = start_date_sanitizer.sanitize()

    # need to sanitize end_date
    end_date_kwargs = {"data": end_date}
    end_date_sanitizer = DateSanitizer(**end_date_kwargs)
    cleaned_end_date = end_date_sanitizer.sanitize()

    # register a new validity in the storage
    validity = Validity(policy, cleaned_start_date, cleaned_end_date)
    storage.add_validity(validity)
    return storage, validity


def create_payment(
        storage: Storage,
        payment_amount: float,
        validity: Validity,
        agent: Agent,
        payment_date: str,
        status: str,
        payment_method: str,
        net_amount: Union[float, int],
        surcharge_amount: Union[float, int],
        issuance_fee: Union[float, int],
        amount_tax: Union[float, int],
        endorsement_number: int,
):
    # need to sanitize payment_amount
    payment_amount_sanitizer = DecimalSanitizer(payment_amount)
    payment_amount_cleaned = payment_amount_sanitizer.sanitize()

    # need to sanitize payment_date
    payment_date_sanitizer = DateSanitizer(data=payment_date)
    payment_date_cleaned = payment_date_sanitizer.sanitize()

    # need to sanitize status
    status_sanitizer = WordSanitizer(field="status", data=status)   
    status_cleaned = status_sanitizer.sanitize()

    # need to sanitize payment_method 
    payment_method_args = {"field": "payment_method", "data": payment_method}
    payment_method_sanitizer = WordSanitizer(**payment_method_args)
    payment_method_cleaned = payment_method_sanitizer.sanitize()

    # need to sanitize net_amount
    surcharge_amount_sanitizer = DecimalSanitizer(surcharge_amount)
    surcharge_amount_cleaned = surcharge_amount_sanitizer.sanitize()

    # need to sanitize issuance_fee
    issuance_fee_sanitizer = DecimalSanitizer(issuance_fee)
    issuance_fee_cleaned = issuance_fee_sanitizer.sanitize()

    # need to sanitize amount_tax
    amount_tax_sanitizer = DecimalSanitizer(amount_tax)
    amount_tax_cleaned = amount_tax_sanitizer.sanitize()

    # need to sanitize net_amount
    net_amount_sanitizer = DecimalSanitizer(net_amount)
    net_amount_cleaned = net_amount_sanitizer.sanitize()

    # need to sanitize endorsement_number
    endorsement_number_sanitizer = IntegerSanitizer(endorsement_number)
    endorsement_number_cleaned = endorsement_number_sanitizer.sanitize()

    # need to register a new payment in the storage
    payment = Payment(
        payment_amount_cleaned,
        validity, agent,
        payment_date_cleaned,
        status_cleaned,
        payment_method_cleaned,
        surcharge_amount_cleaned,
        issuance_fee_cleaned,
        amount_tax_cleaned,
        net_amount_cleaned,
        endorsement_number_cleaned,
    )
    storage.add_payment(payment)
    return storage, payment


def register_payment_line(storage: Storage, line: list):
    (
        agent_number, agent_name,
        policy_number, policy_holder,
        periodicity, status, payment_amount,
        payment_date, validity_start, validity_end,
        payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number,
    ) = line

    storage, customer = create_customer(storage, policy_holder)
    storage, agent = create_agent(storage, agent_name, agent_number)
    storage, policy = create_policy(
        storage, customer, policy_number, periodicity,
    )
    storage, validity = create_validity(
        storage, policy, validity_start, validity_end,
    )
    storage, payment = create_payment(
        storage,
        payment_amount,
        validity, agent,
        payment_date, status,
        payment_method,
        net_amount,
        surcharge_amount,
        issuance_fee, amount_tax,
        endorsement_number,
    )

    return (storage, customer, agent, policy, validity, payment)
