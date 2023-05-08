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


def create_customer(policy_holder, customer_number=0):
    return Customer(policy_holder, customer_number)


def create_agent(agent_number, agent_name):
    return Agent(agent_number, agent_name)


def create_policy(policy_number, customer, periodicity):
    # need to sanitize periodicity
    kwargs = {"field": "periodicity", "data": periodicity}
    sanitizer = WordSanitizer(**kwargs)
    cleaned_periodicity = sanitizer.sanitize()

    return Policy(policy_number, customer, cleaned_periodicity)


def create_validity(policy, start_date, end_date):
    # need to sanitize start_date
    start_date_kwargs = {"data": start_date}
    start_date_sanitizer = DateSanitizer(**start_date_kwargs)
    cleaned_start_date = start_date_sanitizer.sanitize()

    # need to sanitize end_date
    end_date_kwargs = {"data": end_date}
    end_date_sanitizer = DateSanitizer(**end_date_kwargs)
    cleaned_end_date = end_date_sanitizer.sanitize()

    return Validity(policy, cleaned_start_date, cleaned_end_date)


def create_payment(
        payment_amount, validity, agent, payment_date,
        status, payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number,
):
    payment_amount_sanitizer = DecimalSanitizer(payment_amount)
    payment_amount_cleaned = payment_amount_sanitizer.sanitize()

    payment_date_sanitizer = DateSanitizer(data=payment_date)
    payment_date_cleaned = payment_date_sanitizer.sanitize()

    status_sanitizer = WordSanitizer(field="status", data=status)   
    status_cleaned = status_sanitizer.sanitize()
    
    payment_method_args = {"field": "payment_method", "data": payment_method}
    payment_method_sanitizer = WordSanitizer(**payment_method_args)
    payment_method_cleaned = payment_method_sanitizer.sanitize()

    surcharge_amount_sanitizer = DecimalSanitizer(surcharge_amount)
    surcharge_amount_cleaned = surcharge_amount_sanitizer.sanitize()

    issuance_fee_sanitizer = DecimalSanitizer(issuance_fee)
    issuance_fee_cleaned = issuance_fee_sanitizer.sanitize()

    amount_tax_sanitizer = DecimalSanitizer(amount_tax)
    amount_tax_cleaned = amount_tax_sanitizer.sanitize()

    net_amount_sanitizer = DecimalSanitizer(net_amount)
    net_amount_cleaned = net_amount_sanitizer.sanitize()

    endorsement_number_sanitizer = IntegerSanitizer(endorsement_number)
    endorsement_number_cleaned = endorsement_number_sanitizer.sanitize()

    return Payment(
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


def create_customer_agent_policy_and_payment(line: list):
    (
        agent_number, agent_name,
        policy_number, policy_holder,
        periodicity, status, payment_amount,
        payment_date, validity_start, validity_end,
        payment_method, net_amount, surcharge_amount,
        issuance_fee, amount_tax, endorsement_number,
    ) = line

    customer = create_customer(policy_holder)
    Customer.register(customer)

    agent = create_agent(agent_name, agent_number)
    Agent.register(agent)

    policy = create_policy(
        policy_number, customer,
        periodicity
    )
    Policy.register(policy)

    validity = create_validity(
        policy, validity_start, validity_end,
    )
    Validity.register(validity)

    payment = create_payment(
        payment_amount,
        validity, agent,
        payment_date, status,
        payment_method,
        net_amount,
        surcharge_amount,
        issuance_fee, amount_tax,
        endorsement_number,
    )
    Payment.register(payment)

    return (customer, agent, policy, validity, payment)
