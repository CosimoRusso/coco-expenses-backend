from pydantic import BaseModel

from core.date_range import DateRange
import datetime as dt

from csv_server.model.money_model import MoneyModel


class FiscalEntryModel(BaseModel):
    id: str | None
    description: str
    details: str | None
    effective_value: MoneyModel | None
    forecast_value: MoneyModel | None
    category_id: int
    entry_date: dt.date
    depreciation: DateRange | None
    is_expense: bool
