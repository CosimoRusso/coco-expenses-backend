from __future__ import annotations

from storage.csv_manager import CSVManager
from csv_server.model.category_model import CategoryModel
from csv_server.model.fiscal_entry_model import FiscalEntryModel
from storage.memory_storage import MemoryStorage
from settings import ENV
from storage.storage_interface import StorageInterface

Model = CategoryModel | FiscalEntryModel
ModelType = type[CategoryModel] | type[FiscalEntryModel]


model_to_filename_map: dict[ModelType, str] = {
    CategoryModel: "categories.csv",
    FiscalEntryModel: "fiscal_entries.csv",
}

storage: StorageInterface = CSVManager() if ENV != "TEST" else MemoryStorage()


def save_model_to_csv(model: Model) -> None:
    model_as_dict = model.dict()
    if not model_as_dict["id"]:
        model_as_dict["id"] = str(storage.next_id(model_to_filename_map[type(model)]))
    storage.append_row_to_csv(model_as_dict, model_to_filename_map[type(model)])


def get_by_id(model_type: ModelType, model_id: int) -> Model:
    filename = model_to_filename_map[model_type]
    entry = next(
        (row for row in storage.read_csv(filename) if str(row["id"]) == str(model_id)),
    )
    return model_type.parse_obj(entry)
