from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal, Union


class User:
    def __init__(self, number, name):
        self.number: int = number
        self.name: int = name


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
            validity: Validity,
            date: date,
            status: Literal["normal"] = "normal",
            payment_type: Literal[
                "debit", "credit",
                "amex", "agent",
            ] = "debit",
            surcharge: Union[int, Decimal] = 0,
            issuance_fee: Union[int, Decimal] = 0,
            taxes: Union[int, Decimal] = 0,
            net_amount: Union[int, Decimal] = 0,
            endorsement_id: Union[int, Decimal] = 0,
    ):
        self.validity = validity
        self.date = date
        self.status = status
        self.payment_type = payment_type
        self.surcharge = surcharge
        self.issuance_fee = issuance_fee
        self.taxes = taxes
        self.net_amount = net_amount
        self.endorsement_id = endorsement_id


class Report:
    def __init__(self, name):
        self.name = name


@dataclass(frozen=True)
class ReportItem:
    report: Report
    description: str = ""
