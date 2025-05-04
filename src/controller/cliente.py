import socket
import sys

HOST, PORT = "192.168.1.4", 139
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################
mi_valor = 0x00003EF5
print(type(mi_valor))
packed_data = bytearray()
packed_data += mi_valor.to_bytes(4, "big")
mensaje = packed_data

sock.sendto(mensaje, (HOST, PORT))
received = sock.recvfrom(1024)

print(received)