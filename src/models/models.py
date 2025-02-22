from peewee import *

db = SqliteDatabase('tamagochi.db')

class Mascotas(Model):
    duenio = CharField()
    nombre = CharField(unique=True)
    tipo = CharField()
    energia = IntegerField(default=50)
    limpieza = IntegerField(default=50)
    hambre = IntegerField(default=50)
    felicidad = IntegerField(default=50)
    estado = CharField(default='Sano')
    ultima_actualizacion = CharField()

    def __str__(self):
        return f'{self.nombre}, {self.duenio}, {self.tipo}, {self.energia}, {self.limpieza}, {self.hambre}, {self.felicidad}, {self.ultima_actualizacion}'

    class Meta:
        database = db

db.connect()
db.create_tables([Mascotas])