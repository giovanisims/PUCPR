# para salário de R$ 1.257,13 até R$ 2.512,08, alíquota de 15%
# • para salário acima de R$ 2.512,08, alíquota de 27,5 %
salaryB = -1
while salaryB < 0:   
    salaryB = float(input("Qual é o valor do seu salario: ")) * 100
if salaryB in range(127513,251208):
    tax = salaryB/100 * 0.15
    print(f"O valor do desconto é {tax}")
elif salaryB > 251208:
    tax = salaryB/100 * 0.275
    print(f"O valor do desconto é {tax}")
else:
    print("Você não terá desconto")
