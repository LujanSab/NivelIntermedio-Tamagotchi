class Sujeto:
    """
    Clase Sujeto del patrón Observer.

    Mantiene una lista de observadores y les envía notificaciones cuando ocurre un evento.
    Métodos:
    - agregar(obj): Agrega un observador a la lista.
    - quitar(obj): Elimina un observador de la lista si está presente.
    - notificar(*args): Llama al método 'update' de todos los observadores registrados, pasándoles los argumentos.
    """
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
    """
    Clase base para observadores.

    Define la interfaz común que todos los observadores deben implementar.
    """
    def update(self, *args):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverA(Observador):
    """
    Observador concreto que reacciona a las notificaciones del sujeto.

    Al instanciarse, se registra automáticamente en el sujeto como parámetro.
    """
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Aquí están los parámetros: ", args)