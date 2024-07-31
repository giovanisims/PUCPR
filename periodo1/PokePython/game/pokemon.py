import requests
import time
import random
from moves import Moves


class Pokemon:
    def __init__(self, name) -> None:
        self.get_pokemon_info(self.get_pokemon_API(name))
        self.moves_active_objects = self.get_active_moves_with_power()

    def get_pokemon_API(self, name):
        for _ in range(5):
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=5)
                return response
            except requests.exceptions.Timeout:
                print("Timeout occurred. Retrying...")
                time.sleep(1)


    def get_pokemon_info(self, response):
        self.response_json = response.json()
        self.name = self.response_json["name"]
        self.types = self.response_json["types"][0]["type"]["name"]
        self.moves_all = [move["move"]["name"] for move in self.response_json["moves"]]
        self.abilities = [ability["ability"]["name"] for ability in self.response_json["abilities"]]

        for stat in self.response_json["stats"]:
            stat_name = stat["stat"]["name"]
            if stat_name == "hp":
                self.health = stat["base_stat"]
            elif stat_name == "attack":
                self.attack = stat["base_stat"]
            elif stat_name == "defense":
                self.defense = stat["base_stat"]
            elif stat_name == "special-attack":
                self.special_attack = stat["base_stat"]
            elif stat_name == "special-defense":
                self.special_defense = stat["base_stat"]
            elif stat_name == "speed":
                self.speed = stat["base_stat"]

    def get_active_moves_with_power(self):
        moves_with_power = []
        remaining_moves = self.moves_all.copy()
        while remaining_moves and len(moves_with_power) < min(4, len(self.moves_all)):
            move = random.choice(remaining_moves)
            remaining_moves.remove(move)
            try:
                move_object = Moves(move)
                moves_with_power.append(move_object)
            except Moves.NoPowerError:
                print(f"Excluding move {move} because it has no power.")
        return moves_with_power

    def __str__(self) -> str:
        return f"Name: {self.name}\nTypes: {self.types}\nMoves: {self.moves_active}\nAbilities: {self.abilities}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nSpecial Attack: {self.special_attack}\nSpecial Defense: {self.special_defense}\nSpeed: {self.speed}"
