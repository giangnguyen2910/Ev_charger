import pandas as pd
import re, os


os.chdir('/Users/giangnguyen/Documents/Deakin/Project B/Coding/Github/EV Melbourne Data/data_cleaning.py')

data = pd.read_csv('Dataset.csv')

# get the first link to take a closer look
link = data['Link'][0]
link

# Get the coordinates from the link:
locationRegex = re.compile(r'.+8m2!3d(-?\d+.?\d*)!4d(-?\d+.?\d*)')

# Get the longitude and latitude of the charger location:
long = []
lat = []
for i in data['Link'][:]: # eliminate the empty rows
    long.append(locationRegex.search(i).group(1))
    lat.append(locationRegex.search(i).group(2))

# Add the longitude and latitude to the dataframe:
data['long'] = long
data['lat'] = lat

# print out the dataframe:
data.to_csv('charger_detail.csv')