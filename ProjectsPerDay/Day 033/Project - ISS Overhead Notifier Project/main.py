''' ISS Overhead Notifier Project '''
import os
from datetime import datetime
import smtplib
import time
import requests


MY_LAT = -52.3909 # Your latitude
MY_LONG = -175.7142 # Your longitude

def is_iss_overhead():
    ''' Function to define if iss is overhead '''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    # print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    # print(iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    ''' Function to define if is night '''
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = sunrise

    if time_now >= sunset or time_now <= sunrise:
        return True

def send_email(subject, message):
    ''' Send the email '''
    email = "laurasofi0507@gmail.com"
    password = os.environ.get("APP_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{message}"
            )
while True:
    if is_iss_overhead() and is_night():
        send_email("Look Up", "The ISS is above you in the sky.")
        time.sleep(60)
