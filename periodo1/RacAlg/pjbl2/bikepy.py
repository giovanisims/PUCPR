credits = 4
history = []
bike_rented = False


# Obtém a data e a hora do usuário e faz um check se são válidos
def get_data_time():
    while True:
        data = input("Digite a data (dd/mm/yyyy): ")
        day, month, year = data.split("/")
        if int(day) > 31 or int(month) > 12:
            print("Data inválida")
        else:
            break
    while True:
        time = input("Digite o horário (24h, hh:mm): ")
        hour, minute = time.split(":")
        if int(hour) >= 24 or int(minute) >= 60:
            print("Horário inválido")
        else:
            break
    return data, time


# Obtém créditos para o usuário
def get_credits():
    global credits
    cost = 1.50
    print(f"O custo de cada crédito é de R${cost}")
    credits += int(input("Digite a quantidade de créditos que deseja comprar: "))
    print(f"Você têm {credits} créditos")
    return credits


# Obtém o login do usuário
def get_user():
    username = "admin"
    password = "abc123"
    for _ in range(3):
        input_username = input("Digite seu nome: ")
        input_password = input("Digite sua senha: ")
        if input_password != password or input_username != username:
            print("Senha inválida")
        else:
            print(f"Bem-vindo {username}")
            return True
    return False


# Aluga uma bicicleta
def rent_bike(pickup_data, pickup_time):
    global history, bike_rented
    history.append(f"Bicicleta alugada em {pickup_data} às {pickup_time}")
    print(f"Você alugou a bicicleta em {pickup_data} às {pickup_time}")
    bike_rented = True
    return pickup_data, pickup_time


# Devolve uma bicicleta
def return_bike(return_data, return_time):
    global credits, history, bike_rented
    history.append(f"Bicicleta devolvida em {return_data} às {return_time}\n")
    print("Bicicleta devolvida")
    bike_rented = False
    return return_data, return_time


# Imprime o histórico em grupos de retirada e devolução
def print_history():
    global history
    for bike in history:
        print(bike)


# Separa as datas novamente e cobra o usuário pelo aluguel da bicicleta
def charge_user(pickup_data, pickup_time, return_data, return_time):
    global credits

    # Separa os dados de data e hora
    pickup_day, pickup_month, pickup_year = map(int, pickup_data.split("/"))
    return_day, return_month, return_year = map(int, return_data.split("/"))
    pickup_hour, pickup_minute = map(int, pickup_time.split(":"))
    return_hour, return_minute = map(int, return_time.split(":"))

    # Calcula o total de dias
    days_in_use = (
        (return_year - pickup_year) * 365
        + (return_month - pickup_month) * 31
        + (return_day - pickup_day)
    )

    # Calcula o total de horas
    if return_hour < pickup_hour:
        days_in_use -= 1
        hours_in_use = (24 - pickup_hour) + return_hour
    else:
        hours_in_use = return_hour - pickup_hour

    total_hours = days_in_use * 24 + hours_in_use

    if pickup_minute > 0 or return_minute > 0:
        total_hours += 1

    credits -= total_hours
    print(f"Você foi cobrado por {total_hours} horas. Créditos restantes: {credits}")


# Menu de seleção
def main():
    global credits, bike_rented
    if get_user():
        while True:
            menu = input(
                "1 - Alugar uma bicicleta\n2 - Devolver uma bicicleta\n3 - Comprar créditos\n4 - Ver créditos\n5 - Ver histórico\n6 - Sair\nEscolha uma opção: "
            ).lower()
            if menu == "1":
                if bike_rented:
                    print("Você já alugou uma bicicleta.")
                elif credits < 5:
                    print(
                        f"Você tem {credits} créditos e precisa de 5 créditos para alugar uma bicicleta."
                    )
                    get_credits()
                else:
                    pickup_data, pickup_time = get_data_time()
                    rent_bike(pickup_data, pickup_time)
            elif menu == "2":
                if not bike_rented:
                    print("Você não alugou nenhuma bicicleta.")
                else:
                    return_data, return_time = get_data_time()
                    return_data, return_time = return_bike(return_data, return_time)
                    charge_user(pickup_data, pickup_time, return_data, return_time)
            elif menu == "3":
                get_credits()
            elif menu == "4":
                print(f"Você tem {credits} créditos.")
            elif menu == "5":
                print("Histórico de uso:")
                print_history()
            elif menu == "6":
                print("Volte sempre!")
                break
            else:
                print("Opção inválida")


# Inicia a função principal
if __name__ == "__main__":
    main()
