''' Flight Search Class '''

from math import ceil
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "4gFSRJFbL_FFOT2dnZrWD1AuBruFHYyg"
headers = {'apikey': TEQUILA_API_KEY}


class FlightSearch:
    ''' Flight Search Class '''
    def get_destination_code(self, city_name):
        ''' Get destination code '''        
        params = {'term': city_name,
                  'location_types': 'city'}
        response = requests.get(url= f"{TEQUILA_ENDPOINT}/locations/query",
                                params=params,
                                headers=headers,
                                timeout=10)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        ''' Check flights '''
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "COP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=headers,
                                params=query,
                                timeout=10)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {ceil(flight_data.price)} COP")
        return flight_data
