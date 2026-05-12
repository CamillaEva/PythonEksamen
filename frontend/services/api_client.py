import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY= os.getenv("USDA_API_KEY")

def get_calories(food, amount):
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"

    params = {
        "query":food,
        "api_key": API_KEY
    }

    response = requests.get(url, params = params)

    data = response.json()

    foods = data["foods"]

    if not foods:
        return 0
    
    first_food = foods[0]
    nutrients = first_food["foodNutrients"]

    for nutrient in nutrients:
        if nutrient["nutrientName"] == "Energy":
            calories_per_100g = nutrient ["value"]
            total_calories = (float(amount) / 100) * calories_per_100g
            return round(total_calories)
        
    return 0


