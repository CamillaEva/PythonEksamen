import os

os.environ["TESTING"] = "true"

from fastapi.testclient import TestClient
from app.app import app
import pandas as pd

client = TestClient(app)

def setup_function():
    empty_df = pd.DataFrame(columns=[
        "Date",
        "Meal",
        "Food",
        "Gram",
        "Calories"
    ])

    empty_df.to_csv("test_foodlog.csv", index=False)

def test_get_meals():
    new_meal = {
        "Date": "2026-05-25",
        "Meal" : "Breakfast",
        "Food" : "oats",
        "Gram" : 100,
        "Calories" : 250
    }
    
    client.post("/meals", 
                json=new_meal
                )
    
    response = client.get("/meals")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["Food"] == "oats"
    
    
def test_add_meal():
    new_meal = {
        "Date": "2026-05-25",
        "Meal": "Lunch",
        "Food": "Salad",
        "Gram": 150,
        "Calories": 200
    }
    
    response = client.post("/meals",
                        json=new_meal
                        )
    
    assert response.status_code == 200
    assert response.json() == {"message": "Meal saved"}


def test_update_meal():
    new_meal = {
        "Date" : "2026-05-26",
        "Meal" : "Breakfast",
        "Food" : "Yoghurt",
        "Gram" : 150,
        "Calories" : 100
    }

    client.post(
        "/meals",
        json=new_meal
    )

    updated_meal = {
        "Date" : "2026-05-26",
        "Meal" : "Breakfast",
        "Food" : "Oats",
        "Gram" : 100,
        "Calories" : 250
    }

    response = client.put(
        "/meals/0",
        json=updated_meal
    )

    assert response.status_code == 200
    assert response.json() == {
        "message" : "Meal updated"
    }

    response_get = client.get("/meals")
    data = response_get.json()

    assert data[0]["Food"] == "Oats"
    assert data[0]["Calories"] == 250


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