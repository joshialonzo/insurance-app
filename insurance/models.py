from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal, Union


class User:
    def __init__(self, name, number=0):
        self.name: int = name
        self.number: int = number


class Customer(User):    
    def __repr__(self) -> str:
        return f"({self.name}, {self.number})"

    def __str__(self) -> str:
        return f"({self.name}, {self.number})"

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False
        return (
            other.name == self.name
            and
            other.number == self.number
        )

    def __hash__(self):
        return hash(f"{self.name}{self.number}")


class Agent(User):
    def __repr__(self) -> str:
        return f"({self.name}, {self.number})"

    def __eq__(self, other):
        if not isinstance(other, Agent):
            return False
        return (
            other.name == self.name
            and
            other.number == self.number
        )

    def __hash__(self):
        return hash(f"{self.name}{self.number}")


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
    
    def __str__(self) -> str:
        return (
            f"Number: {self.number}, "
            f"Customer: {self.customer}"
        )

    def __eq__(self, other):
        if not isinstance(other, Policy):
            return False
        return (
            other.number == self.number
            and
            other.customer == self.customer
        )

    def __hash__(self):
        return hash(self.number)


class Validity:
    def __init__(
            self,
            policy: Policy,
            start_date: str,
            end_date: str,
    ):
        self.policy = policy
        self.start_date = start_date
        self.end_date = end_date
    
    def __str__(self) -> str:
        return (
            f"Policy: {self.policy.number} "
            f"from {self.start_date} "
            f"to {self.end_date}"
        )

    def __eq__(self, other):
        if not isinstance(other, Validity):
            return False
        return (
            other.policy == self.policy
            and
            other.start_date == self.start_date
            and
            other.end_date == self.end_date
        )

    def __hash__(self):
        return hash(f"{self.policy}{self.start_date}{self.end_date}")

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
            agent: Agent,
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
        self.agent = agent
        self.date = date
        self.status = status
        self.payment_method = payment_method
        self.surcharge_amount = surcharge_amount
        self.issuance_fee = issuance_fee
        self.amount_tax = amount_tax
        self.net_amount = net_amount
        self.endorsement_number = endorsement_number

    def __eq__(self, other):
        if not isinstance(other, Payment):
            return False
        return (
            other.validity == self.validity
            and
            other.endorsement_number == self.endorsement_number
        )

    def __hash__(self):
        return hash(str(self.validity))

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
