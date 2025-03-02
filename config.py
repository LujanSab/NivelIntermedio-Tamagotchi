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

    PERRO_SCALE = 2.0
    GATO_SCALE = 2.0

    _dog_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//perro//perroidle//perro1.png')
    DOG_IMAGE = scale_img(_dog_img, PERRO_SCALE)

    _cat_img = pygame.image.load(f'{ASSETS_UTL}//mascotas//gato//gatoidle//gato1.png')
    CAT_IMG = scale_img(_cat_img, GATO_SCALE)

    MASCOTA_WIDTH = DOG_IMAGE.get_width()
    MASCOTA_HEIGHT = DOG_IMAGE.get_height()

    DORMIR_EMOTE = []
    FELIZ_EMOTE = []
    HAMBRE_EMOTE = []
    LIMPIAR_EMOTE = []
    JUGAR_EMOTE = []

    GATO_IDLE = []

    for i in range(7):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//mascotas//gato//gatoidle//GATO{i+1}.png'), GATO_SCALE)
            GATO_IDLE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//durmiendo//petenergy{i+1}.png'), 1.8)
            DORMIR_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//felicidad//pethapp{i+1}.png'), 1.8)
            FELIZ_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//catfood{i+1}.png'), 1.8)
            HAMBRE_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//limpiar//petbath{i+1}.png'), 1.8)
            LIMPIAR_EMOTE.append(new_img)
    
    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//jugar//catsocial{i+1}.png'), 1.8)
            JUGAR_EMOTE.append(new_img)

    PERRO_IDLE = []

    for i in range(7):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//mascotas//perro//perroidle//perro{i+1}.png'), PERRO_SCALE)
            PERRO_IDLE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//durmiendo//petenergy{i+1}.png'), 1.8)
            DORMIR_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//felicidad//pethapp{i+1}.png'), 1.8)
            FELIZ_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//hambre//dogfood{i+1}.png'), 1.8)
            HAMBRE_EMOTE.append(new_img)

    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//limpiar//petbath{i+1}.png'), 1.8)
            LIMPIAR_EMOTE.append(new_img)
    
    for i in range(2):
            new_img = scale_img(pygame.image.load(f'{ASSETS_UTL}//emotes//jugar//dogsocial{i+1}.png'), 1.8)
            JUGAR_EMOTE.append(new_img)

    BTN_WIDTH = 150
    BTN_HEIGHT = 50
