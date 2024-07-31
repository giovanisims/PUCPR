## Inicialização direta

# # matriz 3 x 3
# matrizInicDireta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for linha in range(0, 3):
#     print("Linha", linha)
# for coluna in range(0, 3):
#     print(matrizInicDireta[linha][coluna])

# # Inicialização dinâmica

# nLinhas = 3
# nColunas = 4
# matrizDinamica = [0] * nLinhas

# for linha in range(nLinhas):
#     matrizDinamica[linha] = [0] * nColunas

# print(matrizDinamica)

###

# # Inicializa a matriz de ordem 5x5  
# matriz = []

# # Lê os valores da matriz do teclado  
# print("Por favor, insira os elementos da matriz 5x5:")
# for i in range(5):
#     linha = list(map(int, input(f"Digite os 5 elementos da linha {i+1}, separados por espaço: ").split()))
#     matriz.append(linha)

# # Imprime a matriz de trás para frente  
# print("\nMatriz impressa da última linha e coluna para a primeira:")
# for i in range(4, -1, -1):
#     for j in range(4, -1, -1):
#         print(matriz[i][j], end=" ")
#     print()

###

# Função para ler uma matriz 2x2 do teclado  
def ler_matriz():
    matriz = []
    for i in range(2):
        linha = list(map(int, input(f"Digite os 2 elementos da linha {i+1}, separados por espaço: ").split()))
        matriz.append(linha)
    return matriz

# Função para somar duas matrizes 2x2  
def somar_matrizes(matriz1, matriz2):
    matriz_resultado = []
    for i in range(2):
        linha_resultado = []
        for j in range(2):
            linha_resultado.append(matriz1[i][j] + matriz2[i][j])
        matriz_resultado.append(linha_resultado)
    return matriz_resultado

# Leitura das duas matrizes do teclado  
print("Digite os elementos da primeira matriz 2x2:")
matriz1 = ler_matriz()

print("Digite os elementos da segunda matriz 2x2:")
matriz2 = ler_matriz()

# Soma das matrizes  
matriz_resultado = somar_matrizes(matriz1, matriz2)

# Exibição da matriz resultante  
print("\nMatriz resultante da soma:")
for linha in matriz_resultado:
    print(' '.join(map(str, linha)))


