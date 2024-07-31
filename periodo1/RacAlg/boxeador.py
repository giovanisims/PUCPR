peso = float(input("Qual é seu peso em kg: "))
if peso < 50: print("Você é peso palha")
elif peso >= 50 and peso <= 59.99: print("Você é peso pluma")
elif peso >= 60 and peso <= 75.99: print("Você é peso leve")
elif peso >= 76 and peso <= 87.99: print("Você é peso pesado")
else: print("Você é super pesado")

