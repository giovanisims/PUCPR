# O e-mail informa quantas cópias
# foram impressas e o custo total em reais. Implemente um programa em Python para
# calcular o valor pago por cópia

copy = int(input("Quantas copias você quer: "))
cost = float(input("Qual é o valor por copia (reais) "))
tcost = copy*cost
print(f"Imprimiram {copy} copia, custando {cost} cada e o valor total foi {tcost} reais")