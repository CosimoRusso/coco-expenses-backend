from pydantic import BaseModel


class MoneyModel(BaseModel):
    value_eur: int  # in cents
    value_original_currency: int | None = None  # in cents
    currency_code: str = "EUR"
