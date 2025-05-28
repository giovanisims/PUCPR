import socket
import threading
import time

def start_admin_panel():
    host = "127.0.0.1"
    port = 8888
    # Your OS usually handles client ports automatically, by using "ephemeral ports" however, since we want to treat this client differently we use a static port
    local_port = 10000

    admin_panel_socket = socket.socket()

    # SOL_SOCKET means a socket level config, SO_REUSEADDR is so we can easily restart and "1" means it's set to TRUE
    admin_panel_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # We need to use a static port here since we use the same connection logic as the sensors
    admin_panel_socket.bind((host, local_port))
    try:
        admin_panel_socket.connect((host, port))

        while True:
            option = input('''
========== Control Panel ==========
[1] - See active sensors
[2] - Temperature averages for each sensor
[3] - Quit
''')
            match option:
                case "1":
                    admin_panel_socket.send("1".encode('utf-8'))
                case "2":
                    admin_panel_socket.send("2".encode('utf-8'))
                case "3":
                    raise KeyboardInterrupt
                case _:
                    print("Invalid option")
            print(admin_panel_socket.recv(1024).decode('utf-8'))
    except KeyboardInterrupt:
        print("Control panel shutting down...")
        exit()
    finally:
        admin_panel_socket.close()
        print("Connection closed")

def main():
    start_admin_panel()

if __name__ == "__main__":
    main()