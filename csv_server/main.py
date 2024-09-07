from fastapi import FastAPI

from csv_server.model.base_model import save_model_to_csv
from csv_server.model.category_model import CategoryModel

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/entry_category")
def create_entry_category(category: CategoryModel) -> CategoryModel:
    save_model_to_csv(category)
    return category
