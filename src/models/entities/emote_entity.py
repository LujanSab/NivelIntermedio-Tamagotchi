import pygame
from config import Config


class EmoteEntity:
    def __init__(self, animaciones):
        self.forma = pygame.Rect((Config.WINDOW_WIDTH/2)-(Config.MASCOTA_WIDTH/2), Config.WINDOW_HEIGHT/2, 29, 30)
        self.imagen: pygame.Surface = None
        self.animaciones = animaciones
        self.animation_index = 0
        self.actualizar_tiempo = pygame.time.get_ticks()

    def comer(self):
        '''
        logica de animacion
        '''
        self.img = Config.HAMBRE_IMG

        cooldown_animation = 50

        if self.animation_index >= len(self.animaciones[0]):
            self.animation_index = 0
        
        self.imagen = self.animaciones[3][self.animation_index]
        
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
            self.animation_index += 1
            self.actualizar_tiempo = pygame.time.get_ticks()
    
    


    