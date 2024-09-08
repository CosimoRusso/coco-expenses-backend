from typing import Protocol


class StorageInterface(Protocol):
    def append_row_to_csv(self, instance: dict[str, str], filename: str) -> None: ...

    def read_csv(self, filename: str) -> list[dict[str, str]]: ...

    def remove_rows_from_csv(
        self, field_name: str, field_value: str, filename: str, limit: int | None = None
    ) -> int: ...

    def remove_row_from_csv(
        self, field_name: str, field_value: str, filename: str
    ) -> int: ...

    def next_id(self, filename: str) -> int: ...
