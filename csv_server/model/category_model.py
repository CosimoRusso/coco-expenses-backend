from __future__ import annotations

from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int
    code: str
    name: str
    for_expenses: bool

    def to_csv_writable_dict(self) -> dict:
        return {
            "id": self.id,
            "category": self.category,
        }

    class Meta:
        table_name = "categories"
