from scapy.all import IP, UDP, send

SERVER_IP = "server"   # numele serviciului din docker-compose
SERVER_PORT = 9999

pkt = IP(dst=SERVER_IP) / UDP(sport=12345, dport=SERVER_PORT) / b"Salut de la Andrei"
send(pkt)

# se observa ca serverul vede exact portul setat  de mine manual. P sursa nu mai este ales automat din sistem ci ales
# de mine in acest header file