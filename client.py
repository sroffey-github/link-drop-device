from dotenv import load_dotenv
import socket
import os

load_dotenv()

PORT = int(os.getenv('PORT'))
SERVER = os.getenv('HOST')
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True

def send(msg):
    message = msg.encode()
    client.send(message)
    print(client.recv(2048).decode())

while connected:
    msg = input('>>> ')
    if msg == DISCONNECT_MESSAGE:
        connected = False
        send(DISCONNECT_MESSAGE)
    else:
        send(msg)