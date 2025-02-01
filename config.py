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

    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1300

    MASCOTA_SCALE = 4.0
    dog_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//perro//PERRO1.png')
    DOG_IMAGE = scale_img(dog_img, MASCOTA_SCALE)
    MASCOTA_WIDTH = DOG_IMAGE.get_width()
    MASCOTA_HEIGHT = DOG_IMAGE.get_height()

    dormir_emote = pygame.image.load(f'{ASSETS_UTL}//emotes//durmiendo//DORMIR1.png')
    DORMIR_IMG = scale_img(dormir_emote, 1.8)

    feliz_emote = pygame.image.load(f'{ASSETS_UTL}//emotes//felicidad//FELICIDAD1.png')
    FELIZ_IMG = scale_img(feliz_emote, 1.8)

    hambre_emote = pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//HAMBRE1.png')
    HAMBRE_IMG = scale_img(hambre_emote, 1.8)

    limpiar_emote = pygame.image.load(f'{ASSETS_UTL}//emotes//limpiar//LIMPIAR1.png')
    LIMPIAR_IMG = scale_img(limpiar_emote, 1.8)

    BTN_WIDTH = 150
    BTN_HEIGHT = 50
