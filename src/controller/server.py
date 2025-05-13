import socketserver

global PORT

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    Esta clase maneja las solicitudes entrantes al servidor UDP.

    Cada vez que se recibe un mensaje desde un cliente, el método `handle` se ejecuta.
    Este método decodifica el mensaje recibido (en bytes) utilizando UTF-8, lo limpia 
    de espacios innecesarios y lo guarda en un archivo de texto llamado 'registro_servidor.txt'.

    El objetivo es registrar en ese archivo cada mensaje recibido por el servidor.
    """
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