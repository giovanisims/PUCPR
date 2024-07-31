import random



def main():
    action_select()



def action_select():
    while True:
        action = input("What would you like to do?\n\n1 - Attack\n2 - Bag\n3 - Pokemon\n4 - Run\n")
        if action == "1":
            attack()
        elif action == "2":
            bag()
        elif action == "3":
            pokemon()
        elif action == "4":
            run()
        else:
            print("Invalid input. Please try again.")

def attack():
    pass  # TODO: Implement this function

def pokemon():
    pass  # TODO: Implement this function

def run():
    pass  # TODO: Implement this function

def bag():
    bag_action = ("What would you like to do?\n\n1 - Potion\n2 - Pokeball\n3 - Other\n")
    if bag_action == "1":
        potion()
    elif bag_action == "2":
        pokeball()
    elif bag_action == "3":
        other()

def pokeball():
    pass  # TODO: Implement this function

def other():
    pass  # TODO: Implement this function

def potion():
    while True:
        potion_choice = input("What potion would you like to use?\n\n1 - Potion\n2 - Super Potion\n3 - Hyper Potion\n4 - Max Potion\n")
        if potion_choice == "1":
            print("You used a potion!")
            current_poke_health = current_poke_health + 20
        elif potion_choice == "2":
            print("You used a super potion!")
            current_poke_health = current_poke_health + 40
        elif potion_choice == "3":
            print("You used a hyper potion!")
            current_poke_health = current_poke_health + 80
        elif potion_choice == "4":
            print("You used a max potion!")
            current_poke_health = current_poke_health + 160
        else:
            print("That is not a valid potion. Please try again.")







if __name__ == "__main__":
    main()
