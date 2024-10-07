import matplotlib.pyplot as plt
import numpy as np

def funcao1grau(a, b, x):
    return a * x + b

c = 1

vetorX = np.arange(-5, 5, c)
# print(vetorX)

# 3. a) A função arange cria um vetor com os valores de -5 a 5 (sem incluir o 5) com progressão de 1

a = 2
b = 5

vetorY = np.arange(-5, 5, c)
# print(vetorY)

fig = plt.figure(figsize=(10, 10))
plt.plot(vetorX, vetorY, label="Funcação 1o grau")

plt.show()

# 5. a) É um grafico discreto que representa um função afim
# 5 .b) É o mesmo grafico só que ele te maior frequencia dos pontos
# 5 .c) Os pontos ficam frequentes o bastante que a função parece ser continua com o c = 0.05
# 5 .d) A função vira uma reta continua com a função plot em vez de scatter



