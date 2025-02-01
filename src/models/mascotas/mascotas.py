
class Mascota:
    def __init__(self, nombre_mascota, nombre_dueño, tipo):
        self._dueño = nombre_dueño
        self._nombre = nombre_mascota
        self._tipo = tipo
        self._energia = 50
        self._limpieza = 50
        self._hambre = 50
        self._felicidad = 50

    @property
    def nombre_dueño(self):
        return self._dueño
    
    @nombre_dueño.setter
    def nombre_dueño(self, nombre_dueño):
        self._dueño = nombre_dueño

    @property
    def nombre_mascota(self):
        return self._nombre
    
    @nombre_mascota.setter
    def nombre_mascota(self, nombre_mascota):
        self.nombre = nombre_mascota
    
    @property
    def tipo_de_mascota(self):
        return self._tipo
    
    @tipo_de_mascota.setter
    def tipo_de_mascota(self, tipo):
        self._tipo = tipo
    
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, valor):
        self._energia = valor

        if self.energia < 50:
            self.felicidad -= 25
        elif self.energia > 50:
            self.felicidad += 25
        elif self.energia == 100:
            self.felicidad = 100

        if self.energia < 0:
            self._energia = 0
        elif self.energia > 100:
            self._energia = 100

    @property
    def limpieza(self):
        return self._limpieza

    @limpieza.setter
    def limpieza(self, valor):
        self._limpieza = valor

        if self.limpieza < 50:
            self.felicidad -= 25
        elif self.limpieza > 50:
            self.felicidad += 25

        if self.limpieza < 0:
            self._limpieza = 0
        elif self.limpieza > 100:
            self._limpieza = 100

    @property
    def hambre(self):
        return self._hambre
    
    @hambre.setter
    def hambre(self, valor):
        self._hambre = valor
        
        if self.hambre < 50:
            self.felicidad -= 25
        elif self.hambre > 50:
            self.felicidad += 25

        if self.hambre < 0:
            self._hambre = 0
        elif self.hambre > 100:
            self._hambre = 100

    @property
    def felicidad(self):
        return self._felicidad

    @felicidad.setter
    def felicidad(self, valor):
        self._felicidad = valor

        if self.felicidad < 0:
            self._felicidad = 0
        elif self.felicidad > 100:
            self._felicidad = 100


class Perro(Mascota):
    def __init__(self, nombre_dueño, nombre_mascota, tipo='perro'):
        super().__init__(nombre_dueño, nombre_mascota, tipo)

    
class Gato(Mascota):
    def __init__(self, nombre_dueño, nombre_mascota, tipo='gato'):
        super().__init__(nombre_dueño, nombre_mascota, tipo)