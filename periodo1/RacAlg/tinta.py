import math

# a lata de tinta custa 50,00 reais;
# • cada lata contém 5 litros;
# • cada litro de tinta pinta 3 metros quadrados
# # cada lata pinta 15 metros quadrados
# Dados de entrada: altura (H) e raio (R)
# • Dados de saída: custo (C) e quantidade (QTDE)

# custo para pintar
# tanques cilíndricos de combustível, em que são fornecidos a altura e o raio desse cilindro.
altura = float(input("Qual é a altura do cilindro: "))
raio = float(input("Qual é o raio do cilindro: "))

# qtde = print((2*3.14 * raio)(raio + altura))

qtde = float((2*3.14*raio*altura)+(2*3.14*raio*raio))
qtdeLatas = math.ceil(qtde/15)
custo = int(qtdeLatas * 50)
print(f"O custo é {custo} reais, e vai precisar de {qtdeLatas} latas")