from pydantic import BaseModel




FILE_NAME = "foodlog.csv"


class Meal(BaseModel):
    Date: str
    Meal: str
    Food: str
    Gram: int
    Calories: float
    
    


    