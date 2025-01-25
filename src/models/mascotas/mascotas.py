class Mascota:
    def __init__(self, nombre_dueño, nombre_mascota):
        self.dueño = nombre_dueño
        self.nombre = nombre_mascota
        self.limpieza = 50
        self.hambre = 50
        self.felicidad = 50

    def limpiarse(self):
        pass

    def comer(self):
        pass

    def jugar(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre_dueño, nombre_perro):
        super().__init__(nombre_dueño, nombre_perro)
        self.tipo = "Perro"

class Hamster(Mascota):
    def __init__(self, nombre_dueño, nombre_hamster):
        super().__init__(nombre_dueño, nombre_hamster)
        self.tipo = "Hamster"