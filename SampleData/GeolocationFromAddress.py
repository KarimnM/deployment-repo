import requests
import urllib.parse
import os
import sys

def address_to_lat_lon(address: str) -> tuple:
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if not bool(response):
        return None,None
    else:
        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])
        return lat, lon


if __name__ == '__main__':
    if len(sys.argv) == 1:
        test_address = '1232 John apple st, Henrico, VA'
    else:
        test_address = sys.argv[1]

    latitude, longitude = address_to_lat_lon(test_address)
    print("Address =", test_address)
    print(latitude, longitude)






