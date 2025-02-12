from src.models.mascotas.mascotas import Mascota, Perro, Gato
from src.controller.logger import log
from src.models.models import Mascotas
from peewee import IntegrityError, DoesNotExist
from datetime import datetime
import pytz


class MascotaService:
    def __init__(self, mascota: Mascota=None):
        self._mascota = mascota

    def crear_mascota(self, nombre, duenio, tipo):
        if tipo == "Perro":
            self._mascota = Perro(nombre, duenio)
            self.crear()
        elif tipo == "Gato":
            self._mascota = Gato(nombre, duenio)
            self.crear()

    def crear(self):
        try:
            zona_horaria_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
            now = datetime.now(zona_horaria_argentina).strftime("%d/%m/%Y, %H:%M:%S")

            mascota = Mascotas(
                duenio = self._mascota.nombre_dueño,
                nombre = self._mascota.nombre_mascota,
                tipo = self._mascota.tipo_de_mascota,
                energia = self._mascota.energia,
                limpieza = self._mascota.limpieza,
                hambre = self._mascota.hambre,
                felicidad = self._mascota.felicidad,
                ultima_vez_actualizado = now
            )

            mascota.save()
        except (Exception, IntegrityError) as e:
            log(e)

    def crear_objeto_mascota(
            self, nombre, 
            duenio, tipo, 
            energia, limpieza, 
            hambre, felicidad
            ):
        if tipo == "perro":
            self._mascota = Perro(nombre, duenio)
        elif tipo == "gato":
            self._mascota = Gato(nombre, duenio)
        self._mascota._energia = energia
        self._mascota._limpieza = limpieza
        self._mascota._hambre = hambre 
        self._mascota._felicidad = felicidad

    def actualizar(
            self, nombre, 
            energia: int=None, limpieza: int=None, 
            hambre: int=None, felicidad: int=None, 
            ultima_vez_actualizado: str = None
            ):
        try:
            zona_horaria_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
            ultima_vez_actualizado = datetime.now(zona_horaria_argentina).strftime("%d/%m/%Y, %H:%M:%S")

            actualizar= {k: v for k, v in locals().items() if k != 'self' and k != 'nombre' and k != 'zona_horaria_argentina' and v is not None}

            if 'energia' in actualizar:
                actualizar['energia'] = max(0, min(100, actualizar['energia']))
            if 'limpieza' in actualizar:
                actualizar['limpieza'] = max(0, min(100, actualizar['limpieza']))
            if 'hambre' in actualizar:
                actualizar['hambre'] = max(0, min(100, actualizar['hambre']))
            if 'felicidad' in actualizar:
                actualizar['felicidad'] = max(0, min(100, actualizar['felicidad']))

            if not actualizar:
                log('No hay datos para actualizar')

            query = (Mascotas
                    .update(**actualizar)
                    .where(Mascotas.nombre == nombre)
                    .execute())
                
            return query > 0
            
        except Exception as e:
            log(e)
    

    def eliminar(self, nombre: str, dueño: str):
        if not nombre and not dueño:
            log("Los campos no deben estar en blanco. Intente nuevamente. ")
        else:
            try:
                Mascotas.delete().where(Mascotas.nombre == nombre).execute()
            except Exception as e:
                log(e)


    def obtener_datos_mascota(self, nombre):
        try:
            datos_mascota = Mascotas.get(Mascotas.nombre == nombre)
            if datos_mascota:
                data = {
                    "id": datos_mascota.id,
                    "nombre_mascota" : datos_mascota.nombre,
                    "nombre_dueño" : datos_mascota.duenio,
                    "tipo" : datos_mascota.tipo,
                    "energia" : datos_mascota.energia,
                    "limpieza" : datos_mascota.limpieza,
                    "hambre" : datos_mascota.hambre,
                    "felicidad" : datos_mascota.felicidad,
                    "ultima_vez_actualizado": datos_mascota.ultima_vez_actualizado
                }
                return data
            return None
        except (Exception, DoesNotExist) as error:
            log(error)
        
        
    def obtener_todas_las_mascotas(self):
        query = Mascotas.select()
        
        mascotas = [(mascota.id, mascota.nombre, 
                     mascota.duenio, mascota.tipo, 
                     mascota.energia, mascota.limpieza, 
                     mascota.hambre, mascota.felicidad, 
                     mascota.ultima_vez_actualizado) for mascota in query]

        if mascotas:
            return mascotas
        else:
            log('No se encontro ninguna mascota')
    

    @property
    def mascota(self):
        return self._mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self._mascota = mascota
    