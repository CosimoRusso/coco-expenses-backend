from core.date_range import DateRange
from core.fiscal_entry import FiscalEntry
from core.tests.base_test_case import BaseTestCase


class TestCreateEntry(BaseTestCase):
    def test_create_entry(self) -> None:
        # Create an entry
        entry = FiscalEntry(
            description="Test Entry",
            details="This is a test entry.",
            effective_value=self.five_euros,
            forecast_value=self.five_euros,
            category=self.expense_category,
            entry_date=self.today,
            depreciation=DateRange(self.today, self.today),
            is_expense=True,
        )
        # Check the entry
        self.assertEqual(entry.description, "Test Entry")
        self.assertEqual(entry.details, "This is a test entry.")
        self.assertEqual(entry.effective_value, self.five_euros)
        self.assertEqual(entry.forecast_value, self.five_euros)
        self.assertEqual(entry.category, self.expense_category)
        self.assertEqual(entry.entry_date, self.today)
        self.assertEqual(entry.depreciation, DateRange(self.today, self.today))
        self.assertTrue(entry.is_expense)
