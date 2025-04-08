import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAqnq7jWL0--KVZnr5emFz1JQWieO5urFE",
  "authDomain": "bsi-seginf.firebaseapp.com",
  "projectId": "bsi-seginf",
  "storageBucket": "bsi-seginf.firebasestorage.app",
  "messagingSenderId": "392766567382",
  "appId": "1:392766567382:web:1a45c59d3e20f101136a77",
  "databaseURL": "",
}

APP = pyrebase.initialize_app(firebaseConfig)

AUTH = APP.auth()

def trying_it_out():

  email = "eva-alvares@tuamaeaquelaursa.com"
  password = "admin1234"
  # token = AUTH.create_user_with_email_and_password(email, password)

  token = AUTH.sign_in_with_email_and_password(email,password)

  print(token)

  id_token = token['idToken']
  print(AUTH.get_account_info(id_token))

def main():
    menu()


def create_user():
    email_input = input('Email: ')
    password_input = input('Password: ')

    try:
      token = AUTH.create_user_with_email_and_password(email_input, password_input)
      print(token)
      id_token = token['idToken']
      AUTH.send_email_verification(id_token)
    except pyrebase.pyrebase.requests.exceptions.HTTPError:
       print('Email is already in use')
    else:
       print("Account created with success")

def login_user():
   pass

def menu():
  while True:
    choice = int(input('''
Would you like to sign in or create an account?
1 - Sign in
2 - Create Account
'''))
    if choice == 1:
      return login_user()
    elif choice == 2:
      return create_user()
    else:
      print('That\'s not an option ')

main()