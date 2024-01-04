''' Send Motivational Quote on Mondays '''
import os
import smtplib
from random import choice
import datetime as dt

def send_email(subject, message):
    ''' Send the email '''
    email = "laurasofi0507@gmail.com"
    password = os.environ.get("APP_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="laurasofi0507@hotmail.com",
            msg=f"Subject:{subject}\n\n{message}"
        )


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open(r"Day 032\quotes.txt", encoding="utf-8") as quotes_file:
        quotes = quotes_file.readlines()

    send_email("Monday Motivation", choice(quotes))
