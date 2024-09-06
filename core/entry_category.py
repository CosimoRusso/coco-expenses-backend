from dataclasses import dataclass


@dataclass
class EntryCategory:
    name: str
    for_expenses: bool
