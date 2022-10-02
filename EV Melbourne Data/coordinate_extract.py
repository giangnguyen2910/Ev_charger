import pandas as pd
import re

# read the data from the dataset
data = pd.read_csv('parks_burwood_GoogleAPI.csv')

# get the first row link
link = data['Link'][0]

locationRegex = re.compile(r'.+8m2!3d(-?\d+.?\d*)!4d(-?\d+.?\d*)')

# Get the longitude and latitude of the charger location:
long = []
lat = []
for i in data['Link'][:]: # eliminate the empty rows
    long.append(locationRegex.search(i).group(1))
    lat.append(locationRegex.search(i).group(2))

# add the coordinates into the dataframe
data['long'] = long
data['lat'] = lat

# print out the dataframe
data.to_csv('parks_burwood.csv')