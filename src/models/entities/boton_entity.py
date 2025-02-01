import pygame
from config import Config


class BotonEntity:
    def __init__(self, x, y, texto, ventana):
        self.ventana = ventana
        self.forma = pygame.Rect(x, y, Config.BTN_WIDTH, Config.BTN_HEIGHT)
        self.texto_fuente = pygame.font.Font(None, 30)
        self.texto = self.texto_fuente.render(texto, True, (255,255,255))
    
    def dibujar(self):
        pygame.draw.rect(self.ventana, (0,0,0), self.forma)
        self.ventana.blit(self.texto, (self.forma.x + (self.forma.width - self.texto.get_width())/2, self.forma.y + (self.forma.height - self.texto.get_height())/2))