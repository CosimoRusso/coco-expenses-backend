from dataclasses import dataclass
import datetime as dt


@dataclass
class DateRange:
    start_date: dt.date
    end_date: dt.date

    def __post_init__(self) -> None:
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before end date")
