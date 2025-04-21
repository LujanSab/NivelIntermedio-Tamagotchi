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

    parametros: 
        - event: La función `log` toma un parámetro `event`, que es un mensaje o evento que
        desea registrar mediante el método `logging.info`. Esta función es útil para registrar información durante
        la ejecución de un programa
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        event = func(*args, **kwargs)
        
        logging.info(f"{event} - Ejecutando función: {func.__name__}")
        resultado = func(*args, **kwargs)
        logging.info(f"{event} - Finalizó función: {func.__name__}")
        return resultado
        
    return wrapper