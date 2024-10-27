from __future__ import annotations

from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int | None
    code: str
    name: str
    for_expenses: bool
