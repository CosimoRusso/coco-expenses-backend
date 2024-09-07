from pydantic import BaseModel

from core.fiscal_entry import FiscalEntry


class FiscalEntryModel(BaseModel):
    id: str
    fiscal_entry: FiscalEntry
