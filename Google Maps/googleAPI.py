#! python 3.10
# Getting EV charger location details

# import libs:
import requests
import json
import pandas as pd
import os


# Main part
# input strings
key = 'AIzaSyDQC0YbdWlWn1Wl8kVX_xXQ2pTp-5XKglY' # Google API key
keyword = 'car-charger'
lat, lng = "-37.8182711", "144.9670618" # Flinder Street Station location
radius = "20000"

# Request URL:
url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={key}'

# Extract information:
res = requests.request('GET', url)
jsonData = res.text
data = json.loads(jsonData)

# create a json data file
with open('data.json', 'w') as f:
    f.write(res.text)

# getting data into a csv file:
df = pd.DataFrame()
df['Business Status'] = [i['business_status'] for i in data['results']]
df['location'] = [i['geometry'] for i in data['results']]
df['Lat'] = [df['location'][i]['location']['lat'] for i in range(len(df['location']))]
df['Lng'] = [df['location'][i]['location']['lng'] for i in range(len(df['location']))]
df['northeast'] = [df['location'][i]['viewport']['northeast'] for i in range(len(df['location']))]
df['View Port Lat'] = [df['northeast'][i]['lat'] for i in range(len(df['northeast']))]
df['View Port Lng'] = [df['northeast'][i]['lat'] for i in range(len(df['northeast']))]
df['Icon'] = [i['icon'] for i in data['results']]
df['Icon Background Color'] = [i['icon_background_color'] for i in data['results']]
df['Icon Mask Base Uri'] = [i['icon_mask_base_uri'] for i in data['results']]
df['Charger Name'] = [i['name'] for i in data['results']]
df['Rating'] = [i['rating'] for i in data['results']]
df['Reference'] = [i['reference'] for i in data['results']]
df['Scope'] = [i['scope'] for i in data['results']]
df['Types'] = [i['types'] for i in data['results']]
df['User Rating Total'] = [i['user_ratings_total'] for i in data['results']]
df['Vicinity'] = [i['vicinity'] for i in data['results']]
df['plus_code'] = [i['plus_code'] for i in data['results']]
df['Compound Code'] = [df['plus_code'][i]['compound_code'] for i in range(len(df['plus_code']))]
df['Global Code'] = [df['plus_code'][i]['global_code'] for i in range(len(df['plus_code']))]

# delete unneccessary columns
df.drop(['location', 'northeast', 'plus_code'], axis = 1, inplace = True)

# print out the file:
path = '/Users/giangnguyen/Desktop'
df.to_csv(os.path.join(path, 'data.csv'))