import socket
import threading

def start_panel():
    host = "127.0.0.2"
    port = "8888"

    panel_socket = socket.socket()

    # 
    panel_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def main():
    start_panel()

if __name__ == "__main__":
    main()