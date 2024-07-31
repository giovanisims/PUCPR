# caixas = c
# livros = L
# livro = peso = p

box = int(input("Quantas caixas: "))
book = int(input("Quantos livros: "))
peso = float(input("Quanto cada libro pesa(kg) "))

pesoT = (book*peso)

print(f"O caminhão pode transportar {book} livros, com um peso de {pesoT} kg")