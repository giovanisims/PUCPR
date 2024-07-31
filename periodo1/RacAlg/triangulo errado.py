# Dados três valores A, B, C, verificar se eles podem ser os
# comprimentos dos lados de um triângulo e, se forem, verificar se
# compõem um triângulo equilátero, isósceles ou escaleno. Indicar
# também se estes valores não formam um triângulo.

def main():
    # valid side A
    sideA = -1
    while sideA <= 0:
        sideA = float(input("Qual é o primeiro valor: "))
    # valid side B
    sideB = -1
    while sideB <= 0:    
        sideB = float(input("Qual é o segundo valor: "))
    # valid side C
    sideC = -1
    while sideC <= 0:
        sideC = float(input("Qual é o terceiro valor: "))

    triangle(sideA, sideB, sideC)

def triangle(sideA, sideB, sideC):
    #Find out the type of triangle
    if sideA + sideB + sideC == sideA * 3:
        print("Esse triângulo é equilatero")
    elif sideA == sideC:
        print("Esse triângulo é isóceles")
    elif sideA == sideB:
        print("Esse triângulo é isóceles")
    elif sideB == sideC:
        print("Esse triângulo é isóceles")
    else:
        print("Esse triangulo é escaleno")


main()



    
