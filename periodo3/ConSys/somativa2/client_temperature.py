import socket
import time

def start_client():

    # The default client socket object is created with AF_INET which is for IPV4 and, AF_INET6 for IPV6.
    # By default it also uses SOCK_STREAM which is for TCP, for UDP its SOCK_DGRAM
    client_socket = socket.socket()

    host = '127.0.0.1'
    port = 8888

    try:

        # They really chose to do it with a tuple twice huh
        client_socket.connect((host, port))
        print(f"Server connected on socket: {host}:{port} ")

        while True:

            message = input('Input test message: ')
            
            if message.lower() == "exit":
                exit()
            
            # The send function expects bytes so we encode it
            # UTF-8 (or 16 if we just wanna waste bandwith) works with everything but is a little slower
            # ASCII can be used for only english characters and basic puctuation (and a "del" character???)
            # latin-1 is ASCII but it also supports accents like á, õ, ü (Just use UTF this method is bad)
            
            client_socket.send(message.encode('utf-8'))
            print(f"Successfully sent this message: {message}")

            # You use recv to receive responses for TCP and recvfrom for UDP dont know why
            # 1024 is the max byte size of the response, you can use a file or preload it but here it doesnt matter
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received this response: {response}")

    except ConnectionRefusedError:
        print("Failed to connect to server")
    except KeyboardInterrupt:
        print("\nClient shutting down...")
        exit()
    except Exception as e:
        print(f"This went wrong: {e}")

    finally:
        # Your OS will usually clean up the zombies anyway but this is good practice
        client_socket.close()
        print("Connection closed")

def main ():
    for i in range(3):
        start_client()
        print(f"Attempting to connect to the server for the {i+1} time...")
        time.sleep(3)

if __name__ == "__main__":
    main()