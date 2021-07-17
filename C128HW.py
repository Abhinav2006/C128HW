import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
urlstart = requests.get(url)
soup = bs(urlstart.text, 'html.parser')
table = soup.find('table')
tr = table.find_all('tr')

data = []

for tr in tr:
    td = tr.find_all('td')
    row = [i.text.strip()for i in td]
    data.append(row)

newData = []

headers = ["Star", "Distance", "Mass", "Radius"]
star = []
distance = []
mass = []
radius = []

for l in range(1, len(data)):
    star.append(data[i][0])
    distance.append(data[i][5])
    mass.append(data[i][8])
    radius.append(data[i][9])

df = pd.DataFrame(list(zip(star, distance, mass, radius)), columns = ['Star', 'Distance', 'Mass', 'Radius'])
df.to_csv('C128HWData.csv')