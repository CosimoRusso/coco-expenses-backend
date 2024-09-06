from dataclasses import dataclass


@dataclass
class EntryCategory:
    name: str
    for_expenses: bool

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.for_expenses is None:
            raise ValueError("for_expenses must be set")
