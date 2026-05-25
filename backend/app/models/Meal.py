from pydantic import BaseModel
import os

TESTING = os.getenv("TESTING") == "true"

if TESTING:
    FILE_NAME = "test_foodlog.csv"
else:
    FILE_NAME = "foodlog.csv"

class Meal(BaseModel):
    Date: str
    Meal: str
    Food: str
    Gram: int
    Calories: float
    
    


    