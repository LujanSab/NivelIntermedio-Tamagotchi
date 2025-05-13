import socket

HOST, PORT = "localhost", 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def enviar_datos_sv(mensaje):
    """
    Función que recibe los datos enviados por el servidor.
    """
    sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
    received = sock.recvfrom(1024)
    return received
