# Dentro de este modulo se colocan todos los modelos de la app
from peewee import *

db = SqliteDatabase('tamagochi.db')

class Mascotas(Model):
    """
    El código define un modelo para mascotas con atributos como dueño, nombre, tipo, nivel de energía,
    limpieza, hambre, felicidad, estado y hora de la última actualización.
    :return: El método `__str__` en el modelo `Mascotas` está devolviendo una cadena formateada
    que contiene los valores de los atributos de la instancia del modelo. El formato es el siguiente:
    """
    duenio = CharField()
    nombre = CharField(unique=True)
    tipo = CharField()
    energia = IntegerField(default=50)
    limpieza = IntegerField(default=50)
    hambre = IntegerField(default=50)
    felicidad = IntegerField(default=50)
    estado = CharField()
    ultima_actualizacion = CharField()

    def __str__(self):
        return f'{self.nombre}, {self.duenio}, {self.tipo}, {self.energia}, {self.limpieza}, {self.hambre}, {self.felicidad}, {self.estado}, {self.ultima_actualizacion}'

    class Meta:
        database = db

db.connect()
db.create_tables([Mascotas])