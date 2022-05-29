# Finding the EV charger locations in AU:
import os
from pathlib import Path
import requests
import bs4


# imput:
url = 'https://www.plugshare.com/'
res = requests.get(url)

# write to a bs4 object:
soup = bs4.BeautifulSoup(res.text, 'html.parser')

with open('PlugShare.html', 'w') as file:
    file.write(str(soup))