import requests
import json


pokemon = input("Enter the name of a pokemon: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
json_pokemon = response.json()
for ability in json_pokemon["abilities"]:
    print(ability["ability"]["name"])

# This shit sucks dont use it
# maybe use it 