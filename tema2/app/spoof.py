from scapy.all import IP, UDP, send

SERVER_IP = "server"   # numele serviciului din docker-compose
SERVER_PORT = 9999
SPORT = 12345

REAL_IP = "172.18.0.2"

pkt_real = IP(src=REAL_IP, dst=SERVER_IP) / UDP(sport=SPORT, dport=SERVER_PORT) / b"Salut real"
send(pkt_real)

FAKE_IP = "10.10.10.10"
pkt_fake = IP(src=FAKE_IP, dst=SERVER_IP) / UDP(sport=SPORT, dport=SERVER_PORT) / b"Salut fals"
send(pkt_fake)


