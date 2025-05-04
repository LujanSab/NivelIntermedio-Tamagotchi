import socket
import sys

HOST, PORT = "localhost", 8080

data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################333
mensaje = f"Mensaje: {data}"

sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
received = sock.recvfrom(1024)

# ===== ENVIO Y RECEPCIÓN DE DATOS =================
 
print(received)
# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================