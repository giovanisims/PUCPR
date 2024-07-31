import random

def main():
    safari_choice = input("Você quer entrar no safari? ")
    if safari_choice == "s":
        safari()
    elif safari_choice == "n":
        print("Ok, até a próxima!")
    else:
        input("Opção inválida!")
        main()

def safari():
        grass_rock = input("Você quer procurar no mato ou na caverna? ")
        if grass_rock == "mato":
            grass_safari()
        elif grass_rock == "caverna":
            rock_safari()
        else:
            print("Opção inválida!")
            safari()

def grass_safari():
    grass_poke = ["Bulbasaur","Caterpie","Pikachu", "Pidgey", "Rattata", "Spearow", "Ekans"]
    pokemon = random.choice(grass_poke)
    catch = input(f"Você encontrou um {pokemon}!\nDeseja capturar?")
    while True:
        if catch == "s":
            print(f"Você capturou o {pokemon}!")
            break
        elif catch == "n":
            print(f"Você fugiu do {pokemon}!")
            break
        else:
            catch = input("Opção inválida! Deseja capturar?")
    catch_again_grass()

def catch_again_grass():
    again = input("Deseja procurar outro pokemon? ")
    if again == "s":
        grass_safari()
    elif again == "n":
        print("Ok, até a próxima!")
    else:
        print("Opção inválida!")
        catch_again_grass()

def rock_safari():
    rock_poke = ["Geodude","Onix","Zubat", "Machop", "Graveler", "Golem", "Rhyhorn"]
    pokemon = random.choice(rock_poke)
    catch = input(f"Você encontrou um {pokemon}!\nDeseja capturar? ")
    while True:
        if catch == "s":
            print(f"Você capturou o {pokemon}!")
            break
        elif catch == "n":
            print(f"Você fugiu do {pokemon}!")
            break
        else:
            catch = input("Opção inválida! Deseja capturar?")

def catch_again_rock():
    again = input("Deseja procurar outro pokemon? ")
    if again == "s":
        rock_safari()
    elif again == "n":
        print("Ok, até a próxima!")
    else:
        print("Opção inválida!")
        catch_again_rock()

if __name__ == "__main__":
    main()