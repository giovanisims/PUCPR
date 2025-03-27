import csv

def checkPassword(ulogin, uPassword, userInfo):
    for lines in userInfo:
        if ulogin == lines['login'] and uPassword == lines['password']:
            return True

def actualProgram(login):
    print(f"Seja bem vindo, {login}")


def main ():
    with open('userInfo.csv', mode='r') as csvFile:
        userInfo = list(csv.DictReader(csvFile))
    attempts = 0
    while attempts < 5:
        login = input("Input your login: ")
        password = input("Input your password: ")
        if checkPassword(login, password, userInfo):
            actualProgram(login)
            break
        else:
            print("Wrong password")
            attempts +=1

    if attempts >= 5:
        print("You input the wrong password too many times, ending runtime")

main()