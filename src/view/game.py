import pygame
from src.config import Styles
from src.models.entities.mascotas_entity import PerroEntity
from src.controller.utils import scale_img


def main():
    pygame.init()

    window = pygame.display.set_mode((Styles.WINDOW_WIDTH, Styles.WINDOW_HEIGHT))
    window.fill((200,200,200))

    animaciones = [
        Styles.DOG_IMAGE
    ]
    
    dog_image = Styles.DOG_IMAGE

    firulais = PerroEntity(
                x=(Styles.WINDOW_WIDTH/2), 
                y=Styles.WINDOW_HEIGHT/2, 
                imagen=dog_image, 
                animaciones=animaciones, 
                nombre_dueño='emi', 
                nombre_mascota='luna'
            )

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        firulais.dibujar(window=window)

        pygame.display.update()

    pygame.quit()

