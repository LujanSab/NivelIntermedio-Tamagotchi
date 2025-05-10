# Este fragmento de código Python importa la clase `VentanaRegistro` desde el módulo `vista` dentro del
# paquete `view` ubicado en el directorio `src`. También importa la clase `Tk` desde el
# módulo `tkinter`.
from src.view.vista import VentanaRegistro
from tkinter import Tk
from src.controller import observador

class Controller:
    """
    Está es la clase principal
    """
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = VentanaRegistro(self.root_controler)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.service)


if __name__ == "__main__":
    '''
    Aca dentro se llama a la vista de tkinter, lo que desencadena
    la ejecucion de toda la app
    '''

    application = Controller(Tk())
    application.root_controler.mainloop()
