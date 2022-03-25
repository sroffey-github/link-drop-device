from dotenv import load_dotenv
import socket
import os
import threading

load_dotenv()

PORT = int(os.getenv('PORT'))
SERVER = os.getenv('HOST')
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(2048).decode()
        if msg == DISCONNECT_MESSAGE:
            conn.send('[!] Connection Closed'.encode())
            connected = False

        print(f'[{addr[0]}:{addr[1]}] {msg}')
        os.system(f'python3 show.py "[{addr[0]}:{addr[1]}] {msg}" &')
        conn.send("[i] Message Received".encode())

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()