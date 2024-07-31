def main():
    nota = input("Digite a nota do aluno: ")
    check(nota)

def check(n):
    try:
        float(n)
    except ValueError:
        print("Nota inválida")
        main()
    else:
        if float(n) < 0 or float(n) > 10:
            print("Nota inválida")
            main()
        else:
            print("Nota válida")

main()