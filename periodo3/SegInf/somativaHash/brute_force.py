# Giovani Nota Simoes Livia Rosembach Oliveira

import json
import time
import hashlib
import string

# I'm not acutally sure how you are supposed to find how many iterations were used
iterations = 100000

def brute_force(user_data):
    # I could have just typed the characters out but I felt like doing this properly
    chars = string.ascii_letters + string.digits
    
    for username in user_data:
        start_time_password = time.perf_counter()
        storage_password_hash = user_data[username]["password"]
        
        # Hashed passwords
        if len(user_data[username]) == 1:
            finished = False
            for char1 in chars:
                for char2 in chars:
                    for char3 in chars:
                        for char4 in chars:
                            new_password = char1 + char2 + char3 + char4
                            encoded_candidate = new_password.encode('utf-8')

                            new_password_hash = hashlib.sha256(encoded_candidate).hexdigest()
                            if new_password_hash == storage_password_hash:
                                end_time_password = time.perf_counter()
                                print(f"SUCCESS! Password for \"{username}\" found: \"{new_password}\"")
                                print(f"Time taken for this password: {end_time_password - start_time_password:.03f}\n")
                                finished = True
                                break
                            
                            current_time = time.perf_counter()
                            if (current_time - start_time_password) > 90:
                                print(f"\nFAILED to find password for \"{username}\" after 90 seconds. Moving on to next user")
                                finished = True
                                break 
                        if finished:
                            break 
                    if finished:
                        break 
                if finished:
                    break 
        # Hashed and salted passwords
        elif len(user_data[username]) == 2:
            pass
            salt_hex = user_data[username]["salt"]
            salt = bytes.fromhex(salt_hex)
            
            finished = False
            for char1 in chars:
                for char2 in chars:
                    for char3 in chars:
                        for char4 in chars:
                            new_password = char1 + char2 + char3 + char4
                            encoded_candidate = new_password.encode('utf-8')
                            
                            new_password_hash = hashlib.pbkdf2_hmac('sha256', encoded_candidate, salt, iterations).hex()
                            if new_password_hash == storage_password_hash:
                                end_time_password = time.perf_counter()
                                print(f"SUCCESS! Password for \"{username}\" found: \"{new_password}\"")
                                print(f"Time taken for this password: {end_time_password - start_time_password:.03f}\n")
                                finished = True
                                break
                            
                            current_time = time.perf_counter()
                            if (current_time - start_time_password) > 90:
                                print(f"\nFAILED to find password for \"{username}\" (salted) after 90 seconds. Moving on to next user")
                                finished = True
                                break
                        if finished:
                            break
                    if finished:
                        break
                if finished:
                    break
        else:
            print("How did you even do this")
            exit()

def get_user_data():
    with open('./users_data_hashed.json', 'r') as hashed_json:
        hashed = json.load(hashed_json)
    with open('./users_data_hashed_salted.json', 'r') as hashed__salted_json:
        hashed_salted = json.load(hashed__salted_json)
    return [hashed, hashed_salted]


def main():
    hashed, hashed_salted = get_user_data()
    
    start_time_hashed = time.perf_counter()
    brute_force(hashed)
    end_time_hashed = time.perf_counter()
    print(f"Total time taken for unsalted hashes: {int(end_time_hashed - start_time_hashed)} seconds")

    start_time_hashed_salted = time.perf_counter()
    brute_force(hashed_salted) # This would target salted passwords
    end_time_hashed_salted = time.perf_counter()
    print(f"Time taken for salted hashes: {int(end_time_hashed_salted - start_time_hashed_salted)} seconds")

if __name__ == "__main__":
    main()