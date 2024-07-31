def basic_while_test():
    _ = 1
    while _ != 0:
        _ = int(input("Digite 0 para parar: "))

# basic_while_test()

def postive_only():
    i = -1
    _ = 0
    while _ <= 10:
        if i < 0:
            i = int(input("Digite um número positivo: "))
        else:
            print(i)
            i = -1
            _ += 1

# postive_only()

def factorial():
    n = int(input("Digite um número inteiro: "))
    f = 1
    while n > 1:
        f *= n
        n -= 1
    print(f)

# factorial()

def highest():
    list = []
    for _ in range(5):
        num = int(input("Digite um número: "))
        list.append(num)
    list.sort()
    print(list[len(list) - 1])

# highest()