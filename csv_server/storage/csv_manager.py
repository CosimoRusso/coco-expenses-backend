from __future__ import annotations

import csv
import os
from pathlib import Path

ROOT_CSV_FOLDER = os.getenv("ROOT_CSV_FOLDER")

__all__ = ["CSVManager"]


class CSVManager:
    def append_row_to_csv(self, instance: dict[str, str], filename: str) -> None:
        file_path = self.get_csv_file_path(filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                writer = csv.DictWriter(f, fieldnames=instance.keys())
                writer.writeheader()
        with open(file_path, "a") as f:
            writer = csv.DictWriter(f, fieldnames=instance.keys())
            writer.writerow(instance)

    @classmethod
    def read_csv(self, filename: str) -> list[dict[str, str]]:
        file_path = self.get_csv_file_path(filename)
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    @classmethod
    def remove_rows_from_csv(
        self, field_name: str, field_value: str, filename: str, limit: int | None = None
    ) -> int:
        file_path = self.get_csv_file_path(filename)
        tmp_file_path = f"{file_path}.tmp"
        content = self.read_csv(filename)
        cleaned_content = [row for row in content if row[field_name] != field_value]
        num_rows_to_delete = len(content) - len(cleaned_content)
        if limit and num_rows_to_delete > limit:
            raise ValueError(
                f"Too many rows to delete ({num_rows_to_delete}), limit is {limit}."
            )
        with open(tmp_file_path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=content[0].keys())
            writer.writeheader()
            for row in cleaned_content:
                writer.writerow(row)
        os.remove(file_path)
        os.rename(tmp_file_path, file_path)
        return num_rows_to_delete

    @classmethod
    def remove_row_from_csv(
        self, field_name: str, field_value: str, filename: str
    ) -> int:
        return self.remove_rows_from_csv(field_name, field_value, filename, limit=1)

    @classmethod
    def get_csv_file_path(self, filename: str) -> Path:
        return ROOT_CSV_FOLDER / Path(filename)

    @classmethod
    def next_id(self, filename: str) -> int:
        content = self.read_csv(filename)
        if not content:
            return 1
        return max(int(row["id"]) for row in content) + 1
