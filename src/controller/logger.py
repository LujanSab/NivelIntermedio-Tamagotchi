import logging
import os
from config import BASE_DIR
from functools import wraps

log_directory = os.path.join(BASE_DIR, 'logs')

os.makedirs(log_directory, exist_ok=True)

log_file_path = os.path.join(log_directory, 'logs.log')

logging.basicConfig(
    filename=log_file_path,
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def log(func):
    """
    La función `log` registra un evento mediante el módulo `logging` en Python.

    Parámetros: 
        - func: La función `log` toma un parámetro `func`, que es una función que
        desea registrar mediante el método `logging.info`. Esta función es útil para registrar información durante
        la ejecución de un programa.
    
    Funcionamiento:
        resultado = func(*args, **kwargs) ejecuta la función original con todos sus argumentos posicionales y con nombre.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ejecutando función: {func.__name__}")
        resultado = func(*args, **kwargs)
        logging.info(f"Evento: {resultado}")
        logging.info(f"Finalizó función: {func.__name__}")
        return resultado
    return wrapper