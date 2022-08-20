import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp_dict = requests.get(url).json()
smartest = ''
intelligence = 0
for element in resp_dict:
    if element['powerstats']['intelligence'] > intelligence:
        smartest = element['name']
        intelligence = element['powerstats']['intelligence']
print(f'Самый умный - {smartest}, интеллект {intelligence}')
