import os

os.environ["TESTING"] = "true"

from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_delete_meal():
    new_meal = {
        "Date" : "2026-05-25",
        "Meal" : "Dinner",
        "Food" : "Pasta",
        "Gram" : 200,
        "Calories" : 300
    }

    client.post(
        "/meals",
        json=new_meal
    )

    response = client.delete("/meals/0")

    assert response.status_code == 200
    assert response.json() == {
        "message":"Meal deleted"
    }