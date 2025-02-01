from models.mascotas.mascotas import Perro, Gato
from models.mascotas.mascotaService import MascotaService

class Controlador:
    def __init__(self):
        self.masc_service = MascotaService() 
    # --------------------------------------------------
    # FUNCIONES AUXILIARES
    # --------------------------------------------------
    def alta(self, nombre, duenio, tipo):
        if tipo == "Perro": 
            perro = Perro(duenio, nombre)
            self.masc_service.crear(perro)
        elif tipo == "Gato":
            gato = Gato(duenio, nombre)
            self.masc_service.crear(gato)

    def consulta(self):
        datos = self.service.obtener_todas_las_mascotas()
        return datos
    
    def eliminar(self, nombre, duenio):
        self.service.eliminar(nombre, duenio)
    
    def modificar(self):
        pass