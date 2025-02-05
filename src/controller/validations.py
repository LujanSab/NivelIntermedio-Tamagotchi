import re

class Validacion:
    def __init__(self):
        self.PATRON_STR = "^[A-Za-z]+(?:[ ][A-Za-z]+)*$"

    def validar_campos_str(self, campo):
        return (re.match(self.PATRON_STR, campo))