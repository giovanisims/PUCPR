# Cada cliente pode comprar quantas entradas quiser;
entrada = int(input("Quantas entradas você quer? "))
# • O cliente deve apresentar no ato do pagamento sua carteira que informa qual é o seu
# desconto atual (0 a 100%);
desconto = float(input("Qual é o desconto "))
# • O cliente poderá também descontar o valor do ticket do estacionamento no ato da
# compra.
ticket=input("Você tem ticket do estacionamento? (Sim/Não) ").lower()
valor = (entrada * (desconto/100) * 25)
if ticket in ("sim"):
    vticket = int(input("Qual é o valor do ticket? "))
    print("O valor da sua(s) entrada é",(valor - vticket))
else:
    print(f"O valor da sua(s) entrada é {valor}")