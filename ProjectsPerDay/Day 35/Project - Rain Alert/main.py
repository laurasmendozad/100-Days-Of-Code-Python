''' Rain Alert '''
import os
import requests
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
APIKEY = "7a390898072ea23ff63debb98be9ec09"

param1 = {
    "q": "Porto Velho, Rondônia, +55",# "Piedecuesta, Santander, +57",
    "limit": 5,
    "appid": APIKEY
}

r1 = requests.get(url='http://api.openweathermap.org/geo/1.0/direct',
                  params=param1,
                  timeout=10)
param2 = {
    "lat": r1.json()[0]["lat"],
    "lon": r1.json()[0]["lon"],
    "appid": APIKEY
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

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella ☂️",
                        from_='+13858326743',
                        to='+573178923835'
                    )

    print(message.status)
