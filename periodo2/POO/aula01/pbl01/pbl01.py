# Crie um programa em Python que implementa uma função que retorna uma lista preenchida com valores inteiros aleatórios. 
# A função deve receber como parâmetro o tamanho da lista. O tamanho deve ser informado pelo usuário via input.

# Para cada número da lista, imprima:

# Se o número é múltiplo de 3
# Se o número é par
# Se o número é ímpar

import random

def main():
    check_list(get_list())

def get_list():
    size = int(input('Size of the list: '))
    list = [random.randint(0, 100) for _ in range(size)]
    return list

def check_list(list):
    for number in sorted(list):
        if number % 2 == 0:
            kind = 'even'
        else:
            kind = 'odd'
        if number % 3 == 0:
            multiple = 'and, is a multiple of 3'
        else:
            multiple = ''
        print(f'{number} is {kind} {multiple}')

if __name__ == '__main__':
    main()
