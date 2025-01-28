import sqlite3
from src.config import DATABASE_NAME

class MascotaDAO:
    def __init__(self):
        try:
            self.con = self.conexion()
            self.cursor = self.crear_cursor()
            self.crear_tabla()
        except ConnectionError as error:
            print(error)

    def conexion(self):
        """_summary_
        - 
        Conexión base de datos. 
        
        Returns:
            _Connection_ : Con esta podemos crear una variable y utilizarla durante las
            consultas, porque hace la conexión con la BD.
        """
        return sqlite3.connect(DATABASE_NAME)
    
    def crear_cursor(self):
        """_summary_
        -
        Returns:
            self.con.cursor : el cursor de la conexion. Esto hará que se puedan recorrer los datos
            fila por fila, leerlos y posibilitar la ejecución de la consulta SQL. 
        """
        return self.con.cursor()

    def crear_tabla(self):
        sql = """CREATE TABLE IF NOT EXISTS mascotas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        dueño TEXT,
        tipo TEXT,
        energia INT,
        limpieza INT,
        hambre INT,
        felicidad INT)"""
        self.cursor.execute(sql)
        self.con.commit()

    def guardar_mascota(self, *args):
        sql = """INSERT INTO mascotas(nombre, dueño, tipo, energia, limpieza, hambre) 
        VALUES(?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, args)
            self.con.commit()
            return f"Se guardó la mascota {args[0]} satisfactoriamente."
        except Exception as error:
            return error

    def actualizar_estado_mascota(self, campos: str, valores: list):
        if not valores:
            raise ValueError('Se necesitan valores para actualizar.')

        sql = f"UPDATE mascotas SET {campos} WHERE nombre = ?"

        try:
            self.cursor.execute(sql, valores)
            self.con.commit()
            return "Se actualizó el estado de la mascota."
        except Exception as error:
            return f"Error: {error}"


    def eliminar_mascota(self, nombredueño, nombremascota):
        data = (nombredueño, nombremascota, )
        sql = "DELETE FROM mascotas WHERE nombre = ?, dueño = ?"
        try:
            self.cursor.execute(sql, data)
            self.con.commit()
            return f"Se eliminó a la mascota {nombremascota}"
        except Exception as error:
            return error

    def extraer_datos_mascota(self, nombremascota):
        """_summary_
        -
        Extrae los datos de una sola mascota. 

        Args:
            nombremascota (str)
        """
        data = (nombremascota, )
        sql = "SELECT * FROM mascotas WHERE nombremascota = ?"
        try:
            self.cursor.execute(sql, data)
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            return error

    def extraer_datos_mascotas(self):
        sql = "SELECT * FROM mascotas"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            return error