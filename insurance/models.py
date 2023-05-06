from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal, Union


class User:
    def __init__(self, name, number=0):
        self.name: int = name
        self.number: int = number


class Customer(User):
    pass


class Agent(User):
    pass


class Policy:
    def __init__(
            self,
            number: int,
            customer: Customer,
            periodicity: Literal[
                "monthly", "quarterly",
                "biannual", "annual",
            ] = "monthly",
    ):
        self.number = number
        self.customer = customer
        self.periodicity = periodicity


class Validity:
    def __init__(
            self,
            policy: Policy,
            start_date: date,
            end_date: date,
    ):
        self.policy = policy
        self.start_date = start_date
        self.end_date = end_date
    
    @property
    def month(self) -> str:
        """Use calendar library to get the month"""
        pass

    @property
    def year(self):
        """Use calendar library to get the year"""
        pass


class Payment:
    def __init__(
            self,
            payment_amount: Union[int, Decimal],
            validity: Validity,
            date: date,
            status: Literal["normal"] = "normal",
            payment_method: Literal[
                "debit", "credit",
                "amex", "agent",
            ] = "debit",
            surcharge_amount: Union[int, Decimal] = 0,
            issuance_fee: Union[int, Decimal] = 0,
            amount_tax: Union[int, Decimal] = 0,
            net_amount: Union[int, Decimal] = 0,
            endorsement_number: Union[int, Decimal] = 0,
    ):
        self.payment_amount = Decimal(payment_amount)
        self.validity = validity
        self.date = date
        self.status = status
        self.payment_method = payment_method
        self.surcharge_amount = surcharge_amount
        self.issuance_fee = issuance_fee
        self.amount_tax = amount_tax
        self.net_amount = net_amount
        self.endorsement_number = endorsement_number
    
    def validate_net_amount(self):
        """Validate the net amount"""
        pass


class Report:
    def __init__(self, name):
        self.name = name


@dataclass(frozen=True)
class ReportItem:
    report: Report
    description: str = ""
