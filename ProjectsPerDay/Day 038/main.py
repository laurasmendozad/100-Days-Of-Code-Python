''' Workout Tracking '''
import os
import json
from datetime import datetime
import requests

nutritionix_id = os.environ["NUTRITIONIX_API_ID"]
nutritionix_apikey = os.environ["NUTRITIONIX_API_KEY"]
sheety_token = os.environ["SHEETY_TOKEN"]

GENDER = "female"
WEIGHT_KG = 90
HEIGHT_CM = 170
AGE = 24

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/dce51f414bc3809c0c41899550c70ce5/workoutsTracking/workouts"

nutritionix_headers = {
    "x-app-id": nutritionix_id,
    "x-app-key": nutritionix_apikey
}

nutritionix_params = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutritionix_response = requests.post(NUTRITIONIX_ENDPOINT,
                         headers=nutritionix_headers,
                         json=nutritionix_params,
                         timeout=10)
nutritionix_response.raise_for_status()
# print(json.dumps(nutritionix_response.json(), indent=4))

sheety_headers = {"Authorization":f"Bearer {sheety_token}"}


for exercise in nutritionix_response.json()["exercises"]:
    sheety_params = {
        "workout":{
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(SHEETY_ENDPOINT,
                                    json=sheety_params,
                                    headers=sheety_headers,
                                    timeout=10)
    print(json.dumps(sheety_response.json(), indent=4))
