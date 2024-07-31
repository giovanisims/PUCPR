# Python para calcular o valor
# médio, em quilos, de um prato. Assim, seu programa deve permitir a
# entrada do peso de cada prato (serão N no total) e imprimir na tela o peso
# médio. O programa deve também imprimir quantos pratos tem peso maior
# que 800 gramas.

def main():
    get_plates = int(input("Digite a quantidade de pratos: "))
    check_plates(get_plates)

def check_plates(plates):
    weight_total = 0
    plates800 = 0

    for _ in range(plates):
        weight = float(input("Digite o peso do prato: "))
        peso_total += weight

        if weight > 0.8:
            pratos_maior_800 += 1

    print(f"Peso médio: {weight_total / weight}")
    print(f"Pratos com peso maior que 800g: {plates800}")

main()