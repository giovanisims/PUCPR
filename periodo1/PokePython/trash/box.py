global box_pokemon
box_pokemon = []

def main():
    store_poke = input("Deseja guardar um pokemon? (Sim/Não): ").lower()
    if store_poke == "sim":
        store()
    elif store_poke == "não":
        print("Ok, até a próxima!")
    else:
        print("Opção inválida!")
        main()

def store():
    while True:
        pokemon = input("Digite o nome do pokemon: ")
        box_pokemon.append(pokemon)
        print(f"{pokemon} foi guardado com sucesso!")
        store_poke = input("Deseja guardar mais um pokemon? (Sim/Exit) ").lower()
        if store_poke == "exit":
            print(f"Ok, até a próxima!\nVocê guardou:\n{'\n'.join(box_pokemon)}")
            break

main()