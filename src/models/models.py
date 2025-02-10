from peewee import *


db = SqliteDatabase('tamagochi.db')

class Mascota(Model):
    duenio = CharField()
    nombre = CharField(unique=True)
    tipo = CharField()
    energia = IntegerField(default=50)
    limpieza = IntegerField(default=50)
    hambre = IntegerField(default=50)
    felicidad = IntegerField(default=50)

    def __str__(self):
        return f'{self.nombre} de {self.duenio}'
    
    class Meta:
        database = db

db.connect()
db.create_tables([Mascota])