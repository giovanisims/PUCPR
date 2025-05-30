# Giovani Nota Simoes Livia Rosembach Oliveira

import json
import hashlib
import os

# Not really sure why you need so many iterations but the more the merrier I guess
iterations = 100000

def sing_in(users_data_hashed, users_data_hashed_salted):
    while True:
        username = input("Input you username: ")
        if username in users_data_hashed and users_data_hashed_salted:
            password = input("Input your password: ")

            # Hashed password stuff
            encoded_password = password.encode('utf-8')
            hashed_password = hashlib.sha256(encoded_password)

            # Hashed and salted password stuff
            salt_hex = users_data_hashed_salted[username]["salt"]
            salt = bytes.fromhex(salt_hex)
            hashed_salted_password = hashlib.pbkdf2_hmac('sha256', encoded_password, salt, iterations).hex()

            if not hashed_password.hexdigest() in users_data_hashed[username]["password"]:
                print("Incorrect password")
            elif not hashed_salted_password in users_data_hashed_salted[username]["password"]:
                print("Incorrect Password")
            else:
                print(f"\nSuccesful Sign In with \"{username}\". \nRedirecting back to access menu.")
                break
        else:
            print(f"User {username} doesn't exist") 


def sign_up_hashing_salting(users_data_hashed, users_data_hashed_salted):
    while True:
        username1 = input("Input you username: ")
        username2 = input("Confirm your username: ")
        if username1 != username2:
            print("Usernames dont match")
        # Yeah this is much easier than when using csv
        elif username1 in users_data_hashed:
            print("Username already in use")
        else:
            break 
    while True:
        raw_password1 = input("Input your password: ")
        raw_password2 = input("Confirm your password: ")
        if raw_password1 != raw_password2:
            print("Passwords don't match")
        else:
            break
    
    # sha256 only hashes bytes??
    encoded_password = (raw_password1.encode('utf-8'))

    # Apparently 16 bytes is a common size for a salt and so is
    salt = os.urandom(16) 
    hashed_password = hashlib.sha256(encoded_password)
    hashed_salted_password = hashlib.pbkdf2_hmac('sha256', encoded_password, salt, iterations).hex()
    try:
        # This dump() function works like this dump(foo, bar, indent=X), so foo is the python object we are serializing
        # bar is the "file like" object we are writing foo to, and indent=4 is just pretty print
        with open('./users_data_hashed.json', 'w') as users_data_json_hashed:
            users_data_hashed[username1] = {"password": hashed_password.hexdigest()}
            json.dump(users_data_hashed, users_data_json_hashed, indent=4)
        with open('./users_data_hashed_salted.json', 'w') as users_data_json_hashed_salted:
            users_data_hashed_salted[username1] = {"password": hashed_salted_password, "salt": salt.hex()}
            json.dump(users_data_hashed_salted, users_data_json_hashed_salted, indent=4)
        print(f"\nUser {username1} sucessfully registered")
    except:
        print("Something went wrong when writing to the files")

def access_menu():
    while True:
        option = input('''
========== Welcome! ==========
[1] - Sign Up
[2] - Sign In
==============================
''') 
        if option not in ["1","2"]:
            print("Invalid Option")
        else:
            return option


def main():
    while True:

        try:
            with open('./users_data_hashed.json', 'r') as users_data_json_hashed:
                users_data_hashed = json.load(users_data_json_hashed)
        except FileNotFoundError:
            print("users_data_hashed.json not found.")
        except json.JSONDecodeError:
            print(f"Error decoding users_data_hashed.json. Using an empty file")
            users_data_hashed = {} 

        try:
            with open('./users_data_hashed_salted.json', 'r') as users_data_json_hashed_salted:
                users_data_hashed_salted = json.load(users_data_json_hashed_salted)
        except FileNotFoundError:
            print("users_data_hashed_salted.json not found.")
        except json.JSONDecodeError:
            print(f"Error decoding users_data_hashed_salted.json. Using an empty file")
            users_data_hashed_salted = ()

        option = access_menu()
        match option:
            case "1":
                sign_up_hashing_salting(users_data_hashed, users_data_hashed_salted)
            case "2":
                sing_in(users_data_hashed, users_data_hashed_salted) 
            case _:
                print("how did you mess this up this badly")
                access_menu()

if __name__ == "__main__":
    main()