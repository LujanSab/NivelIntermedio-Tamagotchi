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
    def __init__(self, x, y, imagen, animaciones, nombre_dueño, nombre_mascota, tipo):
        self.forma = pygame.Rect(0, 0, Styles.MASCOTA_WIDTH, Styles.MASCOTA_HEIGHT)
        self.forma.center = (x,y)
        self.imagen = imagen
        self.animaciones = animaciones[0]
        self.actualizar_tiempo = pygame.time.get_ticks()

        self.comer_frame_index = 0
        self.limpiar_frame_index = 0
        self.dormir_frame_index = 0
        
        self.tipo = tipo
        self.dueño = nombre_dueño
        self.nombre = nombre_mascota
        self.limpieza = 50
        self.hambre = 50
        self.felicidad = 50
        self.energia = 50

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
    
    """
    ------------------------------------------------------------------------------------
    GETTERS Y SETTERS
    ------------------------------------------------------------------------------------
    """
    
    @property
    def get_nombre(self):
        return Mascota.get_nombre()

    @get_nombre.setter
    def set_nombre(nombre):
        Mascota.set_nombre_mascota(nombre)
    
    @property
    def get_limpieza(self):
        return Mascota.get_limpieza()

    @get_limpieza.setter
    def set_limpieza(limpieza):
        Mascota.set_limpieza(limpieza)

    @property
    def get_hambre(self):
        return Mascota.get_hambre()

    @get_hambre.setter
    def set_hambre(limpieza):
        Mascota.set_hambre(limpieza)
    
    @property
    def get_felicidad(self):
        return Mascota.get_felicidad()

    @get_felicidad.setter
    def set_felicidad(felicidad):
        Mascota.set_felicidad(felicidad)

    @property
    def get_energia(self):
        return Mascota.get_energia()

    @get_energia.setter
    def set_energia(energia):
        Mascota.set_energia(energia)


class PerroEntity(MascotaEntity):
    """
    Entidad Perro que hereda de MascotaEntity, de tipo 'perro'
    """
    def __init__(self, x, y, imagen, animaciones, nombre_dueño, nombre_mascota, tipo='perro'):
        super().__init__(x, y, imagen, animaciones, nombre_dueño, nombre_mascota, tipo)


class GatoEntity(MascotaEntity):
    """
    Entidad Gato que hereda de MascotaEntity, de tipo 'gato'
    """
    def __init__(self, x, y, imagen, animaciones, nombre_dueño, nombre_mascota, tipo='gato'):
        super().__init__(x, y, imagen, animaciones, nombre_dueño, nombre_mascota, tipo)
