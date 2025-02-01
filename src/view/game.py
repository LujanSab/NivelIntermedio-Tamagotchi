import pygame

from config import Config
from config import ASSETS_UTL

from src.models.entities.mascotas_entity import PerroEntity
from src.models.entities.emote_entity import EmoteEntity
from src.models.entities.boton_entity import BotonEntity
from src.models.mascotas.mascotas import Perro
from src.models.mascotas.mascotaService import MascotaService

from src.controller.utils import scale_img
from src.controller.logger import log

import traceback


class Game:

    def __init__(self, mascota):
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

        self.boton_admin = BotonEntity(
            30, 
            30,
            'ADMIN',
            self.window
            )

        self.dormir_emote = []
        self.feliz_emote = []
        self.hambre_emote = []
        self.limpiar_emote = []

        for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//durmiendo//DORMIR{i+1}.png'), 1.8)
            self.dormir_emote.append(new_img)

        for i in range(3):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//felicidad//FELICIDAD{i+1}.png'), 1.8)
            self.feliz_emote.append(new_img)

        for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//HAMBRE{i+1}.png'), 1.8)
            self.hambre_emote.append(new_img)

        for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//limpiar//LIMPIAR{i+1}.png'), 1.8)
            self.limpiar_emote.append(new_img)

        self.animaciones_mascotas = [
            Config.DOG_IMAGE,
        ]

        self.animaciones_emotes = [
            self.dormir_emote,
            self.feliz_emote,
            self.hambre_emote,
            self.limpiar_emote
        ]

        self.dog_image = Config.DOG_IMAGE

        self.firu_entity = PerroEntity(
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
        self.firu_servicio._mascota = self.firu

        self.porcentaje_hambre = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
            (Config.BTN_HEIGHT*2) + 30,
            'Hambre 100%',
            self.window
        )

        self.porcentaje_energia = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
            (Config.BTN_HEIGHT*3) + 40,
            'Energia 100%',
            self.window
        )

        self.porcentaje_felicidad = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
            (Config.BTN_HEIGHT*4) + 50,
            'Felicidad 100%',
            self.window
        )

        self.porcentaje_limpieza = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
            (Config.BTN_HEIGHT*5) + 60,
            'Limpieza 100%',
            self.window
        )

    def run(self):

        run = True

        while run:
            """
            main loop of the game
            """
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.boton_limpiar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.limpieza += 25
                            self.firu_servicio.actualizar(limpieza=self.firu.limpieza, nombre=self.firu.nombre_mascota)
                            print(self.firu.limpieza)
                            self.emote_entity.iniciar_animacion('limpiar')

                        elif self.boton_alimentar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.hambre -= 25
                            self.firu_servicio.actualizar(hambre=self.firu.hambre, nombre=self.firu.nombre_mascota)
                            print(self.firu.hambre)
                            self.emote_entity.iniciar_animacion('hambre')

                        elif self.boton_dormir.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.energia += 25
                            self.firu_servicio.actualizar(energia=self.firu.energia, nombre=self.firu.nombre_mascota)
                            print(self.firu.energia)
                            self.emote_entity.iniciar_animacion('dormir')
                
                self.window.fill((200, 200, 200))
                
                self.firu_entity.dibujar(window=self.window)
                self.emote_entity.actualizar_animacion()

                self.boton_limpiar.dibujar((0,0,0))
                self.boton_admin.dibujar((0,0,0))
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