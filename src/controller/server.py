import socketserver

# global HOST
global PORT

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        data_decodificada = data.decode("UTF-8")
        with open("registro_servidor.txt", "a", encoding="utf-8") as f:
            f.write(data_decodificada + "\n")

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        print(f"Servidor escuchando en {HOST}:{PORT}")
        server.serve_forever()