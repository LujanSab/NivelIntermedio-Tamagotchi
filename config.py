from dataclasses import dataclass
import pygame
from src.controller.utils import scale_img
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE_NAME = 'tamagochi.db'

ASSETS_UTL = f'{BASE_DIR}//assets'

FPS = 60

@dataclass
class Config:

    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 1500

    MASCOTA_SCALE = 4.0
    dog_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//perro//PERRO1.png')
    DOG_IMAGE = scale_img(dog_img, MASCOTA_SCALE)
    MASCOTA_WIDTH = DOG_IMAGE.get_width()
    MASCOTA_HEIGHT = DOG_IMAGE.get_height()

    hambre_emote = pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//HAMBRE1.png')
    HAMBRE_IMG = scale_img(hambre_emote, 1.8)

    BTN_LIMPIAR_WIDTH = 150
    BTN_LIMPIAR_HEIGHT = 50
