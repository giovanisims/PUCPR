# Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto
# Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um
# algoritmo em Python que calcule e mostre quantos anos serão necessários
# para que Felisberto seja maior que Anacleto

anacleto = 1.5
felisberto = 1.1
anos = 0

while felisberto < anacleto:
    anacleto += 0.02
    felisberto += 0.03
    anos += 1

print(anos)