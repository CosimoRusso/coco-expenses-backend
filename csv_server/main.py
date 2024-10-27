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
)
from csv_server.model.category_model import CategoryModel

load_dotenv(Path(__file__).parent / ".env")


app = FastAPI()


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


@app.put("/entry_category/{category_id}")
def update_entry_category(category: CategoryModel) -> None:
    try:
        update_entry(category)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Category with given ID not found")


@app.delete("/entry_category/{category_id}")
def delete_category(category_id: int) -> None:
    try:
        delete_entry(CategoryModel, category_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Category with given ID not found")
