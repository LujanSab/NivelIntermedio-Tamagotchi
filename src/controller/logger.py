import logging
import os
from config import BASE_DIR

log_directory = os.path.join(BASE_DIR, 'logs')

os.makedirs(log_directory, exist_ok=True)

log_file_path = os.path.join(log_directory, 'logs.log')

logging.basicConfig(
    filename=log_file_path,
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def log(event):
    logging.info(event)