from dataclasses import dataclass

from core.base_types.currency import Currency


@dataclass
class Money:
    value: int  # in cents
    currency: Currency

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Money value must be positive")
