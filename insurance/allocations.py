"""
1. OrderLine is an immutable dataclass with no behavior.
2. We're not showing imports in most code listings, in an attempt to keep them clean.
We're hoping you can guess that this came via from dataclasses import dataclass;
likewise, typing.Optional and datetime.date. If you want to double-check anything,
you can see the full working code for each chapter in its branch (e.g., chapter_01_domain_model).
3. Type hints are still a matter of controversy in the Python world. For domain models,
they can sometimes help to clarify or document what the expected arguments are,
and people with IDEs are often grateful for them.
You may decide the price paid in terms of readability is too high.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)  #(1) (2)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):  #(2)
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def allocate(self, line: OrderLine):  #(3)
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
