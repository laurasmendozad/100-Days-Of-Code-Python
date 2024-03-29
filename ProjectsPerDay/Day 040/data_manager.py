''' Data Manager Class '''

import os
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/dce51f414bc3809c0c41899550c70ce5/flightDeals/prices"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

class DataManager:
    ''' Data Manager Class '''
    def __init__(self):
        self.destination_data = {}
        self.sheety_headers = {"Authorization":f"Bearer {SHEETY_TOKEN}"}

    def get_destination_data(self):
        '''Use the Sheety API to GET all the data in that sheet and print it out.'''
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,
                                headers=self.sheety_headers,
                                timeout=10)
        print(response.json())
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        '''Update the Sheety'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                         headers=self.sheety_headers,
                         json=new_data,
                         timeout=10)

    def update_lowest_price(self):
        '''Update the Sheety'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                         headers=self.sheety_headers,
                         json=new_data,
                         timeout=10)
