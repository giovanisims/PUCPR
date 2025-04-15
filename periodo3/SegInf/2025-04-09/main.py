# Giovani Nota Simões
# Livia Rosembach Oliveira

# Careful if you open the csv files in vscode depending on the position of your mouse it changes where it adds lines
# Either close them or keep your mouse under the last line

import csv

def filemanager(username):
    """
    Manages file operations for a given user.

    Args:
        username (str): The username of the logged-in user.
    """
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
        if choice in ['1','2','3','4']:
            checkaccess(username, int(choice))
        elif choice == '5':
            return
        else:
            print('Invalid Option')

def checkaccess(username, choice):
    """
    Checks if a user has permission to perform a specific action on a file.

    Args:
        username (str): The username of the user.
        choice (int): The action to be performed (1: Read, 2: Write, 3: Delete, 4: Run).

    Returns:
        bool: True if the user has permission, False otherwise.
    """
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
    """
    Logs in a user by verifying their username and password against the credentials stored in a CSV file.

    Returns:
        str: The username if login is successful, False otherwise.
    """
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
    """
    Signs up a new user by creating a new entry in the credentials and permissions CSV files.
    """
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
    """
    Displays the authentication menu, allowing users to sign up, log in, or exit.
    """
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
    """
    Main function to start the authentication menu.
    """
    authmenu()

if __name__ == '__main__':
    main()