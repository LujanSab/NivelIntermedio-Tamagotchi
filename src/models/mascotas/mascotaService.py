from src.models.mascotas.mascotaDAO import MascotaDAO
from src.controller.logger import log

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

    def actualizar(self, nombre, energia=None, limpieza=None, hambre=None, felicidad=None):
        campos = []
        valores = ()

        if energia is not None:
            campos.append("energia = ?")
            valores.append(energia)
        
        if limpieza is not None:
            campos.append("limpieza = ?")
            valores.append(limpieza)
        
        if hambre is not None:
            campos.append("hambre = ?")
            valores.append(hambre)

        if felicidad is not None:
            campos.append("felicidad = ?")
            valores.append(felicidad)

        if not campos:
            log("No se proporcionaron valores para actualizar.")
            print("No se proporcionaron valores para actualizar.")

        campos_str = ', '.join(campos)
        valores.append(nombre)

        self.dao.actualizar_estado_mascota(campos=campos_str, valores=valores)
    
    def eliminar(self):
        nombre = self.mascota.nombre
        dueño = self.mascota.dueño
        if not nombre and not dueño:
            return "Los campos no deben estar en blanco. Intente nuevamente. "
        else:
            mensaje = self.dao.eliminar_mascota(nombre, dueño)
            return mensaje

    def obtener_datos_mascota(self):
        nombre = self.mascota.nombre
        mascota = self.dao.extraer_datos_mascota(nombre)
        data = {
            "nombre" : mascota.nombre,
            "dueño" : mascota.dueño,
            "tipo" : mascota.tipo,
            "energia" : mascota.energia,
            "limpieza" : mascota.limpieza,
            "hambre" : mascota.hambre,
            "felicidad" : mascota.felicidad
        }
        return data
    
    def obtener_todas_las_mascotas(self):
        mascotas = self.dao.extraer_datos_mascotas()
        return mascotas
    
    def __str__(self):
        return str(self.mascota.nombre_mascota)