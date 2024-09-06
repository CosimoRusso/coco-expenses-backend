from dataclasses import dataclass


@dataclass
class Currency:
    code: str
    symbol: str


EUR = Currency("EUR", "€")
USD = Currency("USD", "$")
UYU = Currency("UYU", "$U")
