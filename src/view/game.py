import pygame
from src.config import Styles
from src.models.entities.mascotas_entity import PerroEntity
from src.models.mascotas.mascotas import Perro
from src.models.mascotas.mascotaService import MascotaService
from src.controller.utils import scale_img
from src.controller.logger import log
import traceback


def main():
    pygame.init()

    window = pygame.display.set_mode((Styles.WINDOW_WIDTH, Styles.WINDOW_HEIGHT))
    window.fill((200,200,200))

    boton_limpiar = pygame.Rect(
        (Styles.WINDOW_WIDTH - Styles.BTN_LIMPIAR_WIDTH) - 30,
        (Styles.WINDOW_HEIGHT - Styles.BTN_LIMPIAR_HEIGHT) - 30,
        Styles.BTN_LIMPIAR_WIDTH,
        Styles.BTN_LIMPIAR_HEIGHT
    )

    boton_alimentar = pygame.Rect(
        (Styles.WINDOW_WIDTH - Styles.BTN_LIMPIAR_WIDTH) - 30,
        30,
        Styles.BTN_LIMPIAR_WIDTH,
        Styles.BTN_LIMPIAR_HEIGHT
    )

    boton_dormir = pygame.Rect(
        30,
        (Styles.WINDOW_HEIGHT - Styles.BTN_LIMPIAR_HEIGHT) - 30,
        Styles.BTN_LIMPIAR_WIDTH,
        Styles.BTN_LIMPIAR_HEIGHT
    )
    
    fuente = pygame.font.Font(None,30)

    texto_limpiar = fuente.render('Limpiar', True, (255,255,255))
    texto_alimentar = fuente.render('Alimentar', True, (255,255,255))
    texto_dormir = fuente.render('Dormir', True, (255,255,255))

    animaciones = [
        Styles.DOG_IMAGE
    ]
    
    dog_image = Styles.DOG_IMAGE

    firu_entity = PerroEntity(
                    x=(Styles.WINDOW_WIDTH/2), 
                    y=Styles.WINDOW_HEIGHT/2, 
                    imagen=dog_image, 
                    animaciones=animaciones, 
                )
    
    firu = Perro(nombre_dueño='emi', nombre_mascota='firu', tipo='perro')
    
    firu_servicio = MascotaService(firu)
    lista = firu_servicio.obtener_por_nombre('firu')
    print(lista)
    if not lista[0]:
        firu_servicio.crear()
    else:
        mi_perro = lista[0]
        firu = Perro(*mi_perro)

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
                        firu.limpieza += 25
                        firu_servicio.actualizar(nombre=firu.nombre, limpieza=firu.limpieza)
                        print('limpiar')
                        # firu_entity.limpiar()
                    elif boton_alimentar.collidepoint(pygame.mouse.get_pos()):
                        firu.hambre -= 25
                        firu_servicio.actualizar(nombre=firu.nombre, hambre=firu.hambre)
                        print('alimentar')
                        # firu_entity.comer()
                    elif boton_dormir.collidepoint(pygame.mouse.get_pos()):
                        firu.energia += 25
                        firu_servicio.actualizar(nombre=firu.nombre, energia=firu.energia)
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
            pygame.quit()

    pygame.quit()

