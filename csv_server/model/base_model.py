from __future__ import annotations

from pydantic import BaseModel

import csv_server.csv_manager as csv_manager
from csv_server.model.category_model import CategoryModel
from csv_server.model.fiscal_entry_model import FiscalEntryModel

model_to_filename_map: dict[type[BaseModel], str] = {
    CategoryModel: "categories.csv",
    FiscalEntryModel: "fiscal_entries.csv",
}


def save_model_to_csv(model: BaseModel) -> None:
    model_as_dict = model.dict()
    if not model_as_dict["id"]:
        model_as_dict["id"] = csv_manager.next_id(model_to_filename_map[type(model)])
    csv_manager.append_row_to_csv(model_as_dict, model_to_filename_map[type(model)])
