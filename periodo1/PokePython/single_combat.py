def main():
    p1_name,p1_health,p1_attack =  create_pokemon()
    p2_name,p2_health,p2_attack =  create_pokemon()
    pokemon_fight(p1_name,p1_health,p1_attack,p2_name,p2_health,p2_attack)

def create_pokemon():
    name = input("Enter the name of your Pokemon: ")
    health = int(input("Enter the health of your Pokemon: "))
    attack = int(input("Enter the attack of your Pokemon: "))
    return name,health,attack

def pokemon_fight(name_1,health_1,attack_1,name_2,health_2,attack_2):
    while health_1 > 0 and health_2 > 0:
        if input("Player 1, do you wnat to attack? Y/N").lower() == "y":
            health_2 -= attack_1
            print(f"{name_1} attacked {name_2} for {attack_1} damage")
            print(f"{name_2} has {health_2} health left")
        elif input("Player 2, do you wnat to attack? Y/N").lower() == "y":
            health_1 -= attack_2
            print(f"{name_2} attacked {name_1} for {attack_2} damage")
            print(f"{name_1} has {health_1} health left")
    if health_1 > health_2:
        print(f"{name_1} wins!")
    else:
        print(f"{name_2} wins!")

main()


