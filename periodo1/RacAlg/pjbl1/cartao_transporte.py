# Alunos:
# Giovani Nota Simões, Sarah Maneira, Livia Rosenbach, Mirella Haisi
 
credit = 0
cost = 0

while True:
    admin_or_user = input("\n1 - Usuário\n2 - Administrador\n3 - Sair\n")
    if admin_or_user == "1":
        while True:
            option = input("\n1 - Carregar créditos\n2 - Usar cartão\n3 - Visualizar creditos\n4 - Voltar\n\n")
            if option == "1":
                credit_to_assign = int(input("Quanto você deseja carregar? "))
                if credit_to_assign < 0:
                    print("Valor inválido")
                else:
                    credit += credit_to_assign
                    print(f"Créditos disponíveis: {credit}")
            elif option == "2":
                if credit < cost:
                    print("Créditos insuficientes")
                else:
                    credit -= cost
                    print(f"Créditos restantes: {credit}")
            elif option == "3":
                print(f"Créditos disponíveis: {credit}")
            elif option == "4":
                break
            else:
                print("Opção inválida")
    elif admin_or_user == "2":
        password = "1234"
        for attempt in range(3):
            password_input = input("\nDigite a senha: ")
            if password_input != password:
                print("Senha incorreta")
            else:
                while True:
                    option = input("\n1 - Definir valor da passagem\n2 - Visualizar valor da passagem\n3 - Visualizar créditos\n4 - Voltar\n\n")
                    if option == "1":
                        cost_to_assign = int(input("Digite o valor da passagem: "))
                        if cost_to_assign < 0:
                            print("Valor inválido")
                        else:
                            cost = cost_to_assign
                    elif option == "2":
                        print(f"Valor da passagem: {cost}")
                    elif option == "3":
                        print(f"Créditos disponíveis: {credit}")
                    elif option == "4":
                        break
                    else:
                        print("Opção inválida")
                break
        else:
            print("\nNúmero máximo de tentativas excedido.")
    elif admin_or_user == "3":
        break
    else:
        print("Opção inválida\n")
    continue
