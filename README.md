# Tamagochi con Pygame

## proyecto
La idea surgio a base de la necesidad de usar bases de datos con el patron MVC y querer hacer un juego, la forma más rapida que encontramos de aplicarlo fue en un tamagochi con diferentes necesidades y funcionalidades.

## utilidades
dentro del juego, cada mascota tiene diferentes parametros: hambre, felicidad, limpieza, energia. Las mismas van cambiando con el tiempo y con las acciones del jugador.
Tambien está planificado en el juego para armar un administrador hecho en tkinter, donde se puedan ver, modificar, eliminar y crear datos de mascotas.

## descargar las dependencias
En la raiz del proyecto, con su gestor de entornos virtuales:
### Anaconda:
- conda create -n [nombre_de_tu_entorno]
- conda activate [nombre_de_tu_entorno]
- pip install -r requirements.txt

### virtualenvwrapper/virtualenvwrapper-win
- mkvirtualenv [nombre_de_tu_entorno]
- pip install -r requirements.txt

### python venv
- python -m venv [nombre_de_tu_entorno]

> [!NOTE]
> source /[nombre_de_tu_entorno]/Scripts/activate > para Windows
> 
> source [nombre_de_tu_entorno]/bin/activate > para MAC/Unix
- pip install -r requirements.txt

## Ejecucion del programa
Encontrara en la raiz del proyecto un archivo llamado main.py, ejecutelo y empezara a correr la app
