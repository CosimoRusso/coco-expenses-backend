from __future__ import annotations

from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int
    code: str
    name: str
    for_expenses: bool
