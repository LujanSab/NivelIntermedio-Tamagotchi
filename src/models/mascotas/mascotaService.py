from src.models.mascotas.mascotas import Mascota
from src.models.mascotas.mascotaDAO import MascotaDAO
from src.controller.logger import log

class MascotaService:
    def __init__(self, mascota: Mascota=None):
        self._mascota = mascota
        self.dao = MascotaDAO()

    def crear(self):
        self.dao.guardar_mascota(
            self._mascota.nombre_mascota,
            self._mascota.nombre_dueño,
            self._mascota.tipo_de_mascota,
            self._mascota.energia,
            self._mascota.limpieza,
            self._mascota.hambre,
            self._mascota.felicidad
        )

    def actualizar(self, nombre, energia: int=None, limpieza: int=None, hambre: int=None, felicidad: int=None):
        campos = []
        valores = []

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

        if not campos[0]:
            log("No se proporcionaron valores para actualizar.")
            print("No se proporcionaron valores para actualizar.")
        else:
            campos_str = ', '.join(campos)
            valores.append(nombre)

            self.dao.actualizar_estado_mascota(campos=campos_str, valores=valores)
    
    def eliminar(self, nombre: str, dueño: str):
        if not nombre and not dueño:
            return "Los campos no deben estar en blanco. Intente nuevamente. "
        else:
            mensaje = self.dao.eliminar_mascota(nombre, dueño)
            return mensaje

    def obtener_datos_mascota(self, nombre):
        datos = self.dao.extraer_datos_mascota(nombre)
        if datos:
            mascota = datos[0]
            data = {
                "id": mascota[0],
                "nombre_mascota" : mascota[1],
                "nombre_dueño" : mascota[2],
                "tipo" : mascota[3],
                "energia" : mascota[4],
                "limpieza" : mascota[5],
                "hambre" : mascota[6],
                "felicidad" : mascota[7]
            }
            return data
        return None
    
    def obtener_todas_las_mascotas(self):
        mascotas = self.dao.extraer_datos_mascotas()
        return mascotas
    
    @property
    def mascota(self):
        return self._mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self._mascota = mascota
    