import sqlite3

class GestorMascotasDAO:
    def __init__(self):
        try:
            self.con = self.conexion()
            self.crear_tabla()
        except ConnectionError as error:
            print(error)

    def conexion(self):
        return sqlite3.connect("database/mascotas.db")
    
    def crear_tabla(self):
        cursor = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS mascotas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        dueño TEXT,
        tipo TEXT,
        energia INT,
        limpieza INT,
        hambre INT,
        felicidad INT)"""
        cursor.execute(sql)
        self.con.commit()

    def guardar_mascota(self, *args):
        cursor = self.con.cursor()
        sql = """INSERT INTO mascotas(nombre, dueño, tipo, energia, limpieza, hambre) 
        VALUES(?, ?, ?, ?, ?, ?)"""
        cursor.execute(sql, args)
        self.con.commit()

    def actualizar_estado_mascota(self, *args):
        cursor = self.con.cursor()
        sql = """UPDATE mascotas SET tipo = ?, energia = ?, limpieza = ?, hambre = ? WHERE id = ?"""
        cursor.execute(sql, args)
        self.con.commit()
