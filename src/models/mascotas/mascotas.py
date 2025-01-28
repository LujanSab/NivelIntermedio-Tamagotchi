
class Mascota:
    def __init__(self, nombre_dueño, nombre_mascota, tipo):
        self.dueño = nombre_dueño
        self.nombre = nombre_mascota
        self.tipo = tipo
        self.energia = 50
        self.limpieza = 50
        self.hambre = 50
        self.felicidad = 50

    @property
    def nombre_dueño(self):
        return self.dueño
    
    @nombre_dueño.setter
    def nombre_dueño(self, nombre_dueño):
        self.dueño = nombre_dueño

    @property
    def nombre_mascota(self):
        return self.nombre
    
    @nombre_mascota.setter
    def nombre_mascota(self, nombre_mascota):
        self.nombre = nombre_mascota
    
    @property
    def tipo_de_mascota(self):
        return self.tipo
    
    @tipo_de_mascota.setter
    def tipo_de_mascota(self, tipo):
        self.tipo = tipo
    
    @property
    def energia(self):
        return self.energia
    
    @energia.setter
    def energia(self, valor):
        self.energia += valor

    @property
    def limpieza(self):
        return self.limpieza

    @limpieza.setter
    def limpieza(self, valor):
        self.limpieza += valor

    @property
    def hambre(self):
        return self.hambre
    
    @hambre.setter
    def hambre(self, valor):
        self.hambre += valor

    @property
    def felicidad(self):
        return self.felicidad

    @felicidad.setter
    def felicidad(self, valor):
        self.felicidad += valor

class Perro(Mascota):
    def __init__(self, nombre_dueño, nombre_perro, tipo='perro'):
        super().__init__(nombre_dueño, nombre_perro, tipo)

    def ladrar(self):
        pass
    
class Gato(Mascota):
    def __init__(self, nombre_dueño, nombre_mascota, tipo='gato'):
        super().__init__(nombre_dueño, nombre_mascota, tipo)

    def maullar(self):
        pass