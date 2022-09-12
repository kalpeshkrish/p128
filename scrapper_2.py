from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
)
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][1])
    mass.append(temp_list[i][2])
    radius.append(temp_list[i][7])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"]
)
df.to_csv("dwarf-stars.csv")