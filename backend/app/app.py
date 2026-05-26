from fastapi import FastAPI
import pandas as pd
import os
from app.models.Meal import Meal, FILE_NAME

app = FastAPI()


def load_meals_dataframe():
    if not os.path.exists(FILE_NAME):
        return None

    return pd.read_csv(FILE_NAME)


# Root
@app.get("/")
def root():
    return {"message": "FastAPI virker"}


# Get
@app.get("/meals")
def get_meals():
    df = load_meals_dataframe()

    if df is None:
        return []

    return df.to_dict(orient="records")


# Post
@app.post("/meals")
def add_meal(meal: Meal):

    df_new = pd.DataFrame([meal.dict()])

    if os.path.exists(FILE_NAME):
        df_new.to_csv(FILE_NAME, mode="a", header=False, index=False)
    else:
        df_new.to_csv(FILE_NAME, index=False)

    return {"message": "Meal saved"}


# Update
@app.put("/meals/{meal_index}")
def update_meal(meal_index: int, updated_meal: Meal):

    df = load_meals_dataframe()

    if df is None:
        return {"error": "File not found"}

    if meal_index not in df.index:
        return {"error": "Meal not found"}

    df.loc[meal_index] = updated_meal.dict()

    df.to_csv(FILE_NAME, index=False)

    return {"message": "Meal updated"}


# Delete
@app.delete("/meals/{meal_index}")
def delete_meal(meal_index: int):

    df = load_meals_dataframe()

    if df is None:
        return {"error": "File not found"}

    if meal_index not in df.index:
        return {"error": "Meal not found"}

    df = df.drop(meal_index)

    df = df.reset_index(drop=True)

    df.to_csv(FILE_NAME, index=False)

    return {"message": "Meal deleted"}
