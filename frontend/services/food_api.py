import requests

BASE_URL = "http://backend:8000"

def get_meals():
    response = requests.get(f"{BASE_URL}/meals")
    return response.json()


def save_meal(data):
    response = requests.post(
        f"{BASE_URL}/meals",
        json=data
    )

    return response.json()


def update_meal(index, data):
    response = requests.put(
        f"{BASE_URL}/meals/{index}",
        json=data
    )

    return response.json()


def delete_meal(index):
    response = requests.delete(
        f"{BASE_URL}/meals/{index}"
    )

    return response.json()