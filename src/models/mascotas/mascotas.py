
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
    def get_nombre_dueño(self):
        return self.dueño
    
    @get_nombre_dueño.setter
    def set_nombre_dueño(self, nombre_dueño):
        self.dueño = nombre_dueño

    @property
    def get_nombre_mascota(self):
        return self.nombre
    
    @get_nombre_mascota.setter
    def set_nombre_mascota(self, nombre_mascota):
        self.nombre = nombre_mascota
    
    @property
    def get_tipo_de_mascota(self):
        return self.tipo
    
    @get_tipo_de_mascota.setter
    def set_tipo_de_mascota(self, tipo):
        self.tipo = tipo
    
    @property
    def get_energia(self):
        return self.energia
    
    @get_energia.setter
    def set_energia(self, valor):
        self.energia += valor

    @property
    def get_limpieza(self):
        return self.limpieza

    @get_limpieza.setter
    def set_limpieza(self, valor):
        self.limpieza += valor

    @property
    def get_hambre(self):
        return self.hambre
    
    @get_hambre.setter
    def set_hambre(self, valor):
        self.hambre += valor

    @property
    def get_felicidad(self):
        return self.felicidad

    @get_felicidad.setter
    def set_felicidad(self, valor):
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