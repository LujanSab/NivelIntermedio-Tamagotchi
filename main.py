# Este fragmento de código Python importa la clase `VentanaRegistro` desde el módulo `vista` dentro del
# paquete `view` ubicado en el directorio `src`. También importa la clase `Tk` desde el
# módulo `tkinter`.
from src.view.vista import VentanaRegistro
from tkinter import Tk

if __name__ == "__main__":
    '''
    Aca dentro se llama a la vista de tkinter, lo que desencadena
    la ejecucion de toda la app
    '''
    vista = VentanaRegistro(Tk())
    vista.root.mainloop()