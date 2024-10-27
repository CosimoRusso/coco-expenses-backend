from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from csv_server.model.base_model import (
    save_model_to_csv,
    get_by_id,
    NotFoundError,
    update_entry,
    get_all,
    delete_entry,
    ModelType,
)
from csv_server.model.category_model import CategoryModel
from csv_server.model.fiscal_entry_model import FiscalEntryModel

load_dotenv(Path(__file__).parent / ".env")


app = FastAPI()


def delete(model_type: ModelType, entry_id: int) -> dict:
    try:
        delete_entry(model_type, entry_id)
        return {"status": "OK"}
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Category with given ID not found")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/entry_category", status_code=201)
def create_entry_category(category: CategoryModel) -> dict:
    stored_category = save_model_to_csv(category)
    return stored_category


@app.get("/entry_category/{category_id}")
def read_entry_category(category_id: int) -> CategoryModel:
    try:
        return get_by_id(CategoryModel, category_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Category with given ID not found")


@app.get("/entry_category")
def read_entry_category() -> list[CategoryModel]:
    return get_all(CategoryModel)


@app.put("/entry_category")
def update_entry_category(category: CategoryModel) -> None:
    try:
        update_entry(category)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Category with given ID not found")


@app.delete("/entry_category/{category_id}")
def delete_category(category_id: int) -> dict:
    return delete(CategoryModel, category_id)


@app.post("/fiscal_entry", status_code=201)
def create_fiscal_entry(fiscal_entry: FiscalEntryModel) -> dict:
    category_id = fiscal_entry.category_id
    if category_id not in [category.id for category in get_all(CategoryModel)]:
        raise HTTPException(status_code=404, detail="Category with given ID not found")
    stored_fiscal_entry = save_model_to_csv(fiscal_entry)
    return stored_fiscal_entry


@app.delete("/fiscal_entry/{fiscal_entry_id}")
def delete_fiscal_entry(fiscal_entry_id: int) -> dict:
    return delete(FiscalEntryModel, fiscal_entry_id)


@app.get("/fiscal_entry")
def read_fiscal_entry() -> list[FiscalEntryModel]:
    return get_all(FiscalEntryModel)


@app.put("/fiscal_entry")
def update_fiscal_entry(fiscal_entry: FiscalEntryModel) -> dict:
    category_id = fiscal_entry.category_id
    if category_id not in [category.id for category in get_all(CategoryModel)]:
        raise HTTPException(status_code=404, detail="Category with given ID not found")
    try:
        update_entry(fiscal_entry)
        return {"status": "OK"}
    except NotFoundError:
        raise HTTPException(
            status_code=404, detail="Fiscal entry with given ID not found"
        )
