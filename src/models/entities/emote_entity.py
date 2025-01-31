import pygame
from config import Config


class EmoteEntity:
    def __init__(self, animaciones, window):
        self.window = window
        self.forma = pygame.Rect((Config.WINDOW_WIDTH/2)-(Config.MASCOTA_WIDTH/2), (Config.WINDOW_HEIGHT/2) - Config.MASCOTA_HEIGHT, 29, 30)
        self.imagen: pygame.Surface = None
        self.animaciones = animaciones
        self.animation_index = 0
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.estado_actual = None


    def cambiar_estado(self, estado: int):
        """
        Cambia el estado de la animación.
        """
        self.estado_actual = estado
        self.animation_index = 0
        self.actualizar_tiempo = pygame.time.get_ticks()

    
    def actualizar(self):
        """
        Llama a la animación actual en cada fotograma.
        """
        if self.estado_actual != None:
            cooldown_animation = 150
            animacion = self.animaciones[self.estado_actual]

            if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
                self.animation_index = (self.animation_index + 1) % len(animacion)
                self.actualizar_tiempo = pygame.time.get_ticks()

            self.imagen = animacion[self.animation_index]

            self.dibujar()

    # def dormir(self):
    #     '''
    #     logica de animacion de emote durmiendo
    #     '''
    #     self.dibujar()

    #     cooldown_animation = 50

    #     if self.animation_index >= len(self.animaciones[0]):
    #         self.animation_index = 0
        
    #     self.imagen = self.animaciones[0][self.animation_index]
        
    #     if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
    #         self.animation_index += 1
    #         self.actualizar_tiempo = pygame.time.get_ticks()
    
    # def feliz(self):
    #     '''
    #     logica de animacion de emote feliz
    #     '''
    #     self.dibujar()

    #     cooldown_animation = 50

    #     if self.animation_index >= len(self.animaciones[1]):
    #         self.animation_index = 0
        
    #     self.imagen = self.animaciones[1][self.animation_index]
        
    #     if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
    #         self.animation_index += 1
    #         self.actualizar_tiempo = pygame.time.get_ticks()

    # def hambre(self):
    #     '''
    #     logica de animacion de emote hambre
    #     '''
    #     self.dibujar()

    #     cooldown_animation = 50

    #     if self.animation_index >= len(self.animaciones[2]):
    #         self.animation_index = 0
        
    #     self.imagen = self.animaciones[2][self.animation_index]
        
    #     if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
    #         self.animation_index += 1
    #         self.actualizar_tiempo = pygame.time.get_ticks()

    # def limpiar(self):
    #     '''
    #     logica de animacion de emote limpiar
    #     '''
    #     self.dibujar()

    #     cooldown_animation = 50

    #     if self.animation_index >= len(self.animaciones[3]):
    #         self.animation_index = 0
        
    #     self.imagen = self.animaciones[3][self.animation_index]
        
    #     if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
    #         self.animation_index += 1
    #         self.actualizar_tiempo = pygame.time.get_ticks()

    def dibujar(self):
        if self.estado_actual != None:
            self.window.blit(self.imagen, self.forma)
    
    


    