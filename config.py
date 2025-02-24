# Este fragmento de código define una clase `Config` usando una clase de datos en Python. Contiene varios
# valores constantes relacionados con un juego, como dimensiones de ventana, escalas de imagen, rutas de imagen y
# dimensiones de botón. Además, carga imágenes usando pygame y las escala usando una función `scale_img`
# importacion desde `src.controller.utils`.
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
    '''
    Dataclass Config construida para almacenar constantes sobre el juego
    '''
    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1300

    PERRO_SCALE = 4.0
    GATO_SCALE = 3.0

    _dog_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//perro//PERRO1.png')
    DOG_IMAGE = scale_img(_dog_img, PERRO_SCALE)

    _cat_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//gato//GATO1.png')
    CAT_IMG = scale_img(_cat_img, GATO_SCALE)

    MASCOTA_WIDTH = DOG_IMAGE.get_width()
    MASCOTA_HEIGHT = DOG_IMAGE.get_height()

    DORMIR_EMOTE = []
    FELIZ_EMOTE = []
    HAMBRE_EMOTE = []
    LIMPIAR_EMOTE = []

    GATO_IDLE = []

    for i in range(10):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//mascotas//gato//GATO{i+1}.png'), GATO_SCALE)
            GATO_IDLE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//durmiendo//DORMIR{i+1}.png'), 1.8)
            DORMIR_EMOTE.append(new_img)

    for i in range(3):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//felicidad//FELICIDAD{i+1}.png'), 1.8)
            FELIZ_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//HAMBRE{i+1}.png'), 1.8)
            HAMBRE_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//limpiar//LIMPIAR{i+1}.png'), 1.8)
            LIMPIAR_EMOTE.append(new_img)

    BTN_WIDTH = 150
    BTN_HEIGHT = 50
