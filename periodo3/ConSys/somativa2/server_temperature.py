import socket

def handle_client(client_socket, address):
    print(f"Successfully conected to socket: {address}")

    try:
        while True:

            # You know the drill, recv for response 1024 max bytes and UTF-8 decoding 
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:
                break

            response = f"Succesfully received \"{message}\""
            print(f"Succesfully received \"{message}\" from socket: {address}")

            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Message from socket: {address} failed with: {e}")
    finally:
        # You know what's going on here already
        client_socket.close()

def start_server():

    host = '127.0.0.1'
    port = 8888

    # Server socket object
    server_socket = socket.socket()

    # We use this since TCP takes a few minutes to unlock a port after you stop using it so restarting is a pain
    # SOL_SOCKET is because we are setting configuring at socket-level rather than protocol-level
    # SO_REUSEADDR is the actual option we are changing and the 1 is to enable it since its boolean w/ 1-0
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # You need to set the above options before binding the socket otherwise it doesnt apply
    server_socket.bind((host, port))

    # You can limit the amount of incoming connections here but I didnt want to. Ex: foo_bar.listen(10) 
    # For whatever reason this takes a tuple with two args, instead of just two separate args
    server_socket.listen()
    print(f"Server listening on socket: {host}:{port}")

    try:
        while True:
            '''
            Alright this one is a bit rough, since I'm using TCP I cant respond to the client using its own sockets
            (i.e. you cant send the response back to the client using just 123.123.123.123:1234) this works in UDP.
            However this is TCP so I NEED to respond, which means I gotta do the TCP handshake which is kinda complicated
            In python that means that I need to use the clients socket object but, that object is all the way in another file
            So its easier to just re-instatiate in this file (idk if that's a term) that's half of what foo_bar.accept() does
            When printed out that object has 6 attributes:

            fd=4: File descriptor (idk what this acutally is)
            family=2: IPv4 (AF_INET) This is a default setting
            type=1: TCP (SOCK_STREAM) This is a default setting
            proto=0: Default protocol (idk what this is either)
            laddr: Server side socket
            raddr: Client side socket

            The other half of the accept function is just a tuple (AGAIN) with the host and port of the client
            '''
            client_socket, address = server_socket.accept()

            # I want to acknowledge that I know calling other functions inside of one functions is bad but this works really well
            handle_client(client_socket, address)

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        # Your OS does clean this up but this is good practice
        server_socket.close
        print("Server closed")

def main():
    start_server()

if __name__ == "__main__":
    main()