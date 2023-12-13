''' Habit Tracking '''
import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "lauramendoza"
TOKEN = "asdu453asdbla45sdsidfu5"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params, timeout=10)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers, timeout=10)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

DATE = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": DATE,
    "quantity": input("How many kilometers did you cycle today? ")
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT,
#                          json=pixel_config,
#                          headers=headers,
#                          timeout=10)
# print(response.text)

PIXEL_MODIFICATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_update = {
    "quantity": "0.1"
}

# response = requests.post(url=PIXEL_MODIFICATION_ENDPOINT,
#                          json=pixel_update,
#                          headers=headers,
#                          timeout=100)
# print(response.text)

PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.post(url=PIXEL_DELETE_ENDPOINT,
#                          headers=headers,
#                          timeout=100)
# print(response.text)
