import os
from cryptography.fernet import Fernet

KEY_FILE = 'secret.key'

def generate_key():
    """Generates and saves a new key if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        print(f"New key generated and saved to {KEY_FILE}")

def load_key():
    """Loads the key from the file."""
    generate_key()
    return open(KEY_FILE, 'rb').read()

def get_cipher():
    """Returns a Fernet instance configured with the generated secret key."""
    return Fernet(load_key())

if __name__ == "__main__":
    generate_key()
