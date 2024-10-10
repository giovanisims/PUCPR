def union(x,y):
    return f"O resultado na união é {x.union(y)}"

def intersection(x,y):
    return f"O resultado da interseção é {x.intersection(y)}"

def difference(x,y):
    return f"O resultado da diferença {x.difference(y)}"

def cartesian_product(x,y):
    return f"O produto cartesiano é {{(a,b) for a in x for b in y}}"

def subset(x, y):
    while True:
        print('''1 - Subconjunto
2 - Subconjunto próprio''')
        choice = input("Digite a opção desejada: ")
        match(choice):
            case "1":
                if x.issubset(y):
                    return f"{x} é subconjunto de {y}"
                else:
                    return f"{x} não é subconjunto de {y}"
            case "2":
                if x.issubset(y) and x != y:
                    return f"{x} é subconjunto próprio de {y}"
                else:
                    return f"{x} não é subconjunto próprio de {y}"

def get_set():
    while True:
        set1 = input("Digite o valores do primeiro conjunto separados por espaço: ")
        set2 = input("Digite o valores do segundo conjunto separados por espaço: ")
        set1 = set(map(int, set1.split()))
        set2 = set(map(int, set2.split()))
        return set1, set2
    

def main():
    set1, set2 = get_set()
    while True:
        print('''1 - União  
2 - Interseção  
3 - Diferença  
4 - Subconjunto (y em relação a x)
5 - Subconjunto (x em relação a y)
6 - Sair  
7 - Alterar Conjuntos''')
        choice = input("Digite a opção desejada: ")
        match choice:
            case "1":
                print(union(set1, set2))
            case "2":
                print(intersection(set1, set2))
            case "3":
                print(difference(set1, set2))
            case "4":
                print(subset(set2, set1))
            case "5":
                print(subset(set1, set2))
            case "6":
                break  
            case "7":
                set1, set2 = get_set()
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()