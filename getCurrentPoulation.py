import json
import urllib3
import pandas as pd

API_KEY = '872399484d9afeef08537ab0acae3e0278d81356'
# 15 estados mais populasos dos EUA
Locations = {
    'California': '06',
    'Florida': '12',
    'Georgia': '13',
    'Illinois': '17',
    'Indiana': '18',
    'Massachusetts': '25',
    'Michigan': '26',
    'NewJersey': '34',
    'NewYork': '36',
    'NorthCarolina': '37',
    'Ohio': '39',
    'Pennsylvania': '42',
    'Texas': '48',
    'Virginia': '51',
    'Washington': '53',
}

Codigos = ",".join(Locations.values())
API_LINK = f"https://api.census.gov/data/2018/pep/population?get=POP,GEONAME&for=state:{Codigos}&key={API_KEY}"

response = urllib3.PoolManager().request("GET", API_LINK)
response = pd.DataFrame(json.loads(response.data)).to_csv(r'population.csv', index = None, header = False, sep=';', encoding='utf-8')