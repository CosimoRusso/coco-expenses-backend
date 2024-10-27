from __future__ import annotations

import os

from csv_server.storage.csv_manager import CSVManager
from csv_server.model.category_model import CategoryModel
from csv_server.model.fiscal_entry_model import FiscalEntryModel
from csv_server.storage.memory_storage import MemoryStorage
from csv_server.storage.storage_interface import StorageInterface

Model = CategoryModel | FiscalEntryModel
ModelType = type[CategoryModel] | type[FiscalEntryModel]

env = os.environ.get("ENV")


model_to_filename_map: dict[ModelType, str] = {
    CategoryModel: "categories.csv",
    FiscalEntryModel: "fiscal_entries.csv",
}

storage: StorageInterface = CSVManager() if env != "TEST" else MemoryStorage()


class NotFoundError(Exception):
    pass


def save_model_to_csv(model: Model) -> dict:
    model_as_dict = model.dict()
    if not model_as_dict["id"]:
        model_as_dict["id"] = str(storage.next_id(model_to_filename_map[type(model)]))
    storage.append_row_to_csv(model_as_dict, model_to_filename_map[type(model)])
    return model_as_dict


def get_by_id(model_type: ModelType, model_id: int) -> Model:
    filename = model_to_filename_map[model_type]
    entry = next(
        (row for row in storage.read_csv(filename) if str(row["id"]) == str(model_id)),
        None,
    )
    if not entry:
        raise NotFoundError()
    return model_type.parse_obj(entry)


def get_all(model_type: ModelType) -> list[Model]:
    filename = model_to_filename_map[model_type]
    entries = storage.read_csv(filename)
    return [model_type.parse_obj(entry) for entry in entries]


def update_entry(model: Model) -> dict:
    model_as_dict = model.dict()
    num_removed = storage.remove_row_from_csv(
        "id", str(model_as_dict["id"]), model_to_filename_map[type(model)]
    )
    if num_removed == 0:
        raise NotFoundError()
    storage.append_row_to_csv(model_as_dict, model_to_filename_map[type(model)])
    return {"status": "OK"}


def delete_entry(model_type: ModelType, model_id: int) -> dict:
    num_removed = storage.remove_row_from_csv(
        "id", str(model_id), model_to_filename_map[model_type]
    )
    if num_removed == 0:
        raise NotFoundError()
    return {"status": "OK"}
