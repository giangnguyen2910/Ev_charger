# Getting EV charger location details

# import libs:
import requests
import json
import pandas as pd
import numpy as np


# Main part
# input strings
key = 'AIzaSyDQC0YbdWlWn1Wl8kVX_xXQ2pTp-5XKglY' # Google API key
keyword = 'car-charger'
lat, lng = "-37.8182711", "144.9670618" # Flinder Street Station location
radius = "20000"

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={key}'

res = requests.request('GET', url)
jsonData = res.text
data = json.loads(jsonData)
print(data)
