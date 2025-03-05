# Aca se encuentra la logica de entidad para los emoticones
import pygame
from config import Config


class EmoteEntity:
    """
    La clase `EmoteEntity` en Python define métodos para controlar y mostrar animaciones para un
    personaje en una ventana usando Pygame.

    :param tipo_animacion: El parámetro `tipo_animacion` en el método `iniciar_animacion` de la
    clase `EmoteEntity` se usa para especificar el tipo de animación que se debe iniciar. Es un
    parámetro de cadena que puede tener valores como "dormir", "feliz", "hambre", etc...
    """
    def __init__(self, animaciones, window):
        self.window = window
        self.forma = pygame.Rect(
            (Config.WINDOW_WIDTH/2),
            (Config.WINDOW_HEIGHT/2) - (Config.MASCOTA_HEIGHT-20), 
            29, 
            30)
        self.imagen: pygame.Surface = None
        self.animaciones = animaciones
        self.animation_index = 0
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.animacion_activa = False
        self.tiempo_inicio = 0


    def iniciar_animacion(self, tipo_animacion):
        """
        Inicia una animación y establece el tiempo de inicio
        """
        self.animation_index = 0
        self.animacion_activa = True
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tipo_animacion = tipo_animacion
    

    def actualizar_animacion(self):
        """
        Controla la duración de la animación y la reproduce si está activa
        """
        if not self.animacion_activa:
            return
        
        # Detener animación si han pasado 2 segundos
        if pygame.time.get_ticks() - self.tiempo_inicio >= 2000:
            self.animacion_activa = False
            return
        
        cooldown_animation = 250

        if self.tipo_animacion == "dormir":
            animacion = self.animaciones[0]
        elif self.tipo_animacion == "feliz":
            animacion = self.animaciones[1]
        elif self.tipo_animacion == "hambre":
            animacion = self.animaciones[2]
        elif self.tipo_animacion == "limpiar":
            animacion = self.animaciones[3]
        elif self.tipo_animacion == "jugar":
            animacion = self.animaciones[4]
        else:
            return
        
        if self.animation_index >= len(animacion):
            self.animation_index = 0
        
        self.imagen = animacion[self.animation_index]

        self.dibujar()
        
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
            self.animation_index += 1
            self.actualizar_tiempo = pygame.time.get_ticks()

    def dibujar(self):
        if self.animacion_activa and self.imagen:
            self.window.blit(self.imagen, self.forma)
    
    


    