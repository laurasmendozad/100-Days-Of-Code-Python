''' Workout Tracking '''

import json
from datetime import datetime
import requests

APP_ID = "101750f2"
API_KEY = "e5f398969bae76a0c568601a7919b9e7"
SHEETY_TOKEN = "KSDU234BFLASJDNA23SKDA457SL"

GENDER = "female"
WEIGHT_KG = 86
HEIGHT_CM = 170
AGE = 23

NUTRITIONIX_ENDPOINT =  "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/dce51f414bc3809c0c41899550c70ce5/workoutsTracking/workouts"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
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

sheety_headers = {"Authorization":f"Bearer {SHEETY_TOKEN}"}

print(sheety_headers)

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
