import pygame
from abc import ABC, abstractmethod
from src.config import Styles
from src.models.mascotas.mascotas import Mascota


class MascotaEntity:
    """
    MascotaEntity es una clase abstracta que se ocupa de crear los metodos y definir
    los atributos de las entidades hijas

    parametros:
    ----------
        - x: se encarga de definir la posicion de la entidad en el eje x
        - y: se encarga de definir la posicion de la entidad en el eje y
        - imagen: define la imagen de la entidad con la que se va a renderizar
        - animaciones: una lista de listas con las animaciones:
            indices:
            -------
                - 0 es quieto
                - 1 es limpiando
                - 2 es comiendo
                - 3 es durmiendo
        - nombre_dueño: nombre del usuario dueño
        - nombre_mascota: nombre de la mascota
        - tipo: tipo de mascota, perro o gato

    metodos:
    -------
        - limpiar: se encarga de ejecutar la animacion para la limpieza
        - comer: se encarga de ejecutar la animacion para comer
        - dormir: se encarga de ejecutar la animacion para dormir
        - getters: encargados de devolver la informacion de la mascota a la vista
        - setters: encargados de enviar informacion a la clase Mascota para almacenarla en la base de datos
    """
    def __init__(self, x, y, imagen, animaciones):
        self.forma = pygame.Rect(0, 0, Styles.MASCOTA_WIDTH, Styles.MASCOTA_HEIGHT)
        self.forma.center = (x,y)
        self.imagen = imagen
        self.animaciones = animaciones[0]
        self.actualizar_tiempo = pygame.time.get_ticks()

        self.comer_frame_index = 0
        self.limpiar_frame_index = 0
        self.dormir_frame_index = 0

    """
    ------------------------------------------------------------------------------------
    METODOS
    ------------------------------------------------------------------------------------
    """

    def dibujar(self, window):
        '''
        funcion para dibujar la mascota en la pantalla
        '''
        window.blit(self.imagen, self.forma)
        pygame.draw.rect(window, (255,255,255), self.forma, width=1)

    def limpiar(self):
        '''
        logica de animacion de limpieza
        '''
        cooldown_animation = 50

        if self.comer_frame_index >= len(self.animaciones[2]):
            self.comer_frame_index = 0
        
        self.imagen = self.animaciones[1][self.comer_frame_index]
        
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
            self.comer_frame_index += 1
            self.actualizar_tiempo = pygame.time.get_ticks()
    
    def comer(self):
        '''
        logica de animacion de comer
        '''
        cooldown_animation = 50

        if self.comer_frame_index >= len(self.animaciones[2]):
            self.comer_frame_index = 0
        
        self.imagen = self.animaciones[2][self.comer_frame_index]
        
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
            self.comer_frame_index += 1
            self.actualizar_tiempo = pygame.time.get_ticks()
    
    def dormir(self):
        '''
        logica de animacion de dormir
        '''
        cooldown_animation = 50

        if self.comer_frame_index >= len(self.animaciones[2]):
            self.comer_frame_index = 0
        
        self.imagen = self.animaciones[3][self.comer_frame_index]
        
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animation:
            self.comer_frame_index += 1
            self.actualizar_tiempo = pygame.time.get_ticks()
    
    
class PerroEntity(MascotaEntity):
    """
    Entidad Perro que hereda de MascotaEntity, de tipo 'perro'
    """
    def __init__(self, x, y, imagen, animaciones):
        super().__init__(x, y, imagen, animaciones)


class GatoEntity(MascotaEntity):
    """
    Entidad Gato que hereda de MascotaEntity, de tipo 'gato'
    """
    def __init__(self, x, y, imagen, animaciones):
        super().__init__(x, y, imagen, animaciones)
