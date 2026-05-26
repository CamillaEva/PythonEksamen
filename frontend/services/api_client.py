import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY= os.getenv("USDA_API_KEY")
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
ENERGY_NUTRIENT_NAME = "Energy"


def get_calories(food, grams):
  
    params = {
        "query":food,
        "api_key": API_KEY
    }

    response = requests.get(USDA_API_URL, params = params)

    if response.status_code != 200:
        return 0

    data = response.json()

    foods = data.get("foods", [])

    if not foods:
        return 0
    
    first_food = foods[0]
    nutrients = first_food.get("foodNutrients", [])

    for nutrient in nutrients:
        if nutrient.get("nutrientName") == ENERGY_NUTRIENT_NAME:
            calories_per_100g = nutrient.get ("value", 0)
            total_calories = (float(grams) / 100) * calories_per_100g
            return round(total_calories)
        
    return 0


