import os
import sys
from pathlib import Path
import subprocess
import threading

theproc=None

class ControlServer:
    def __init__(self):
        self.raiz = Path(__file__).resolve().parent.parent
        self.ruta_server = os.path.join(self.raiz, 'controller', 'server.py')
        
    def try_connection(self): 
        global theproc
        if theproc is not None and theproc.poll() is None:  # El proceso ya está corriendo
            print("El servidor ya está corriendo.")
            theproc.kill()
            threading.Thread(target=self.lanzar_servidor(), args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.lanzar_servidor(), args=(True,), daemon=True).start()
        
    def lanzar_servidor(self):
        global theproc
        the_path = self.ruta_server
        theproc = subprocess.Popen([sys.executable, the_path])

    def stop_server(self):
        global theproc
        if theproc is not None and theproc.poll() is None:
            theproc.kill()
            theproc = None
