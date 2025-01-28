from src.models.mascotas.mascotaDAO import MascotaDAO


class MascotaService:
    def __init__(self, mascota):
        self.mascota = mascota
        self.dao = MascotaDAO()

    def crear(self):
        self.dao.guardar_mascota(
            self.mascota.nombre_mascota,
            self.mascota.nombre_dueño,
            self.mascota.tipo,
            self.mascota.energia,
            self.mascota.limpieza,
            self.mascota.hambre
        )
    
    def obtener_por_nombre(self, nombre):
        mascota = self.dao.extraer_datos_mascota(nombre)

        return mascota
    
    def __str__(self):
        return str(self.mascota.nombre_mascota)