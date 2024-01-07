''' Rain Alert '''
import os
import requests
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
apikey = os.environ['OPENWEATHERMAP_APIKEY']

param1 = {
    "q": "Seattle, Washington, +1",
    "limit": 5,
    "appid": apikey
}

r1 = requests.get(url='http://api.openweathermap.org/geo/1.0/direct',
                  params=param1,
                  timeout=10)
param2 = {
    "lat": r1.json()[0]["lat"],
    "lon": r1.json()[0]["lon"],
    "appid": apikey
}

r2 = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',
                  params=param2,
                  timeout=10)

WILL_RAIN = False

for i in range(0,3):
    condition_code = r2.json()["list"][i]["weather"][0]["id"]
    if condition_code < 700:
        WILL_RAIN = True

if WILL_RAIN:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12015146534',
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        to=os.environ['PHONE'])
    print(message.status)
