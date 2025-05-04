import socket
import threading
import socketserver
from pathlib import Path
import os
import sys
import binascii
from datetime import datetime


# global HOST
global PORT

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("Datos recibidos", data)
        print("Datos decodificados", data.decode("UTF-8"))
        value2 = 0xA0
        packed_data_2 = bytearray()
        packed_data_2 += value2.to_bytes(1, "big")
        socket.sendto(packed_data_2, self.client_address)        


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        print(f"Servidor escuchando en {HOST}:{PORT}")
        server.serve_forever()