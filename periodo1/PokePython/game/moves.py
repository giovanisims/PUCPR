import requests
import time
import random

class Moves:
    class NoPowerError(Exception):
        pass

    def __init__(self, move) -> None:
        self.get_move_info(self.get_move_API(move))

    def get_move_API(self, move):
        for _ in range(5):
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/move/{move}", timeout=5)
                return response
            except requests.exceptions.Timeout:
                print("Timeout occurred. Retrying...")
                time.sleep(1)


    def get_move_info(self, response):
        self.response_json = response.json()
        self.name = self.response_json["name"]
        self.power_points = self.response_json["pp"]
        self.power = self.response_json["power"]
        self.type = self.response_json["type"]["name"]

        if self.power is None:
            raise self.NoPowerError(f"The move {self.name} has no power.")


    def __str__(self) -> str:
        return f"Name: {self.name}\nPower: {self.power}\nPower Points: {self.power_points}\nDamage Class: {self.type}"

