from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
from app.models.Meal import Meal, FILE_NAME


app = FastAPI()
    
    
    

@app.get("/")
def root():
    return {"message": "FastAPI virker"}


@app.get("/meals")
def get_meals():
    if not os.path.exists(FILE_NAME):
        return []
    
    df = pd.read_csv(FILE_NAME)
    
    return df.to_dict(orient="records")


@app.post("/meals")
def add_meal(meal: Meal):
    
    df_new = pd.DataFrame([meal.dict()])
    
    if os.path.exists(FILE_NAME):
        df_new.to_csv(FILE_NAME, mode="a", header=False, index=False)
    else:
        df_new.to_csv(FILE_NAME, index=False)
        
    return {"message": "Meal saved"}


# ---------- UPDATE ----------
@app.put("/meals/{meal_index}")
def update_meal(meal_index: int, updated_meal: Meal):

    if not os.path.exists(FILE_NAME):
        return {"error": "File not found"}

    df = pd.read_csv(FILE_NAME)

    if meal_index not in df.index:
        return {"error": "Meal not found"}

    df.loc[meal_index] = updated_meal.dict()

    df.to_csv(FILE_NAME, index=False)

    return {"message": "Meal updated"}


# ---------- DELETE ----------
@app.delete("/meals/{meal_index}")
def delete_meal(meal_index: int):

    if not os.path.exists(FILE_NAME):
        return {"error": "File not found"}

    df = pd.read_csv(FILE_NAME)

    if meal_index not in df.index:
        return {"error": "Meal not found"}

    df = df.drop(meal_index)
    
    df = df.reset_index(drop=True)

    df.to_csv(FILE_NAME, index=False)

    return {"message": "Meal deleted"}