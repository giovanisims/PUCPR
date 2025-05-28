import socket
import time
import random
import os

def start_client(sensor_name):
    # The default client socket object is created with AF_INET which is for IPV4 and, AF_INET6 for IPV6.
    # By default it also uses SOCK_STREAM which is for TCP, for UDP its SOCK_DGRAM
    client_socket = socket.socket()

    host = '127.0.0.1'
    port = 8888

    try:
        # They really chose to go with a tuple twice huh
        client_socket.connect((host, port))
        print(f"{sensor_name}: connected to server at: {host}:{port}")

        while True:
            current_temperature = random.randint(15, 30)
            message = f"{sensor_name}|{current_temperature}"

            # The send function expects bytes so we encode it
            # UTF-8 (or 16 if we just wanna waste bandwith) works with everything but is a little slower
            # ASCII can be used for only english characters and basic puctuation (and a "del" character???)
            # latin-1 is ASCII but it also supports accents like á, õ, ü (Just use UTF this method is bad)
            
            client_socket.send(message.encode('utf-8'))
            print(f"{sensor_name} successfully sent this temperature: {current_temperature}°C")

            # You use recv to receive responses for TCP and recvfrom for UDP dont know why
            # 1024 is the max byte size of the response, you can use a file or preload it but here it doesnt matter
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received this response: {response}")

            time.sleep(3)

    except ConnectionRefusedError:
        print("Failed to connect to server")
    except KeyboardInterrupt:
        print(f"\n{sensor_name} shutting down...")
    except Exception as e:
        print(f"This went wrong: {e}")

    finally:
        # Your OS will usually clean up the zombies anyway but this is good practice
        client_socket.close()
        print("Connection closed")

def main():
    # The function getpid() gets the process ID of the current processes, i.e. if you run the code and it gets the PID 1234 the thread is called Sensor-1234  
    process_id = os.getpid()
    sensor_name = f"Sensor-{process_id}"
    
    print(f"Auto-generated sensor name: {sensor_name}")
    print(f"Starting {sensor_name}...")
    start_client(sensor_name)

if __name__ == "__main__":
    main()