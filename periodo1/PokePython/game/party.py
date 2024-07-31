import requests
import time
import random
from pokemon import Pokemon

class Party:
    def __init__(self) -> None:
        self.get_party_info(self.get_party_API())
        self.pokemon_objects = [Pokemon(name) for name in self.party]

    def get_party_API(self):
        for _ in range(5):
            try:
                response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1302", timeout=5)
                return response
            except requests.exceptions.Timeout:
                print("Timeout occurred. Retrying...")
                time.sleep(1)


    def get_party_info(self, response):
        self.response_json = response.json()
        self.party_all = [pokemon["name"] for pokemon in self.response_json["results"]]
        self.party = random.sample(self.party_all, 6)


    def __str__(self) -> str:
        return f"Party: {self.party}"
