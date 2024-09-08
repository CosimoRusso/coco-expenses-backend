from dotenv import load_dotenv
from fastapi import FastAPI

from csv_server.model.base_model import save_model_to_csv, get_by_id
from csv_server.model.category_model import CategoryModel

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/entry_category", status_code=201)
def create_entry_category(category: CategoryModel) -> CategoryModel:
    save_model_to_csv(category)
    return category


@app.get("/entry_category/{category_id}")
def read_entry_category(category_id: int) -> CategoryModel:
    return get_by_id(CategoryModel, category_id)
