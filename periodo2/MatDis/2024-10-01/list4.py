# running = -1
# votes = []

# while running != 0:
#     user_input = int(input("Digite um valor de 0 a 6 \n"))
#     if user_input == 0:
#         running = 0
#     elif user_input < 0 or user_input > 6:
#         print("O valor deve ser de 0 a 6")
#     else:
#         match user_input:
#             case 1:
#                 votes.append("Python")
#             case 2:
#                 votes.append("C++")
#             case 3:
#                 votes.append("Java")
#             case 4:
#                 votes.append("Rust")
#             case 5:
#                 votes.append("C#")
#             case 6:
#                 votes.append("Outro")

# print("Linguagem | Votos | Percentual")
# for language in set(votes):
#     count = votes.count(language)
#     percentage = (count / len(votes)) * 100
#     print(f"{language} | {count} | {percentage:.2f}%")
# print(f"Total |{len(votes)}|")

# numeros = []

# for i in range(5):
#     num = float(input(f"Digite o número {i+1}: "))
#     numeros.append(num)


# numeros_invertidos = tuple(numeros[::-1])

# for i, num in enumerate(numeros_invertidos):
#     print(f"{i+1} -> {num}")

# medias = []

# for aluno in range(6):
#     print(f"\nAluno {aluno + 1}:")
#     notas = []
#     for nota in range(4):
#         nota_atual = float(input(f"Digite a nota {nota + 1}: "))
#         notas.append(nota_atual)
    
#     media = sum(notas) / 4
#     medias.append(media)

# alunos_com_media_acima_7 = sum(1 for media in medias if media >= 7.0)

# print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_com_media_acima_7}")

# import random

# def sorteia(num):
#     for _ in range(6):
#         num.append(random.randint(1, 100))


# def somaPar(num):
#     soma = 0
#     pares_somados = []
#     for n in num:
#         if n % 2 == 0:
#             soma += n
#             pares_somados.append(n)

#     print(f"Pares somados: {pares_somados}")
#     print(f"Soma dos pares: {soma}")

# num = []
# sorteia(num)
# print(f"Números sorteados: {num}")
# somaPar(num)

# def consoante(letra):
#     return letra.lower() in 'bcdfghjklmnpqrstvwxyz'


# caracteres = []
# consoantes = []


# for i in range(6):
#     caractere = input(f"Digite o caractere {i+1}: ")
#     caracteres.append(caractere)
    

#     if consoante(caractere):
#         consoantes.append(caractere)


# print(f"Consoantes lidas ({len(consoantes)}):")
# for i, consoante in enumerate(consoantes):
#     print(f"{i+1} -> {consoante}")

# somatorio = 0
# for x in range(3):
#     for y in range(2):
#         somatorio += (x * y) - 5

# print(somatorio)

# somatorio = 0
# for x in range(2,5):
#     for y in range(2,3):
#         somatorio += (x + y)** 2

# print(somatorio)

individuos = int(input("Digite o número de indivíduos: "))

alturas = []

for i in range(individuos):
    alturas.append(float(input(f"Digite a altura do indivíduo {i+1}: ")))

media = sum(alturas) / individuos  
print(f"A média das alturas é {media:.2f}")

