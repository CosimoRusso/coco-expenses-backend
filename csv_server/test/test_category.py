from fastapi.testclient import TestClient
from csv_server.main import app

client = TestClient(app)


def test_create_category() -> None:
    category_json = {"id": 1, "code": "test", "name": "Test", "for_expenses": True}
    response = client.post("/entry_category", json=category_json)
    assert response.status_code == 201
    assert response.json() == category_json
    response = client.get("/entry_category/1")
    assert response.status_code == 200
    assert response.json() == category_json
