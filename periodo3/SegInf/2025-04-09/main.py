import csv

def filemanager(username):
    print(f'Welcome {username}')
    while True:
        choice = input('''
Select a command:
    1 - Read  
    2 - Write  
    3 - Delete  
    4 - Run  
    5 - Exit 
''')
        match choice:
            case '1':
                checkaccess(username, int(choice))
            case '2':
                checkaccess(username, int(choice))
            case '3':
                checkaccess(username, int(choice))
            case '4':
                checkaccess(username, int(choice))
            case '5':
                return

def checkaccess(username, choice):
    filename = input('Input the filename: ').strip()
    with open('permissions.csv', 'r') as csvfile:
        permissionreader = csv.reader(csvfile, delimiter=',')
        next(permissionreader)
        for row in permissionreader:
            if username == row[0] and filename == row[1]:
                if row[choice + 1] == '1':
                    print('You can do that!')
                    return True  
                else:
                    print('You can\'t do that!')
                    return False  
        print("No matching permissions found.")
        return False

def login():
    username = input("Input your username: ").strip()
    password = input("Input your password: ").strip()
    with open('credentials.csv', 'r') as csvfile:
        loginreader = csv.reader(csvfile, delimiter=',')
        next(loginreader)
        for row in loginreader:
            if username == row[0] and password == row[1]:
                return username  
        return False

def signup():
    username = input('Input your username: ').strip()
    if not username:
        print('Invalid username')
        return False

    password = input('Input your password: ').strip()
    if not password:
        print('Invalid password')
        return False

    while True:
        passwordconfirm = input('Confirm your password: ').strip()
        if password != passwordconfirm:
            print('Passwords are different')
        else:
            break

    with open('credentials.csv', 'a', newline='') as csvfile:
        signupwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        signupwriter.writerow([username, password])

    with open('permissions.csv', 'a', newline='') as csvfile:
        permissionswriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        permissionswriter.writerow([username,"placeholder",0,0,0,0])

def authmenu():
    while True:
        choice = input('''
--------------------------
Select an option:
    1 - Sign-Up  
    2 - Log-In  
    3 - Leave  
''')
        match choice:
            case '1':
                signup()
            case '2':
                username = login()
                if username:
                    filemanager(username)
                else:
                    print('Login information incorrect')
            case '3':
                exit('Goodbye :)')
            case _:
                print('Invalid Option')

def main():
    authmenu()

if __name__ == '__main__':
    main()