# Este es el modulo donde aparece toda la logica dentro del juego y se 
# llaman a distintos modulos, como config, las diferentes entidades y las utilidades
import pygame
import traceback
from datetime import datetime, timedelta

from config import Config
from config import ASSETS_UTL

from src.models.entities.mascotas_entity import PerroEntity, GatoEntity
from src.models.entities.emote_entity import EmoteEntity
from src.models.entities.boton_entity import BotonEntity
from src.models.mascotas.mascotas import Mascota
from src.models.mascotas.mascotaService import MascotaService

from src.controller.utils import scale_img
from src.controller.logger import log


class Game:
    """
    El código Python dado define un juego en el que el 
    jugador puede interactuar con una mascota virtual
    alimentándola, limpiándola, jugando con ella y poniéndola 
    a dormir, mientras monitorea sus diversas estadísticas y emociones.
    """

    def __init__(self, mascota: Mascota):
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

        self.boton_salir = BotonEntity(
            30, 
            (Config.WINDOW_WIDTH/2),
            'SALIR',
            self.window
            )

        self.boton_jugar = BotonEntity(
            70, 
            30,
            'JUGAR',
            self.window
            )
        
        self.boton_nombre = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH/2),
            (Config.BTN_HEIGHT*2) + 30,
            f"{self.firu.nombre_mascota} - {self.firu.tipo_de_mascota}",
            self.window
        )

        self.boton_nombre_duenio = BotonEntity(
            (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH/2),
            (Config.WINDOW_HEIGHT - Config.BTN_HEIGHT) - 30,
            f"Dueño: {self.firu.nombre_dueño}",
            self.window
        )

        self.animaciones_mascotas = []

        self.animaciones_emotes = [
            Config.DORMIR_EMOTE,
            Config.FELIZ_EMOTE,
            Config.HAMBRE_EMOTE,
            Config.LIMPIAR_EMOTE,
            Config.JUGAR_EMOTE
        ]

        
        if self.firu.tipo_de_mascota == 'perro':
            self.animaciones_mascotas.append(Config.PERRO_IDLE)
            self.firu_entity = PerroEntity(
                            x=(Config.WINDOW_WIDTH/2), 
                            y=Config.WINDOW_HEIGHT/2, 
                            imagen=Config.DOG_IMG, 
                            animaciones=self.animaciones_mascotas, 
                        )
        elif self.firu.tipo_de_mascota == 'gato':
            self.animaciones_mascotas.append(Config.GATO_IDLE)
            self.firu_entity = GatoEntity(
                            x=(Config.WINDOW_WIDTH/2), 
                            y=Config.WINDOW_HEIGHT/2, 
                            imagen=Config.CAT_IMG,
                            animaciones=self.animaciones_mascotas, 
                        )
        self.emote_entity = EmoteEntity(
                        animaciones=self.animaciones_emotes,
                        window=self.window
                    )
        
        self.firu_servicio = MascotaService()
        self.firu_servicio.mascota = self.firu

    def check_status_mascota(self, null):
        atributos = [
            self.firu.energia,
            self.firu.hambre,
            self.firu.felicidad,
            self.firu.social,
            self.firu.limpieza
        ]

        atributo_bajo = 0
        atributo_cero = 0
        for atributo in atributos:
            if (atributo < 30):
                atributo_bajo += 1
            if (atributo == 0):
                atributo_cero += 1 
        
        if (atributo_bajo >= 3 and atributo_cero < 3):
            self.firu.estado = 'Enfermo'
        elif (atributo_cero >= 3):
            self.firu.estado = 'Morido'
        else:
            self.firu.estado = 'Sano'

        
    def run(self):
        '''
        Metodo encargado de correr el juego, con logica que se necesita 
        verificar en cada tick que pasa
        '''

        run = True

        while run:
            '''
            bucle main del juego
            '''

            self.firu_dict = self.firu_servicio.obtener_datos_mascota(self.firu.nombre_mascota)

            fecha_ultima_actualizacion = datetime.strptime(self.firu_dict['ultima_actualizacion'], "%d/%m/%Y, %H:%M:%S")

            diferencia_tiempo = datetime.now() - fecha_ultima_actualizacion

            self.firu_servicio.actualizar_estado_mascota(self.firu.nombre_mascota, self.firu, self.firu_dict, diferencia_tiempo)

            self.check_status_mascota(self)

            self.porcentaje_hambre = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*2) + 30,
                f"Hambre {self.firu_dict['hambre']}%",
                self.window
            )

            self.porcentaje_energia = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*3) + 40,
                f"Energia {self.firu_dict['energia']}%",
                self.window
            )

            self.porcentaje_felicidad = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*4) + 50,
                f"Felicidad {self.firu_dict['felicidad']}%",
                self.window
            )

            self.porcentaje_limpieza = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*5) + 60,
                f"Limpieza {self.firu_dict['limpieza']}%",
                self.window
            )

            self.porcentaje_social = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*6) + 70,
                f"Social {self.firu_dict['social']}%",
                self.window
            )

            self.boton_estado = BotonEntity(
                (Config.WINDOW_WIDTH/2) - (Config.MASCOTA_WIDTH*2),
                (Config.BTN_HEIGHT*7) + 80,
                f"{self.firu_dict['estado']}",
                self.window
            )

            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        accion = ''
                        
                        if self.boton_limpiar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.limpiar()
                            accion = 'limpiar'

                        elif self.boton_alimentar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.alimentar()
                            accion = 'hambre'

                        elif self.boton_dormir.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.dormir()
                            accion = 'dormir'

                        elif self.boton_jugar.forma.collidepoint(pygame.mouse.get_pos()):
                            self.firu.jugar()
                            accion = 'jugar'
                        
                        elif self.boton_salir.forma.collidepoint(pygame.mouse.get_pos()):
                            run = False

                        if(accion):
                            self.firu_servicio.actualizar(energia=self.firu.energia, felicidad=self.firu.felicidad, hambre=self.firu.hambre, social=self.firu.social, limpieza=self.firu.limpieza, nombre=self.firu.nombre_mascota)
                            self.emote_entity.iniciar_animacion(accion)

                if (self.firu.estado == 'Sano'):
                    self.animaciones_mascotas.clear()
                    if (self.firu.tipo_de_mascota == 'gato'):
                        self.animaciones_mascotas.append(Config.GATO_IDLE)
                    else:
                        self.animaciones_mascotas.append(Config.PERRO_IDLE)
                if (self.firu.estado == 'Enfermo'):
                    self.animaciones_mascotas.clear()
                    if (self.firu.tipo_de_mascota == 'gato'):
                        self.animaciones_mascotas.append(Config.GATO_SICK)
                    else:
                        self.animaciones_mascotas.append(Config.PERRO_SICK)
                if (self.firu.estado == 'Morido'):
                    self.animaciones_mascotas.clear()
                    if (self.firu.tipo_de_mascota == 'gato'):
                        self.animaciones_mascotas.append(Config.GATO_DEAD)
                    else:
                        self.animaciones_mascotas.append(Config.PERRO_DEAD)
                

                
                self.window.fill((200, 200, 200))
                
                self.firu_entity.dibujar(window=self.window)

                if isinstance(self.firu_entity, GatoEntity):
                    self.firu_entity.idle()

                self.emote_entity.actualizar_animacion()

                self.boton_limpiar.dibujar((0,0,0))
                self.boton_salir.dibujar((0,0,0))
                self.boton_dormir.dibujar((0,0,0))
                self.boton_alimentar.dibujar((0,0,0))
                self.boton_jugar.dibujar((0,0,0,0))

                self.boton_estado.dibujar((150,150,150))
                self.boton_nombre.dibujar((100,100,100))

                self.porcentaje_energia.dibujar((150,150,150))
                self.porcentaje_hambre.dibujar((150,150,150))
                self.porcentaje_felicidad.dibujar((150,150,150))
                self.porcentaje_limpieza.dibujar((150,150,150))
                self.porcentaje_social.dibujar((150,150,150))

                self.boton_nombre_duenio.dibujar((100,100,100))

                pygame.display.update()

            except:
                log(f'{__file__} - {traceback.format_exc()}')
                run = False

        pygame.quit()