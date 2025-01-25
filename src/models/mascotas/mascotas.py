from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, nombre_dueño, nombre_mascota, tipo):
        self.dueño = nombre_dueño
        self.nombre = nombre_mascota
        self.tipo = tipo
        self.limpieza = 50
        self.hambre = 50
        self.felicidad = 50

    @property
    @abstractmethod
    def nombre_dueño(self):
        return self.dueño
    
    @nombre_dueño.setter
    @abstractmethod
    def set_nombre_dueño(self, nombre_dueño):
        self.dueño = nombre_dueño

    @property
    @abstractmethod
    def nombre_mascota(self):
        return self.nombre
    
    @nombre_mascota.setter
    @abstractmethod
    def set_nombre_mascota(self, nombre_mascota):
        self.nombre = nombre_mascota
    
    @property
    @abstractmethod
    def tipo_de_mascota(self):
        return self.tipo
    
    @tipo_de_mascota.setter
    @abstractmethod
    def set_tipo_de_mascota(self, tipo):
        self.tipo = tipo
    
    @abstractmethod
    def limpiarse(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def jugar(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre_dueño, nombre_perro, tipo):
        super().__init__(nombre_dueño, nombre_perro, tipo)

    def ladrar(self):
        pass
    
class Gato(Mascota):
    def __init__(self, nombre_dueño, nombre_gato):
        super().__init__(nombre_dueño, nombre_gato)

    def maullar(self):
        pass