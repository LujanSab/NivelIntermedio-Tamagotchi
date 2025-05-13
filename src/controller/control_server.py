import os
import sys
from pathlib import Path
import subprocess
import threading

theproc=""

class ControlServer:
    """
    Clase encargada de controlar la ejecución de un servidor definido en 'server.py'.

    Métodos:
    - try_connection(): Intenta lanzar el servidor. Si ya está corriendo, lo detiene y lo reinicia.
    - lanzar_servidor(var): Lanza el servidor si 'var' es True, ejecutando el script 'server.py' como un subproceso.
    - stop_server(): Detiene el servidor si está en ejecución.
    
    La ruta al script del servidor se define de forma relativa al directorio del archivo actual.
    """
    def __init__(self):
        self.raiz = Path(__file__).resolve().parent.parent   # Ruta raíz del proyecto (dos niveles por encima del archivo actual)
        self.ruta_server = os.path.join(self.raiz, 'controller', 'server.py')
        
    def try_connection(self, ): 
        if theproc != "":
            theproc.kill()
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        
    def lanzar_servidor(self, var):
        the_path =  self.ruta_server
        if var==True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()
        else:
            print("")

    def stop_server(self, ):
        global theproc
        if theproc !="":
            theproc.kill() 

 