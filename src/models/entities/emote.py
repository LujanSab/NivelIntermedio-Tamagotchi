import pygame
from config import Config


class Emote:
    def __init__(self, img, animaciones):
        self.forma = pygame.Rect((Config.WINDOW_WIDTH/2)-(Config.MASCOTA_WIDTH/2), Config.WINDOW_HEIGHT/2, 29*1.8, 30*1.8)
        self.imagen = img
        self.animaciones = animaciones