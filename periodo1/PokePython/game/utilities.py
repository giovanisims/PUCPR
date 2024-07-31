import random
import sys
from party import Party

def selection_menu():
    while True:
        return input(f"[1] - Fight\n[2] - Bag\n[3] - Pokemon\n[4] - Run\n[5] - Quit\n\n")


def player_menu(pp,pn):
    while True:
        print(f"Selected pokémon: {pp.pokemon_objects[0].name}".title())
        match selection_menu():
            case "1":
                move_menu(pn.pokemon_objects[0],pp.pokemon_objects[0])
            case "2":
                bag_menu()
            case "3":
                pokemon_menu(pp, pn)
            case "4":
                if escape(pn.pokemon_objects, pp.pokemon_objects):
                    break
            case "5":
                sys.exit("Goodbye! ")


def move_menu(pnpo, pppo):
    while True:
        move_select = input(f"[1] - {pppo.moves_active_objects[0].name}\n[2] - {pppo.moves_active_objects[1].name}\n[3] - {pppo.moves_active_objects[2].name}\n[4] - {pppo.moves_active_objects[3].name}\n[5] - Back\n".title())
        if move_select in ["1", "2", "3", "4"]:
            move = pppo.moves_active_objects[int(move_select) - 1]
            if move.power_points != 0:
                if move.power != None:
                    if move.type == "psychic":
                        f =((((2 * 1 / 5 + 2) * pppo.attack * move.power / pnpo.defense) / 50) + 2) * 1.5 * random.randint(85,100) / 100
                    else:
                        f =((((2 * 1 / 5 + 2) * pppo.attack * move.power / pnpo.defense) / 50) + 2) * random.randint(85,100) / 100
                    print(f"{pppo.name} used {move.name} and dealt {move.power} damage!".tile())
                    pnpo.health -= f
                    print(f"{pnpo.name} has {pnpo.health} health points left!")
                    break
            move.power_points -= 1
        elif move_select == "5":
            break

def npc_moves(pppo, pnpo):
    move = random.choice(pnpo.moves_active_objects)
    if move.power_points != 0:
        if move.type == "psychic":
            f =((((2 * 1 / 5 + 2) * pnpo.attack * move.power / pppo.defense) / 50) + 2) * 1.5 * random.randint(85,100) / 100
        else:
            f =((((2 * 1 / 5 + 2) * pnpo.attack * move.power / pppo.defense) / 50) + 2) * random.randint(85,100) / 100
        print(f"{pnpo.name} used {move.name} and dealt {move.power} damage!".title())
        pppo.health -= f
        print(f"{pppo.name} has {pppo.health} health points left!")
    else:
        print(f"{pnpo.name} used Struggle! ## I have no clue what this even does")
    move.power_points -= 1

def bag_menu():
    ...

def pokemon_menu(pp,pn):
    while True:
        for pokemon in pp.pokemon_objects:
            print(f"[{pp.pokemon_objects.index(pokemon) + 1}] - {pokemon.name}".title())
        print("[7] - Back", end="\n\n")
        selected_poke = input("Select a Pokémon: ")
        if selected_poke in ["1", "2", "3", "4", "5", "6"]:
            if pp.pokemon_objects[int(selected_poke) - 1].health <= 0:
                print("This Pokémon has fainted!")
            else:
                pp.pokemon_objects.insert(0, pp.pokemon_objects.pop(int(selected_poke) - 1))
                break
        elif selected_poke == "7":
            player_menu(pp, pn)


def escape(pnpo, pppo):
    c = 1
    print(f"Your {pppo[0].name} is trying to get away from the wild {pnpo[0].name}!")
    f = (((pppo[0].speed * 128)/pnpo[0].speed) + 30 * c) % 256
    if f > 255:
        print("You got away safely!")
        return True
    if random.randint(0, 255) < f:
        print("You got away safely!")
        return True
    else:
        print("You couldn't get away!")
        c += 1