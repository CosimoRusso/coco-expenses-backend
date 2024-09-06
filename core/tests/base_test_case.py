from unittest import TestCase

from core.entry_category import EntryCategory
from core.base_types.code import Code
from core.base_types.currency import Currency
from core.base_types.money import Money

import datetime as dt


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.currency = Currency(code="EUR", symbol="€")
        self.expense_category = EntryCategory(
            code=Code("expense_category"),
            name="Expense Category",
            for_expenses=True,
        )
        self.income_category = EntryCategory(
            code=Code("income_category"),
            name="Income Category",
            for_expenses=False,
        )
        self.five_euros = Money(value=500, currency=self.currency)
        self.today = dt.date.today()
