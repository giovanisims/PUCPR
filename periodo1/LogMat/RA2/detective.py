import random

clues = [
    "Se Sarah estava no Havana, então ela não estava no bloco azul. (A → ¬B)",
    "Livia estava na natação na terça-feira entre as 15h e 17h. (C → D)",
    "Giovani chega à PUC às 17h e se encontra com Sarah. (E ^ F)",
    "Lucas chega à PUC às 18h. (G)",
    "Na quarta-feira, Giovani, Lucas e Livia chegam às 16:30 para a monitoria. (H → I ^ J ^ K)",
    "O grupo se encontra no bloco azul ou na biblioteca antes das aulas. (L → M v N)",
    "O professor Mateus foi visto pela última vez às 17:45 no corredor do bloco azul. (O)",
    "Se Livia está na aula após 18:15, então ela não pode estar no bloco azul. (P → ¬Q)",
]
clue_count = 0


def main():
    global clue_count
    # Prints the introductory paragraph
    print(
        "Na universidade PUC, um crime misterioso aconteceu no bloco azul. O professor Mateus foi encontrado sem vida, assassinado na terça-feira por volta das 18:00. Todos os integrantes do grupo são suspeitos. Cabe a você, o detetive, juntar as pistas, fazer deduções e descobrir quem é o culpado e o que realmente aconteceu.\nResponda:\n 1 - Quem matou o professor Mateus?\n 2 - Onde estava cada integrante no momento do crime? (Opcional)\n"
    )
    # Prompts the user if the want to see a clue, and allows the GM to end the game
    for _ in range(len(clues)):
        choice = input("Clique para ver uma Pista ").lower()
        match choice:
            case "end":
                break
            case _:
                clue_count += 1
                print_clue()
    print(f"Vocês usaram {clue_count} pistas")


def print_clue():
    global clue_count
    clue = random.randint(0, len(clues) - 1)
    print(f"Pista {clue_count} - {clues[clue]}")
    clues.pop(clue)


# Deduções possíveis
# Se Sarah estava no Havana, ela não estava no bloco azul às 18h. (¬B)
# Se Livia estava na natação na terça-feira, ela chegou à PUC às 17h. (C → D)
# Giovani chega à PUC às 17h e se encontra com Sarah, então Sarah estava na PUC às 18h. (E ^ F → B)
# Se Livia está na aula após 18:15, ela não estava no bloco azul. (P → ¬Q)

# Com base nas preposições lógicas e na análise das pistas, Giovani é o assassino do professor Mateus

if __name__ == "__main__":
    main()
