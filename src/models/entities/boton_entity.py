# Aca se encuentra la logica de entidad para los botones
import pygame
from config import Config


class BotonEntity:
    """
    El código define una clase BotonEntity para crear botones en una ventana de Pygame con métodos para
    inicializar y dibujar el botón.

    :param color: El parámetro `color` en el método `dibujar` representa el color que se
    usará para dibujar la entidad del botón en la pantalla. Debe ser una tupla que contenga valores RGB, por ejemplo, `(255, 0, 0)` para rojo, `(0, 255,
    :type color: tuple
    """
    def __init__(self, x, y, texto, ventana):
        self.ventana = ventana
        self.forma = pygame.Rect(x, y, Config.BTN_WIDTH, Config.BTN_HEIGHT)
        self.texto_fuente = pygame.font.Font(None, 30)
        self.texto = self.texto_fuente.render(texto, True, (255,255,255))
    
    def dibujar(self, color: tuple):
        pygame.draw.rect(self.ventana, color, self.forma)
        self.ventana.blit(self.texto, (self.forma.x + (self.forma.width - self.texto.get_width())/2, self.forma.y + (self.forma.height - self.texto.get_height())/2))