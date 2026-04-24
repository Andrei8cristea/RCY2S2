import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"Server pornit pe {SERVER_IP}:{SERVER_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    mesaj = data.decode()
    print(f"Primit mesaj: {mesaj} de la {addr}")
