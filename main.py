# from src.view.game import Game


# if __name__ == '__main__':
#     game = Game()
#     game.run()

from src.view.vista import VentanaRegistro
from tkinter import Tk

if __name__ == "__main__":
    vista = VentanaRegistro(Tk())
    vista.root.mainloop()