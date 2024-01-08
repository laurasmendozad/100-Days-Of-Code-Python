''' Habit Tracking '''
import os
from datetime import datetime, timedelta
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
username = os.environ["PIXELA_USERNAME"]
token = os.environ["PIXELA_TOKEN"]

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params, timeout=10)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers, timeout=10)
# print(response.text)

PIXELA_MODIFICATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs/{GRAPH_ID}"

DATE = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": DATE,
    "quantity": input("How many kilometers did you cycle today? ")
}

# response = requests.post(url=PIXELA_MODIFICATION_ENDPOINT,
#                          json=pixel_config,
#                          headers=headers,
#                          timeout=10)
# print(response.text)

# DATE = (datetime.now()-timedelta(days=12)).strftime("%Y%m%d")

pixel_update = {
    "date": DATE,
    "quantity": "15"
}

# response = requests.post(url=PIXELA_MODIFICATION_ENDPOINT,
#                          json=pixel_update,
#                          headers=headers,
#                          timeout=10)
# print(response.text)

PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.delete(url=PIXEL_DELETE_ENDPOINT,
#                          headers=headers,
#                          timeout=10)
# print(response.text)