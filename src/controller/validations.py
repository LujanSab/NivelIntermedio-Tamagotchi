# Dentro de este modulo se agregan todas las validaciones necesarias
# para la app en general
import re

class Validacion:
    """
    La función `validar_campos_str` utiliza un patrón de expresión regular para validar una cadena
    de entrada.

    :param campo: El parámetro `campo` es una cadena que desea validar contra el patrón de expresión regular
    definido en el atributo `PATRON_STR` de la clase `Validacion`. 
    El patrón de expresión regular `^[A-Za-z]+(?:[ ][A-Za-z]+)*$` 
    se utiliza para validarlo
    """
    def __init__(self):
        self.PATRON_STR = "^[A-Za-z]+(?:[ ][A-Za-z]+)*$"

    def validar_campos_str(self, campo):
        """
    La función `validar_campos_str` verifica si una cadena dada coincide con un patrón especificado.

    :param campo: El parámetro `campo` es una cadena que representa un campo o valor que necesita
    ser validado contra un patrón de expresión regular definido en el atributo `PATRON_STR` de la
    clase. El método `validar_campos_str` usa la función `re.match` para verificar si el `campo`
    :return: La función `validar_campos_str` está devolviendo el resultado de `re.match(self.PATRON_STR,
    campo)`. Es probable que esta función esté verificando si la cadena `campo` coincide con un patrón específico
    definido por `self.PATRON_STR`. Si hay una coincidencia, devolverá el objeto coincidente, de lo contrario,
    devolverá `None`.
    """
        return (re.match(self.PATRON_STR, campo))