class MemoryStorage:
    def __init__(self):
        self.data: dict[str, list[dict[str, str]]] = {}

    def append_row_to_csv(self, instance: dict[str, str], filename: str) -> None:
        if filename not in self.data:
            self.data[filename] = []
        self.data[filename].append(instance)

    def read_csv(self, filename: str) -> list[dict[str, str]]:
        return self.data.get(filename, [])

    def remove_rows_from_csv(
        self, field_name: str, field_value: str, filename: str, limit: int | None = None
    ) -> int:
        # Remove the rows and returns the count of removed rows. If count is greater than limit, raise ValueError.
        content = self.data.get(filename, [])
        cleaned_content = [row for row in content if row[field_name] != field_value]
        num_rows_to_delete = len(content) - len(cleaned_content)
        if limit and num_rows_to_delete > limit:
            raise ValueError(
                f"Too many rows to delete ({num_rows_to_delete}), limit is {limit}."
            )
        self.data[filename] = cleaned_content
        return num_rows_to_delete

    def remove_row_from_csv(
        self, field_name: str, field_value: str, filename: str
    ) -> int:
        return self.remove_rows_from_csv(field_name, field_value, filename, limit=1)

    def next_id(self, filename: str) -> int:
        content = self.data.get(filename, [])
        if not content:
            return 1
        return max(int(row["id"]) for row in content) + 1
