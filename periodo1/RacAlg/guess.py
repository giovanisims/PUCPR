def main():
    question = get_question()
    guess = get_guess()
    check_guess(guess, question)

def get_question():
    try:
        question = int(input("Digite um numero entre 1 e 100: "))
        if question < 1 or question > 100:
            print("Por favor, digite apenas números entre 1 e 100")
            get_question()
        else:
            return question
    except ValueError:
        print("Digite um número inteiro")
        get_question()

def get_guess():
    try:
        guess = int(input("Qual é o seu chute? "))
        if guess < 1 or guess > 100:
            print("O número é entre 1 e 100")
            get_guess()
        else:
            return guess
    except ValueError:
        print("Digite um número inteiro")
        get_guess()

def check_guess(g, q):
    while g != q:
        if g < q:
            print("Chute um número maior")
            g = get_guess()
        elif g > q:
            print("Chute um número menor")
            g = get_guess()
    print("Você acertou!")

main()