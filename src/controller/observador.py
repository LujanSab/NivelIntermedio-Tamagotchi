class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        if obj in self._observadores:
            self._observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)

class Observador:
    def update(self, *args):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Aquí están los parámetros: ", args)