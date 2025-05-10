import os
import sys
from pathlib import Path
import subprocess
import threading

theproc=""

class ControlServer:
    def __init__(self):
        self.raiz = Path(__file__).resolve().parent.parent
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

    # =================== INNIT AND STOP SERVER ====================== 
    def stop_server(self, ):
        global theproc
        if theproc !="":
            theproc.kill() 

 