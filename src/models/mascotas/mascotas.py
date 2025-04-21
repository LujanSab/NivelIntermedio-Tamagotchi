# Este es un modulo dedicado a la logica minima para las mascotas,
# de las que despues va a consumir los datos el ORM 
# para pasarlo a la base de datos
class Mascota:
    """
    La clase `Mascota` en Python define atributos y métodos 
    para gestionar las características de una mascota, 
    como energía, limpieza, hambre, felicidad y estado.
    """
    def __init__(self, nombre_mascota, nombre_dueño, tipo, estado):
        self._dueño = nombre_dueño
        self._nombre = nombre_mascota
        self._tipo = tipo
        self._energia = 50
        self._limpieza = 50
        self._hambre = 50
        self._felicidad = 50
        self._social = 50
        self._estado = estado
        self._ultima_actualizacion: str = ''
        self._block_atributo = False

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
        self._nombre = nombre_mascota
    
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

    @property
    def social(self):
        return self._social

    @social.setter
    def social(self, valor):
        self._social = valor

        if self.social < 0:
            self._social = 0
        elif self.social > 100:
            self._social = 100
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def ultima_actualizacion(self):
        return self._ultima_actualizacion
    
    @ultima_actualizacion.setter
    def ultima_actualizacion(self, ultima_actualizacion):
        self._ultima_actualizacion = ultima_actualizacion

    def jugar(self):
        self.social += 12;
        if (self.social < 100 ):
            if self.social >= 50:
                self.felicidad += 7
                self.limpieza -= 14
                self.hambre -= 11
                self.energia -= 16
            elif self.social < 50:
                self.felicidad += 9
                self.limpieza -= 21
                self.hambre -= 16
                self.energia -= 18

    def alimentar(self):
        self.hambre += 13;
        if (self.social > 0 ):
            if self.hambre >= 50:
                self.felicidad += 2
                self.limpieza -= 15 
            elif self.hambre < 50:
                self.felicidad += 7
                self.limpieza -= 11

    def limpiar(self):
        self.limpieza += 14;
        if (self.limpieza < 100 ):
            if self.limpieza <= 50:
                self.felicidad -= 13
                self.social -= 17
            elif self.limpieza > 50:
                self.felicidad -= 8
                self.social -= 18

    def dormir(self):
        self.energia += 11;
        if (self.energia < 100 ):
            if self.energia >= 50:
                self.felicidad += 7
                self.social -= 11
                self.hambre -= 7
            elif self.energia < 50:
                self.felicidad += 12
                self.social -= 14
                self.hambre -= 11

class Perro(Mascota):
    '''
    Clase que hereda de mascota, con la diferencia que esta es de tipo perro,
    y por lo tanto, tendra sus caracteristicas cuando se llame en otros modulos
    '''
    def __init__(self, nombre_dueño, nombre_mascota, tipo='perro', estado='sano'):
        super().__init__(nombre_dueño, nombre_mascota, tipo, estado)

    
class Gato(Mascota):
    '''
    Clase que hereda de mascota, con la diferencia que esta es de tipo gato,
    y por lo tanto, tendra sus caracteristicas cuando se llame en otros modulos
    '''
    def __init__(self, nombre_dueño, nombre_mascota, tipo='gato', estado='sano'):
        super().__init__(nombre_dueño, nombre_mascota, tipo, estado)