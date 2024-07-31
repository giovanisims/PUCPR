import sys
from party import Party
import utilities


def main():
    party_player = Party()
    while True:
        while True:
            start = input("Would you like to look for pokémon? ").lower()
            if start in ["yes", "y", "s", "sim"]:
                party_npc = Party()
                print(f"You found a wild: {party_npc.pokemon_objects[0].name}!".title())
                break
            elif start in ["no", "n", "nao", "não"]:
                sys.exit("Goodbye!")
        if party_player.pokemon_objects[0].speed >= party_npc.pokemon_objects[0].speed:
            utilities.player_menu(party_player,party_npc)
        while all(pokemon.health > 0 for pokemon in party_player.pokemon_objects) and party_npc.pokemon_objects[0].health > 0:
            utilities.npc_moves(party_player.pokemon_objects[0], party_npc.pokemon_objects[0])



if __name__ == "__main__":
    main()