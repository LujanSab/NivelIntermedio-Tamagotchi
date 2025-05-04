# Aca dentro esta toda la logica para las interfaces graficas con Tkinter PREVIAS a entrar al juego,
# dentro se evaluan y traen diferentes datos de la base de datos, dandote ademas diferentes funciones como usuario
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import W
from tkinter.ttk import Treeview
from tkinter.messagebox import askyesno, showinfo
from src.models.mascotas.mascotaService import MascotaService
from src.view.game import Game
from tkinter import Toplevel
from src.controller.logger import log
from src.controller.validations import Validacion
from src.view.control_server import ControlServer

# --------------------------------------------------
# Ventana de Registro 
# --------------------------------------------------
class VentanaRegistro:
    """
    El código define una clase `VentanaRegistro` en Python que crea una ventana GUI para registrar
    información de la mascota e iniciar un juego de mascota virtual.
    """
    def __init__(self, root):
        self.root = root
        self.root.geometry('190x250')
        self.root.resizable(False, False)
        self.root.title("")
        self.root.configure(bg="#c689e3")
        self.service = MascotaService()
        self.validacion = Validacion()
        self.var_nombre_mascota = StringVar()
        self.var_nombre_duenio = StringVar()
        self.tipo = None
        self.server = ControlServer()
        self.server.try_connection()
        # --------------------------------------------------
        # LABELS 
        # --------------------------------------------------
        self.titulo_2 = Label(self.root, text="Datos Mascota", bg="#790f9b", fg="white", width=25)
        self.titulo_2.place(x=5, y=5)

        self.lab_nom_mascota = Label(self.root, text="Nombre", bg="#c689e3")
        self.lab_nom_mascota.place(x=5, y=30)

        self.lab_nom_duenio = Label(self.root, text="Dueño", bg="#c689e3")
        self.lab_nom_duenio.place(x=5, y=60)

        self.lab_tipo = Label(self.root, text="Tipo", bg="#c689e3")
        self.lab_tipo.place(x=5, y=90)

        self.lab_existente = Label(self.root, text="¿Ya tienes una mascota?", bg="#c689e3")
        self.lab_existente.place(x=25, y=160)

        # --------------------------------------------------
        # ENTRYS 
        # --------------------------------------------------
        self.entry_nom_mascota = Entry(self.root, textvariable=self.var_nombre_mascota, width=19)
        self.entry_nom_mascota.place(x=65, y=30)

        self.entry_nom_duenio= Entry(self.root, textvariable=self.var_nombre_duenio, width=19)
        self.entry_nom_duenio.place(x=65, y=60)

        # --------------------------------------------------
        # BUTTONS
        # --------------------------------------------------
        self.boton_perro = Button(self.root, text="Perro", command=lambda:self.obtener_perro(), width=6)
        self.boton_perro.place(x=65, y=90)

        self.boton_gato = Button(self.root, text="Gato", command=lambda:self.obtener_gato(), width=6)
        self.boton_gato.place(x=130, y=90)

        self.boton_comenzar = Button(self.root, text="Comenzar partida", command=lambda:self.comenzar_partida(), width=24)
        self.boton_comenzar.place(x=5, y=120)

        self.boton_existente = Button(self.root, text="Buscar", command=lambda:self.buscar_mascota(), width=24)
        self.boton_existente.place(x=5, y=180)

    # --------------------------------------------------
    # FUNCIONES
    # --------------------------------------------------
    @log
    def comenzar_partida(self):
        '''
        Crea una mascota en la 
        base de datos y ejecuta la funcion run para correr el juego
        '''
        try:
            nombre = self.var_nombre_mascota.get()
            duenio = self.var_nombre_duenio.get()
            if self.validacion.validar_campos_str(nombre) and self.validacion.validar_campos_str(duenio):
                self.service.crear_mascota(nombre, duenio, self.tipo)
                if self.service.mascota:
                    game = Game(self.service.mascota)
                    game.run()
                    return f"Se registró a la mascota {nombre} del dueño: {duenio}. Comienzo de partida."
                else:
                    showinfo("", "No se creó su mascota virtual. Intente de nuevo.")
                    return "No se creó su mascota virtual."
            else:
                showinfo("", "Los datos ingresados contienen carácteres inválidos. Intente de nuevo.")
                self.limpiar()
                return "Los datos ingresados contienen carácteres inválidos."
        except Exception as error:
            self.limpiar()
            showinfo("", "Los campos no deben estar en blanco.")
            return error, "Los campos no deben estar en blanco."
        finally:
            self.limpiar()
            self.server.stop_server()
            return "Terminó la partida."

    def obtener_perro(self):
        """
        Esta función de Python establece el atributo 
        "tipo" en perro y desactiva
        el botón gato.
        """
        self.tipo = self.boton_perro["text"]
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        """
        Esta función de Python establece el atributo 
        "tipo" en gato y desactiva
        el botón perro.
        """
        self.tipo = self.boton_gato["text"]
        self.boton_perro["state"] = "disabled"
    
    def buscar_mascota(self):
        '''
        Ejecuta la ventana secundaria para administracion de mascotas
        '''
        self.ventana_principal = VentanaPrincipal(Toplevel())
        self.ventana_principal.root.mainloop()

    def limpiar(self):
        '''
        Elimina el texto de los campos de nombre de mascota y nombre del dueño
        '''
        self.var_nombre_mascota.set("")
        self.var_nombre_duenio.set("")
        self.boton_gato["state"] = "active"
        self.boton_perro["state"] = "active"



# --------------------------------------------------
# Ventana Principal 
# --------------------------------------------------
class VentanaPrincipal:
    """
    El código define una clase `VentanaPrincipal` en Python para administrar un sistema de registro de mascotas
    con funciones para filtrar, jugar con, ver, seleccionar y eliminar registros de mascotas.
    """
    def __init__(self, root):
        self.root = root
        self.service = MascotaService()
        self.validacion = Validacion()
        self.root.geometry('850x450')
        self.root.resizable(False, False)
        self.root.title("Mascotas")
        self.root.configure(bg="#c689e3")
        self.var_nombre_mascota = StringVar()
        self.var_nombre_duenio = StringVar()
        self.tipo = None
        self.valor = 0
        self.datos_mascota = None

        # --------------------------------------------------
        # LABELS 
        # --------------------------------------------------
        self.titulo_1 = Label(self.root, text="Registro Mascotas", bg="#c689e3")
        self.titulo_1.place(x=5, y=12)
        self.titulo_1.config(font=("Helvetica", 12, "bold"))

        self.titulo_2 = Label(self.root, text="Datos Mascota", bg="#790f9b", fg="white", width=25)
        self.titulo_2.place(x=660, y=40)

        self.lab_nom_mascota = Label(self.root, text="Nombre", bg="#c689e3")
        self.lab_nom_mascota.place(x=660, y=70)

        self.lab_nom_duenio = Label(self.root, text="Dueño", bg="#c689e3")
        self.lab_nom_duenio.place(x=660, y=100)

        self.lab_tipo = Label(self.root, text="Tipo", bg="#c689e3")
        self.lab_tipo.place(x=660, y=130)

        # --------------------------------------------------
        # ENTRYS 
        # --------------------------------------------------
        self.entry_nom_mascota = Entry(self.root, textvariable=self.var_nombre_mascota, width=19)
        self.entry_nom_mascota.place(x=720, y=70)

        self.entry_nom_duenio= Entry(self.root, textvariable=self.var_nombre_duenio, width=19)
        self.entry_nom_duenio.place(x=720, y=100)

        # --------------------------------------------------
        # TREEVIEW 
        # --------------------------------------------------
        self.tree = Treeview(self.root, height=17)

        # --- COLUMNS
        self.tree["columns"] = ("Nombre", "Dueño", "Tipo", "Energia", "Limpieza", "Hambre", "Felicidad", "Social", "Ultimo Ingreso")
        self.tree.column("#0", width=30, minwidth=30)
        self.tree.column("Nombre", width=60, minwidth=60, anchor=W)
        self.tree.column("Dueño", width=60, minwidth=60, anchor=W)
        self.tree.column("Tipo", width=60, minwidth=60, anchor=W)
        self.tree.column("Energia", width=60, minwidth=60, anchor=W)
        self.tree.column("Limpieza", width=60, minwidth=60, anchor=W)
        self.tree.column("Hambre", width=60, minwidth=60, anchor=W)
        self.tree.column("Felicidad", width=60, minwidth=60, anchor=W)
        self.tree.column("Social", width=60, minwidth=60, anchor=W)
        self.tree.column("Ultimo Ingreso", width=120, minwidth=120, anchor=W)
        self.tree.place(x=5, y=40)

        # --- HEADERS
        self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dueño", text="Dueño")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Energia", text="Energia")
        self.tree.heading("Limpieza", text="Limpieza")
        self.tree.heading("Hambre", text="Hambre")
        self.tree.heading("Felicidad", text="Felicidad")
        self.tree.heading("Social", text="Social")
        self.tree.heading("Ultimo Ingreso", text="Ultimo Ingreso")

        # --------------------------------------------------
        # BUTTONS
        # --------------------------------------------------
        self.boton_perro = Button(self.root, text="Perro", command=lambda:self.obtener_perro(), width=6)
        self.boton_perro.place(x=720, y=130)

        self.boton_gato = Button(self.root, text="Gato", command=lambda:self.obtener_gato(), width=6)
        self.boton_gato.place(x=790, y=130)
        
        self.boton_buscar = Button(self.root, text="Buscar", command=lambda:self.filtrar_mascota(), width=25)
        self.boton_buscar.place(x=660, y=160)
        
        self.boton_jugar = Button(self.root, text="Jugar", command=lambda:self.jugar(), width=25, state="disabled")
        self.boton_jugar.place(x=660, y=195)

        self.boton_consulta = Button(self.root, text="Ver todas las mascotas", command=lambda:self.consulta(), width=25)
        self.boton_consulta.place(x=660, y=250)

        self.boton_seleccionar = Button(self.root, text="Seleccionar", command=lambda:self.seleccionar(), width=25, state="disabled")
        self.boton_seleccionar.place(x=660, y=290)

        self.boton_eliminar = Button(self.root, text="Eliminar", command=lambda:self.eliminar(), width=25, state="disabled")
        self.boton_eliminar.place(x=660, y=330)
    
    # --------------------------------------------------
    # FUNCIONES
    # --------------------------------------------------
    def obtener_perro(self):
        """
        Esta función de Python establece el atributo 
        "tipo" en función del texto de un botón y desactiva
        el botón gato.
        """
        self.tipo = self.boton_perro["text"].lower()
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        """
        Esta función de Python establece el atributo 
        "tipo" en función del texto de un botón y desactiva
        el botón perro.
        """
        self.tipo = self.boton_gato["text"].lower()
        self.boton_perro["state"] = "disabled"
        
    @log
    def filtrar_mascota(self):
        '''
        Esta funcion se encarga de filtrar la mascota y traer todos los datos
        que coincidan con el nombre y el dueño que hayas especificado
        '''
        nombre = self.var_nombre_mascota.get()
        dueño = self.var_nombre_duenio.get()

        if self.validacion.validar_campos_str(nombre) and self.validacion.validar_campos_str(dueño):
            data = self.service.obtener_datos_mascota(nombre)
            if data:
                self.tree.insert("", 0, 
                                text=data["id"], 
                                values=(data["nombre_mascota"], 
                                        data["nombre_dueño"], 
                                        data["tipo"], 
                                        data["energia"],
                                        data["limpieza"],  
                                        data["hambre"], 
                                        data["felicidad"],
                                        data["social"],
                                        data["ultima_actualizacion"]))
                self.boton_jugar["state"] = "active"
                return f"Se filtró a: Mascota: {nombre}. Dueño: {dueño}"
            else:
                showinfo("", f"No existe la mascota llamada:{nombre}. Intente con otro nombre.")
                return f"No existe la mascota llamada:{nombre}. Intente con otro nombre."
        else:
            showinfo("", "Los datos ingresados contienen carácteres inválidos. Intente de nuevo.")
            return "Los datos ingresados contienen carácteres inválidos. Intente de nuevo."
        
    @log
    def jugar(self):
        '''
        Dentro de esta funcion, se crea un objeto de mascota previo a jugar, con los datos
        de la mascota seleccionada y ejecuta el metodo run de game.py
        '''
        try:
            self.valor = self.tree.focus()
            item = self.tree.item(self.valor)
            self.datos_mascota = item['values']
            self.service.crear_objeto_mascota(nombre=self.datos_mascota[0], 
                                            duenio=self.datos_mascota[1], 
                                            tipo=self.datos_mascota[2],
                                            energia=self.datos_mascota[3],
                                            limpieza=self.datos_mascota[4],
                                            hambre=self.datos_mascota[5],
                                            felicidad=self.datos_mascota[6],
                                            social=self.datos_mascota[7])
            if self.service.mascota:
                game = Game(self.service.mascota)
                game.run()
                self.limpiar_vista()
                return f"Comenzó la partida con la mascota {self.datos_mascota[0]}"
            else:
                showinfo("", "No se creó su mascota virtual. Intente de nuevo.")
                return "No se creó su mascota virtual."
        except Exception as error:
            return error

    @log
    def consulta(self):
        '''
        Metodo que se encarga de limpiar la tabla en la 
        vista y traer todos los datos de todas las mascotas
        '''
        self.limpiar_vista()
        datos = self.service.obtener_todas_las_mascotas()
        for fila in datos:
            self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]))
            self.boton_seleccionar["state"] = "active"
        
        return "Se insertaron a todas las mascotas."
    
    @log
    def seleccionar(self):
        '''
        Metodo que se encarga de seleccionar un elemento de la tabla
        '''
        self.valor = self.tree.selection()
        item = self.tree.item(self.valor)
        self.datos_mascota = item['values']
        self.var_nombre_mascota.set(self.datos_mascota[0])
        self.var_nombre_duenio.set(self.datos_mascota[1])
        self.boton_gato["state"] = "disabled"
        self.boton_perro["state"] = "disabled"
        self.boton_jugar["state"] = "active"
        self.boton_eliminar["state"] = "active"
        return f"Se seleccionó a la mascota f{self.datos_mascota[0]}"

    @log
    def eliminar(self):
        '''
        Metodo que se encarga de eliminar una mascota seleccionada
        en la tabla
        '''
        if askyesno("Atención", f"¿Desea confirmar la eliminación de la mascota: {self.datos_mascota[0]}?"):
            mensaje = self.service.eliminar(self.datos_mascota[0], self.datos_mascota[1])
            self.tree.delete(self.valor)
            self.valor = 0
            showinfo("", mensaje)
            self.limpiar_vista_eliminar()
            return mensaje
        else:
            showinfo("", "No se han efectuado cambios")
            return "No se han efectuados cambios."
    
    def limpiar_vista(self):
        '''
        Metodo que se encarga de limpiar los datos de la tabla de datos
        '''
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        self.var_nombre_duenio.set("")
        self.var_nombre_mascota.set("")
        self.boton_gato["state"] = "active"
        self.boton_perro["state"] = "active"
        self.boton_eliminar["state"] = "disabled"
        self.boton_jugar["state"] = "disabled"
        self.boton_seleccionar["state"] = "disabled"
    
    def limpiar_vista_eliminar(self):
        """
        Método para la limpiar la vista después de usar la función eliminar.
        """
        self.boton_gato["state"] = "active"
        self.boton_perro["state"] = "active"
        self.boton_eliminar["state"] = "disabled"
        self.boton_jugar["state"] = "disabled"
        self.var_nombre_duenio.set("")
        self.var_nombre_mascota.set("")

    

 