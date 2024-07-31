def main():
    get_name()
    get_starter()

def get_starter():
    chosen = input(f'''Now {player_name} which Pokémon do you want?\n\nDo you want, Charmander(fire), Squirtle(water), Grass(Bulbasaur)? ''').strip().lower()

    while chosen not in ["charmander","fire","charmander(fire)","squirtle","water","squirtle(water)",
                        "bulbasaur","grass","bulbasaur(grass)"]:
        print("Hey! Don't go away yet!")
        chosen = input("So do you want, Charmander(fire), Squirtle(water), Grass(Bulbasaur)? ").strip().lower()

    if chosen in ["charmander","fire","charmander(fire)"]:
        print("You chose Charmander; This Pokémon is really energetic!")
    elif chosen in ["squirtle","water","squirtle(water)"]:
        print("You chose Squirtle; This Pokémon is really energetic!")
    elif chosen in ["bulbasaur","grass","bulbasaur(grass)"]:
        print("You chose Bulbasaur; This Pokémon is really energetic!")

def get_name():

    global player_name
    player_name = input('''Hello there! Welcome to the world of Pokémon! My name is Oak! People call me the Pokémon Prof! 
    This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. 
    Other use them for fights. Myself… I study Pokémon as a profession.\n\nWhat is your name? ''').strip().lower().title()


main()