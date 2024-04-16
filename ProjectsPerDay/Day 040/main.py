''' Flight Deals '''
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

import os
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

os.system('cls')

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# print("Welcome to Laura's Flight Club.\n \
# We find the best flight deals and email them to you.")

# first_name = input("What is your first name? -> ").title()
# last_name = input("What is your last name? -> ").title()
# email1 = input("What is your email? -> ").lower()
# email2 = input("Please verify your email -> ").lower()

# while email1 != email2:
#     print("Sorry the emails doesn't match\nPlease write it again or type quit to exit")
#     email1 = input("What is your email? -> ")
#     if email1.lower() == "quit":
#         exit()
#     email2 = input("Please verify your email -> ")
#     if email2.lower() == "quit":
#         exit()

# data_manager.create_customer(first_name, last_name, email1)
# print("Welcome!. You're in the club!")

sheet_data = data_manager.get_destination_data()
print(sheet_data)
ORIGIN_CITY_IATA = "BOG"

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)

for i, destination in enumerate(sheet_data):
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if (flight is not None) and (flight.price < destination["lowestPrice"]):
        sheet_data[i]["lowestPrice"] = flight.price
        data_manager.update_lowest_price()
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\n Flight has {flight.stop_overs} stop over, via {flight.via_city}."
        notification_manager.send_sms(message)
