import socket
import threading
from collections import deque, defaultdict

SENSORS = []
'''
The defaultdict function automatically creates key value pairs instead of raising a KeyError. Ex. If you try to access Sensor 5, and it hasn't been added to the
dictionary it will create a key called "Sensor 5", then lambda dinamically creates a function that makes a new deck, so you get a structure like this:
{"foo": deque[1, 2, 3, 4, 5, ...], maxlen=INT}
And since it's all dynamic it's really robust! Unless you try to randomly access something like "Racecar 69" but at that point it's your own fault
'''
SENSOR_TEMPS = defaultdict(lambda: deque(maxlen=10))

'''
This creates a individual object that all threads will need to access, which means I can use it to make threads wait dinamically, since all threads share it
this is necessary because the client both reads and writes to SENSOR_TEMPS, and if that happens while you try to access it with the control panel things break
apparently the correct usage for data locks in python is using the "with" function since because that functions automatically frees/closes the data you are using
it's helps with optimization (I think?), (it's also needed to free the lock apparently, but the lock should be freed when the thread finishes using it anyway
so I'm kinda confused, whatever threads are weird in python), so that's why I'm using "with" here 
'''
data_lock = threading.Lock()

def handle_client(client_socket, address):
    # deque automatically removes the oldest entry in a list 
    temp_list = deque(maxlen=10)

    client_ip, client_port = address
    address_str = f"{client_ip}:{client_port}"
    
    current_sensor_name = None
    
    print(f"Successfully conected to socket: {address_str}")
    try:
        while True:
            response = ""

            # You know the drill, recv for response 1024 max bytes and decoding the message 
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received input from {address_str}")

            if not message:
                break

            if client_port == 10000:
                match message:
                    case "1":
                        print(f"Sending sensor sockets...")
                        with data_lock:
                            response += f"You have {len(SENSORS)} sensors running on: \n"
                            for sensor_name in SENSORS:
                                response += f"{sensor_name} connected \n"
                    case "2":
                        print(f"Sending average temperatures per socket")
                        with data_lock:
                            if not SENSORS:
                                response += "Please wait a second and let the system gather more data"
                            else:
                                for sensor_name in SENSORS:
                                    temps = SENSOR_TEMPS[sensor_name]
                                    if len(temps) > 1:
                                        avg_temp = (sum(temps) / len(temps))
                                        response += f"{sensor_name}: {(avg_temp):.0f}°C or {(avg_temp * 9/5 + 32):.0f}°F \n"
                                    else:
                                        response += f"{sensor_name}: Please wait a second and let the system gather more data \n"
            else:
                try:
                    sensor_name, temperature_str = message.split('|', 1)
                    temperature = int(temperature_str)
                    current_sensor_name = sensor_name
                    
                    
                    # Here I'm using the lock because it can mess things up if the threads race each other and end up inserting duplicate sensor names then,
                    # it accesses the temperature dict, if it fails defaultdict creates the appropriate key, if it succeeds it adds the most recent temp reading
                    with data_lock:
                        if sensor_name not in SENSORS:
                            SENSORS.append(sensor_name)
                        SENSOR_TEMPS[sensor_name].append(temperature)
                    
                    response = f"Temperature received: \"{temperature}\" From socket: {address_str}"
                except ValueError:
                    response = f"Temperature received: \"{message}\" From socket: {address_str}"
                    if (client_port not in SENSORS) and (client_port != 10000):
                        SENSORS.append(client_port)
                    temp_list.append(int(message))


                    # print(f"this is the average temp: {(total_temp / len(temp_list)):.0f} On the sensor at socket: {address_str}")
 
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Message from socket: {address_str} failed with: {e}")
    finally:
        # This removes the relevant sensor from both global arrays whenever it either, fails or closes normally
        if current_sensor_name:
            with data_lock:
                if current_sensor_name in SENSORS:
                    SENSORS.remove(current_sensor_name)
                if current_sensor_name in SENSOR_TEMPS:
                    del SENSOR_TEMPS[current_sensor_name]
        # You know what's going on here already
        client_socket.close()

def start_server():

    host = '127.0.0.1'
    port = 8888

    # Server socket object
    server_socket = socket.socket()

    # We change these settings because TCP takes a few minutes to unlock a port after you stop using it so restarting is a pain
    # SOL_SOCKET is because we are setting configuring at socket-level rather than protocol-level
    # SO_REUSEADDR is the actual option we are changing and the 1 is to enable it since its boolean w/ 1-0
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # You need to set the above options before binding the socket otherwise it doesnt apply
    # For whatever reason this takes a tuple with two args, instead of just two separate args
    server_socket.bind((host, port))

    # You can limit the amount of incoming connections here but I didnt want to. Ex: foo_bar.listen(10) 
    server_socket.listen()
    print(f"Server listening on socket: {host}:{port}")

    try:
        while True:
            '''
            Alright this one is a bit of a mouthful, since I'm using TCP I cant respond to the client using its own sockets
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

            # I want to acknowledge that I know calling other functions inside of a functions is bad but this works really well so screw it
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address)
            )

            # This turns the normal thread into a daemon thread, i.e. It doesn't prevent the program from exiting if still active
            client_thread.daemon=True
            client_thread.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        # Your OS does clean this up but this is good practice
        server_socket.close()
        print("Server closed")

def main():
    start_server()

if __name__ == "__main__":
    main()