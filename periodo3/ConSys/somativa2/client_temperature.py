import socket
import time
import random
import threading

def start_client(all_sensors_connected):

    # The default client socket object is created with AF_INET which is for IPV4 and, AF_INET6 for IPV6.
    # By default it also uses SOCK_STREAM which is for TCP, for UDP its SOCK_DGRAM
    client_socket = socket.socket()

    host = '127.0.0.1'
    port = 8888

    try:

        # They really chose to go with a tuple twice huh
        client_socket.connect((host, port))
        print(f"{threading.current_thread().name}: connected to server at: {host}:{port} ")

        # This pauses the current thread's execution until I "set" this event
        all_sensors_connected.wait()


        while True:
            # message = input('Input test message: ')
            
            # if message.lower() == "exit":
            #     exit()
            
            current_temperature = random.randint(15,30)
            thread_name = threading.current_thread().name
            message = f"{thread_name}|{current_temperature}"

            # The send function expects bytes so we encode it
            # UTF-8 (or 16 if we just wanna waste bandwith) works with everything but is a little slower
            # ASCII can be used for only english characters and basic puctuation (and a "del" character???)
            # latin-1 is ASCII but it also supports accents like á, õ, ü (Just use UTF this method is bad)
            
            client_socket.send(message.encode('utf-8'))
            print(f"{threading.current_thread().name} successfully sent this temperature: {current_temperature}°C")

            # You use recv to receive responses for TCP and recvfrom for UDP dont know why
            # 1024 is the max byte size of the response, you can use a file or preload it but here it doesnt matter
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received this response: {response}")

            time.sleep(1)

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
    sensors_amount = 5
    all_sensors_connected = threading.Event()

    for i in range(sensors_amount):
        client_thread = threading.Thread(
            target=start_client,
            # They really love their tuples huh
            args=(all_sensors_connected,),
            name=f"Sensor {i+1}"
        )

        # Without daemon threads Ctrl+C doesn't work properly
        client_thread.daemon=True
        client_thread.start()
        print(f"Started: {client_thread.name}")
        time.sleep(1)
    
    # Time for threads to connect

    # Changes the event to set so that the threads can run normally after they all connect
    all_sensors_connected.set()

    try:
        # I have no clue why but, I need this try except otherwise the threads don't function properly
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down all clients...")



if __name__ == "__main__":
    main()