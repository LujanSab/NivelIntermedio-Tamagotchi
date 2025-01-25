from dataclasses import dataclass
import pygame
from src.controller.utils import scale_img

@dataclass
class Styles:

    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 1500

    MASCOTA_SCALE = 4.0
    dog_img = pygame.image.load('assets//dog.png')
    DOG_IMAGE = scale_img(dog_img, MASCOTA_SCALE)
    MASCOTA_WIDTH = DOG_IMAGE.get_width()
    MASCOTA_HEIGHT = DOG_IMAGE.get_height()
