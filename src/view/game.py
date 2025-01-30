import pygame
from config import Config
from config import ASSETS_UTL
from src.models.entities.mascotas_entity import PerroEntity
from src.models.mascotas.mascotas import Perro
from src.models.mascotas.mascotaService import MascotaService
from src.controller.utils import scale_img
from src.controller.logger import log
import traceback


def main():
    pygame.init()

    window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    window.fill((200,200,200))

    boton_limpiar = pygame.Rect(
        (Config.WINDOW_WIDTH - Config.BTN_LIMPIAR_WIDTH) - 30,
        (Config.WINDOW_HEIGHT - Config.BTN_LIMPIAR_HEIGHT) - 30,
        Config.BTN_LIMPIAR_WIDTH,
        Config.BTN_LIMPIAR_HEIGHT
    )

    boton_alimentar = pygame.Rect(
        (Config.WINDOW_WIDTH - Config.BTN_LIMPIAR_WIDTH) - 30,
        30,
        Config.BTN_LIMPIAR_WIDTH,
        Config.BTN_LIMPIAR_HEIGHT
    )

    boton_dormir = pygame.Rect(
        30,
        (Config.WINDOW_HEIGHT - Config.BTN_LIMPIAR_HEIGHT) - 30,
        Config.BTN_LIMPIAR_WIDTH,
        Config.BTN_LIMPIAR_HEIGHT
    )
    
    fuente = pygame.font.Font(None,30)

    texto_limpiar = fuente.render('Limpiar', True, (255,255,255))
    texto_alimentar = fuente.render('Alimentar', True, (255,255,255))
    texto_dormir = fuente.render('Dormir', True, (255,255,255))

    hambre_emote = []

    for i in range(2):
        hambre_emote.append(Config.HAMBRE_IMG)

    animaciones_mascotas = [
        Config.DOG_IMAGE,
    ]

    animaciones_emotes = [
        hambre_emote,
    ]
    
    dog_image = Config.DOG_IMAGE

    firu_entity = PerroEntity(
                    x=(Config.WINDOW_WIDTH/2), 
                    y=Config.WINDOW_HEIGHT/2, 
                    imagen=dog_image, 
                    animaciones=animaciones_mascotas, 
                )
    
    firu = Perro(nombre_dueño='emi', nombre_mascota='firu', tipo='perro')
    
    firu_servicio = MascotaService(firu)
    perro_dict = firu_servicio.obtener_datos_mascota()

    if not perro_dict:
        firu_servicio.crear()
    else:
        firu = Perro(nombre_mascota=perro_dict['nombre_mascota'], nombre_dueño=perro_dict['nombre_dueño'], tipo=perro_dict['tipo'])

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
                    if boton_limpiar.collidepoint(pygame.mouse.get_pos()):
                        firu.hambre += 25
                        firu_servicio.actualizar(limpieza=firu.limpieza)
                        print('limpiar')
                        # firu_entity.limpiar()
                    elif boton_alimentar.collidepoint(pygame.mouse.get_pos()):
                        firu.hambre -= 25
                        firu_servicio.actualizar(hambre=firu.hambre)
                        print('alimentar')
                        firu_entity.comer()
                    elif boton_dormir.collidepoint(pygame.mouse.get_pos()):
                        firu.energia += 25
                        firu_servicio.actualizar(energia=firu.energia)
                        print('dormir')
                        # firu_entity.comer()
            
            firu_entity.dibujar(window=window)

            pygame.draw.rect(window, (0,0,0), boton_limpiar)
            pygame.draw.rect(window, (0,0,0), boton_alimentar)
            pygame.draw.rect(window, (0,0,0), boton_dormir)

            window.blit(texto_limpiar, (boton_limpiar.x + (boton_limpiar.width - texto_limpiar.get_width())/2, boton_limpiar.y + (boton_limpiar.height - texto_limpiar.get_height())/2))
            window.blit(texto_alimentar, (boton_alimentar.x + (boton_alimentar.width - texto_alimentar.get_width())/2, boton_alimentar.y + (boton_alimentar.height - texto_alimentar.get_height())/2))
            window.blit(texto_dormir, (boton_dormir.x + (boton_dormir.width - texto_dormir.get_width())/2, boton_dormir.y + (boton_dormir.height - texto_dormir.get_height())/2))

            pygame.display.update()

        except:
            log(f'{__file__} - {traceback.format_exc()}')
            run = False

    pygame.quit()

