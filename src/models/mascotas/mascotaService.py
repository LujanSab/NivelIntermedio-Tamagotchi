from src.models.mascotas.mascotas import Mascota, Perro, Gato
from src.controller.logger import log
from src.models.models import Mascotas
from peewee import IntegrityError, DoesNotExist
from datetime import datetime, timedelta
import pytz


class MascotaService:
    """
    La clase `MascotaService` en Python proporciona métodos para crear, actualizar, eliminar y
    recuperar información sobre mascotas, así como para administrar sus estados y propiedades.

    :param nombre: El parámetro "nombre" hace referencia al nombre de la mascota o mascota. Se utiliza para
    identificar la mascota específica al realizar operaciones como crear, actualizar o eliminar
    datos de mascotas en la clase MascotaService
    :param duenio: El parámetro `duenio` en la clase `MascotaService` hace referencia al dueño o
    tutor de la mascota (mascota). Se utiliza para identificar a la persona responsable del cuidado y
    bienestar de la mascota
    :param tipo: El parámetro `tipo` en el método `crear_mascota` y el método `crear_objeto_mascota` hace referencia al tipo de mascota que se está creando. Puede ser "Perro" o "Gato". Este parámetro se utiliza para determinar qué clase
    """
    
    def __init__(self, mascota: Mascota=None):
        self._mascota = mascota

    def crear_mascota(self, nombre, duenio, tipo):
        try:
            if tipo == "Perro":
                self._mascota = Perro(nombre, duenio)
                self.crear()
            elif tipo == "Gato":
                self._mascota = Gato(nombre, duenio)
                self.crear()
        except Exception as e:
            log(e)
            print(e)

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
                social = self._mascota.social,
                estado = self._mascota.estado,
                ultima_actualizacion = now
            )

            mascota.save()
        except (Exception, IntegrityError) as e:
            log(e)

    def crear_objeto_mascota(
            self, nombre, 
            duenio, tipo, 
            energia, limpieza, 
            hambre, felicidad, 
            social
            ):
        if tipo == "perro":
            self._mascota = Perro(nombre, duenio)
        elif tipo == "gato":
            self._mascota = Gato(nombre, duenio)
        self._mascota._energia = energia
        self._mascota._limpieza = limpieza
        self._mascota._hambre = hambre 
        self._mascota._felicidad = felicidad
        self._mascota._social = social

    def actualizar(
        self, 
        nombre: str,
        energia: int = None,
        limpieza: int = None,
        hambre: int = None,
        felicidad: int = None,
        social: int = None,
        estado: str = None
    ):
        try:
            zona_horaria_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
            ultima_actualizacion = datetime.now(zona_horaria_argentina).strftime("%d/%m/%Y, %H:%M:%S")

            actualizar = {
                "energia": energia,
                "limpieza": limpieza,
                "hambre": hambre,
                "felicidad": felicidad,
                "social": social,
                "estado": estado,
                "ultima_actualizacion": ultima_actualizacion
            }

            actualizar = {k: v for k, v in actualizar.items() if v is not None}

            for key in ["energia", "limpieza", "hambre", "felicidad", "social"]:
                if key in actualizar:
                    actualizar[key] = max(0, min(100, actualizar[key]))

            if actualizar:
                query = (Mascotas
                        .update(**actualizar)
                        .where(Mascotas.nombre == nombre)
                        .execute())
                return query > 0
            else:
                log('No hay datos para actualizar')

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
                    "social" : datos_mascota.social,
                    "estado" : datos_mascota.estado,
                    "ultima_actualizacion": datos_mascota.ultima_actualizacion
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
                     mascota.social, mascota.ultima_actualizacion, 
                     mascota.estado) for mascota in query]

        if mascotas:
            return mascotas
        else:
            log('No se encontro ninguna mascota')

    def actualizar_estado_mascota(self, nombre_mascota, obj_mascota, dict_mascota, diferencia_tiempo):
            PRIMER_CAMBIO_SEGUNDOS = 15 #cambios cada 15 segundos
            DIA_LIMITE = 5 #dia de moricion 
            
            CAMBIO_VALORES_SEGUNDOS = {
                "energia" : 2, 
                "limpieza" : 1,
                "hambre" : 2,
                "felicidad": 1, 
                "social": 1
            }

            segundos_transcurridos = diferencia_tiempo.total_seconds()
            intervalo_segundos = segundos_transcurridos / PRIMER_CAMBIO_SEGUNDOS  #cantidad de veces que sucede los cambios

            try:
                if diferencia_tiempo >= timedelta(days=DIA_LIMITE):

                    self.actualizar(
                        nombre=nombre_mascota, 
                        energia=0,
                        limpieza=0, 
                        hambre=100,
                        felicidad=0,
                        social=0,
                        estado='Morido'
                        )
                    
                    obj_mascota.energia = 0
                    obj_mascota.limpieza = 0
                    obj_mascota.hambre = 100
                    obj_mascota.felicidad = 0
                    obj_mascota.social = 0
                    obj_mascota.estado = 'Morido'

                elif diferencia_tiempo >= timedelta(seconds=PRIMER_CAMBIO_SEGUNDOS):

                    self.actualizar(
                        nombre=nombre_mascota, 
                        energia=dict_mascota["energia"]-(CAMBIO_VALORES_SEGUNDOS["energia"]*intervalo_segundos),
                        limpieza=dict_mascota["limpieza"]-(CAMBIO_VALORES_SEGUNDOS["limpieza"]*intervalo_segundos), 
                        hambre=dict_mascota["hambre"]+(CAMBIO_VALORES_SEGUNDOS["hambre"]*intervalo_segundos),
                        felicidad=dict_mascota["felicidad"]-(CAMBIO_VALORES_SEGUNDOS["felicidad"]*intervalo_segundos),
                        social=dict_mascota["social"]-(CAMBIO_VALORES_SEGUNDOS["social"]*intervalo_segundos)
                        )
                    
                    obj_mascota.energia -= (CAMBIO_VALORES_SEGUNDOS["energia"]*intervalo_segundos)
                    obj_mascota.limpieza -= (CAMBIO_VALORES_SEGUNDOS["limpieza"]*intervalo_segundos)
                    obj_mascota.hambre += (CAMBIO_VALORES_SEGUNDOS["hambre"]*intervalo_segundos)
                    obj_mascota.felicidad -= (CAMBIO_VALORES_SEGUNDOS["felicidad"]*intervalo_segundos)
                    obj_mascota.social -= (CAMBIO_VALORES_SEGUNDOS["social"]*intervalo_segundos)

            except Exception as error:
                log(error)

    @property
    def mascota(self):
        return self._mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self._mascota = mascota
    