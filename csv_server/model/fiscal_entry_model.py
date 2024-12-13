from pydantic import BaseModel

import datetime as dt


class FiscalEntryModel(BaseModel):
    id: int | None = None
    description: str
    details: str | None
    effective_value: int | None
    forecast_value: int | None
    currency: str = "EUR"
    category_id: int
    entry_date: dt.date
    depreciation_start_date: dt.date
    depreciation_end_date: dt.date
    is_expense: bool
