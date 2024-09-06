from dataclasses import dataclass

from core.base_types.code import Code


@dataclass
class EntryCategory:
    code: Code
    name: str
    for_expenses: bool

    def __post_init__(self) -> None:
        if not self.code and self.code.value:
            raise ValueError("Code cannot be empty")
        if not self.name:
            self.name = self.code.value.replace("_", " ").capitalize()
        if self.for_expenses is None:
            raise ValueError("for_expenses must be set")
