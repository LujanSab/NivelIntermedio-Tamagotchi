import pygame

from config import Config
from config import ASSETS_UTL

from src.models.entities.mascotas_entity import PerroEntity
from src.models.entities.emote_entity import EmoteEntity
from src.models.mascotas.mascotas import Perro
from src.models.mascotas.mascotaService import MascotaService

from src.controller.utils import scale_img
from src.controller.logger import log

import traceback


class Game:

    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.window.fill((200,200,200))

        self.boton_limpiar = pygame.Rect(
            (Config.WINDOW_WIDTH - Config.BTN_WIDTH) - 30,
            (Config.WINDOW_HEIGHT - Config.BTN_HEIGHT) - 30,
            Config.BTN_WIDTH,
            Config.BTN_HEIGHT
        )

        self.boton_alimentar = pygame.Rect(
            (Config.WINDOW_WIDTH - Config.BTN_WIDTH) - 30,
            30,
            Config.BTN_WIDTH,
            Config.BTN_HEIGHT
        )

        self.boton_dormir = pygame.Rect(
            30,
            (Config.WINDOW_HEIGHT - Config.BTN_HEIGHT) - 30,
            Config.BTN_WIDTH,
            Config.BTN_BOTON_HEIGHT
        )

        self.boton_admin = pygame.Rect(
            30,
            30,
            Config.BTN_WIDTH,
            Config.BTN_HEIGHT
        )

        self.fuente = pygame.font.Font(None,30)

        self.texto_limpiar = self.fuente.render('Limpiar', True, (255,255,255))
        self.texto_alimentar = self.fuente.render('Alimentar', True, (255,255,255))
        self.texto_dormir = self.fuente.render('Dormir', True, (255,255,255))

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
        
        self.firu = Perro(nombre_dueño='emi', nombre_mascota='firu', tipo='perro')
        
        self.firu_servicio = MascotaService(self.firu)
        self.perro_dict = self.firu_servicio.obtener_datos_mascota()

        if not self.perro_dict:
            self.firu_servicio.crear()
        else:
            self.firu = Perro(nombre_mascota=self.perro_dict['nombre_mascota'], nombre_dueño=self.perro_dict['nombre_dueño'], tipo=self.perro_dict['tipo'])

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
                        if self.boton_limpiar.collidepoint(pygame.mouse.get_pos()):
                            self.firu.limpieza += 25
                            self.firu_servicio.actualizar(limpieza=self.firu.limpieza)
                            print('limpiar')
                            self.emote_entity.iniciar_animacion('limpiar')

                        elif self.boton_alimentar.collidepoint(pygame.mouse.get_pos()):
                            self.firu.hambre -= 25
                            self.firu_servicio.actualizar(hambre=self.firu.hambre)
                            print('alimentar')
                            self.emote_entity.iniciar_animacion('hambre')

                        elif self.boton_dormir.collidepoint(pygame.mouse.get_pos()):
                            self.firu.energia += 25
                            self.firu_servicio.actualizar(energia=self.firu.energia)
                            print('dormir')
                            self.emote_entity.iniciar_animacion('dormir')
                
                self.window.fill((200, 200, 200))
                
                self.firu_entity.dibujar(window=self.window)
                self.emote_entity.actualizar_animacion()

                pygame.draw.rect(self.window, (0,0,0), self.boton_limpiar)
                pygame.draw.rect(self.window, (0,0,0), self.boton_alimentar)
                pygame.draw.rect(self.window, (0,0,0), self.boton_dormir)

                self.window.blit(self.texto_limpiar, (self.boton_limpiar.x + (self.boton_limpiar.width - self.texto_limpiar.get_width())/2, self.boton_limpiar.y + (self.boton_limpiar.height - self.texto_limpiar.get_height())/2))
                self.window.blit(self.texto_alimentar, (self.boton_alimentar.x + (self.boton_alimentar.width - self.texto_alimentar.get_width())/2, self.boton_alimentar.y + (self.boton_alimentar.height - self.texto_alimentar.get_height())/2))
                self.window.blit(self.texto_dormir, (self.boton_dormir.x + (self.boton_dormir.width - self.texto_dormir.get_width())/2, self.boton_dormir.y + (self.boton_dormir.height - self.texto_dormir.get_height())/2))

                pygame.display.update()

            except:
                log(f'{__file__} - {traceback.format_exc()}')
                run = False

        pygame.quit()

