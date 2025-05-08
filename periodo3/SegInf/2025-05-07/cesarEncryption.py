# Cesar cypher, move letters k to the right k = 2 A -> C
# a = 97 z = 122

k = 3

def decrypt():
    encryptedText = input("Type out what you want to decrypt: ").lower()
    decryptedText = ""

    for letter in encryptedText:
        if letter.isalpha():  # Makes sure its a letter
            new_k = k % 26  #  Accounts for alphabet wrapping
            new_letter = ord(letter) - new_k
            if new_letter < 97:  # If it goes below 'a'
                new_letter = 123 - (97 - new_letter)  # Wrap around to 'z'
            decryptedText += chr(new_letter)
        else:
            decryptedText += letter  # Keep non-alphabetic characters unchanged

    print(f"Decrypted text: {decryptedText}")

def encrypt():
    unencryptedText = input("Type out what you want to encrypt: ").lower()
    encryptedText = ""

    for letter in unencryptedText:
            if letter.isalpha():  # Makes sure its a letter
                new_k = k % 26  # Accounts for alphabet wrapping
                new_letter = ord(letter) + new_k
                if new_letter > 122:  # If it goes beyond 'z'
                    new_letter = 96 + (new_letter - 122)  # Wrap around to 'a'
                encryptedText += chr(new_letter)
            else:
                encryptedText += letter  # Keep non-alphabetic characters unchanged

    print(f"Encrypted text: {encryptedText}")

def defineOffset():
    global k
    while True:
        try:
            k = int(input("Define the offset: "))
            return
        except:
            print("The offset needs to be a number")

def encryptDecryptMenu():
    while True:
        choice = input(f'''
1 - Set letter offset (Currently: {k})
2 - Encrypt
3 - Decrypt
4 - Exit
''')
        match choice:
            case "1":
                defineOffset()
            case "2":
                encrypt()
            case "3":
                decrypt()
            case "4":
                break
            case _:
                print("Invalid choice")

def main():
    encryptDecryptMenu()

if __name__ == "__main__":
    main()
