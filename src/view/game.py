import pygame

from config import Config
from config import ASSETS_UTL

from src.models.entities.mascotas_entity import PerroEntity, GatoEntity
from src.models.entities.emote_entity import EmoteEntity
from src.models.entities.boton_entity import BotonEntity
from src.models.mascotas.mascotas import Mascota
from src.models.mascotas.mascotaService import MascotaService

from src.controller.utils import scale_img
from src.controller.logger import log

import traceback


class Game:

    def __init__(self, mascota: Mascota):
        pygame.init()
        self.firu = mascota

        self.window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.window.fill((200,200,200))

        # BOTONES
        self.boton_limpiar = BotonEntity(
            (Config.WINDOW_WIDTH - Config.BTN_WIDTH) - 30,
            (Config.WINDOW_HEIGHT - Config.BTN_HEIGHT) - 30,
            'LIMPIAR',
            self.window
        )

        self.boton_alimentar = BotonEntity(
            x=(Config.WINDOW_WIDTH - Config.BTN_WIDTH) - 30,
            y=30,
            texto='ALIMENTAR',
            ventana=self.window
            )

        self.boton_dormir = BotonEntity(
            30, 
            (Config.WINDOW_HEIGHT - Config.BTN_HEIGHT) - 30,
            'DORMIR',
            self.window
            )

        self.boton_salir = BotonEntity(
            30, 
            30,
            'SALIR',
            self.window
            )

        self.animaciones_mascotas = []

        self.animaciones_emotes = [
            Config.DORMIR_EMOTE,
            Config.FELIZ_EMOTE,
            Config.HAMBRE_EMOTE,
            Config.LIMPIAR_EMOTE
        ]

        self.dog_image = Config.DOG_IMAGE

        if self.firu.tipo_de_mascota == 'perro':
            self.animaciones_mascotas.append(self.dog_image)
            self.firu_entity = PerroEntity(
                            x=(Config.WINDOW_WIDTH/2), 
                            y=Config.WINDOW_HEIGHT/2, 
                            imagen=self.dog_image, 
                            animaciones=self.animaciones_mascotas, 
                        )
        elif self.firu.tipo_de_mascota == 'gato':
            self.animaciones_mascotas.append(Config.GATO_IDLE)
            self.firu_entity = GatoEntity(
                            x=(Config.WINDOW_WIDTH/2), 
                            y=Config.WINDOW_HEIGHT/2, 
                            imagen=self.dog_image, 
                            animaciones=self.animaciones_mascotas, 
                        )
        self.emote_entity = EmoteEntity(
                        animaciones=self.animaciones_emotes,
                        window=self.window
                    )
        
        self.firu_servicio = MascotaService()
        self.firu_servicio.mascota = self.firu

    def run(self):

        run = True

        while run:
            """
            main loop of the game
            """
            self.firu_dict = self.firu_servicio.obtener_datos_mascota(self.firu.nombre_mascota, self.firu.nombre_dueño, self.firu.tipo_de_mascota)

            self.porcentaje_hambre = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*2) + 30,
                f"Hambre {self.firu_dict['hambre']}%",
                self.window
            )

            self.porcentaje_energia = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*3) + 40,
                f"Energia {self.firu_dict['energia']}%",
                self.window
            )

            self.porcentaje_felicidad = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*4) + 50,
                f"Felicidad {self.firu_dict['felicidad']}%",
                self.window
            )

            self.porcentaje_limpieza = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*5) + 60,
                f"Limpieza {self.firu_dict['limpieza']}%",
                self.window
            )

            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.boton_limpiar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.limpieza += 25
                            self.firu_servicio.actualizar(limpieza=self.firu.limpieza, felicidad=self.firu.felicidad, nombre=self.firu.nombre_mascota)
                            print(self.firu.limpieza)
                            self.emote_entity.iniciar_animacion('limpiar')

                        elif self.boton_alimentar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.hambre -= 25
                            self.firu_servicio.actualizar(hambre=self.firu.hambre, felicidad=self.firu.felicidad, nombre=self.firu.nombre_mascota)
                            print(self.firu.hambre)
                            self.emote_entity.iniciar_animacion('hambre')

                        elif self.boton_dormir.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.energia += 25
                            self.firu_servicio.actualizar(energia=self.firu.energia, felicidad=self.firu.felicidad, nombre=self.firu.nombre_mascota)
                            print(self.firu.energia)
                            self.emote_entity.iniciar_animacion('dormir')
                        
                        elif self.boton_salir.forma.collidepoint(pygame.mouse.get_pos()):
                            run = False
                
                self.window.fill((200, 200, 200))
                
                self.firu_entity.dibujar(window=self.window)

                if isinstance(self.firu_entity, GatoEntity):
                    self.firu_entity.idle()

                self.emote_entity.actualizar_animacion()

                self.boton_limpiar.dibujar((0,0,0))
                self.boton_salir.dibujar((0,0,0))
                self.boton_dormir.dibujar((0,0,0))
                self.boton_alimentar.dibujar((0,0,0))

                self.porcentaje_energia.dibujar((150,150,150))
                self.porcentaje_hambre.dibujar((150,150,150))
                self.porcentaje_felicidad.dibujar((150,150,150))
                self.porcentaje_limpieza.dibujar((150,150,150))

                pygame.display.update()

            except:
                log(f'{__file__} - {traceback.format_exc()}')
                run = False

        pygame.quit()