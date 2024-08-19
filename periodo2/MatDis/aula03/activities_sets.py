def get_set_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return set(map(int, user_input.split()))
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros separados por espaços.")

def display_menu():
    print("\nMenu de Operações entre Conjuntos:")
    print("a) União")
    print("b) Intersecção")
    print("c) Diferença")
    print("d) Produto cartesiano")
    print("e) Verificação se A é subconjunto de B")
    print("f) Verificação se B é subconjunto de A")
    print("g) Sair")

def main():
    A = get_set_input("Digite os elementos do conjunto A (separados por espaço): ")
    B = get_set_input("Digite os elementos do conjunto B (separados por espaço): ")

    while True:
        display_menu()
        choice = input("Escolha uma opção: ").strip().lower()

        if choice == 'a':
            print(f"União: {A.union(B)}")
        elif choice == 'b':
            print(f"Intersecção: {A.intersection(B)}")
        elif choice == 'c':
            print(f"Diferença (A - B): {A.difference(B)}")
        elif choice == 'd':
            cartesian_product = {(a, b) for a in A for b in B}
            print(f"Produto cartesiano: {cartesian_product}")
        elif choice == 'e':
            sub_choice = input("Verificar se A é subconjunto de B (1) ou subconjunto próprio de B (2): ").strip()
            if sub_choice == '1':
                print(f"A é subconjunto de B: {A.issubset(B)}")
            elif sub_choice == '2':
                print(f"A é subconjunto próprio de B: {A < B}")
            else:
                print("Opção inválida.")
        elif choice == 'f':
            sub_choice = input("Verificar se B é subconjunto de A (1) ou subconjunto próprio de A (2): ").strip()
            if sub_choice == '1':
                print(f"B é subconjunto de A: {B.issubset(A)}")
            elif sub_choice == '2':
                print(f"B é subconjunto próprio de A: {B < A}")
            else:
                print("Opção inválida.")
        elif choice == 'g':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()