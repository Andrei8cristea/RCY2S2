import socket

SERVER_IP = "server"   # numele serviciului din docker-compose
SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mesaj = "Salut de la Andrei Cristea"
sock.sendto(mesaj.encode(), (SERVER_IP, SERVER_PORT))

print("Mesaj trimis.")
