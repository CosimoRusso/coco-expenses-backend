from __future__ import annotations

from dataclasses import dataclass
import datetime as dt

from core.date_range import DateRange
from core.entry_category import EntryCategory
from core.base_types.money import Money


@dataclass(frozen=True, kw_only=True)
class FiscalEntry:
    description: str
    details: str | None
    effective_value: Money | None
    forecast_value: Money | None
    category: EntryCategory
    entry_date: dt.date
    depreciation: DateRange | None
    is_expense: bool

    def __post_init__(self) -> None:
        if not self.description:
            raise ValueError("Description cannot be empty")
        if not self.effective_value and not self.forecast_value:
            raise ValueError(
                "At least one of effective_value or forecast_value must be set"
            )
        if not self.category:
            raise ValueError("Category must be set")
        if self.is_expense is None:
            raise ValueError("is_expense must be set")
        if self.is_expense and not self.category.for_expenses:
            raise ValueError("Category must be for expenses")
        if not self.is_expense and self.category.for_expenses:
            raise ValueError("Category must be for incomes")
