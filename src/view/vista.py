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

# --------------------------------------------------
# Ventana de Registro 
# --------------------------------------------------
class VentanaRegistro:
    def __init__(self, root):
        self.root = root
        self.root.geometry('190x250')
        self.root.title("")
        self.root.configure(bg="#c689e3")
        self.service = MascotaService()
        self.validacion = Validacion()
        self.var_nombre_mascota = StringVar()
        self.var_nombre_duenio = StringVar()
        self.tipo = None

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
    def comenzar_partida(self):
        try:
            nombre = self.var_nombre_mascota.get()
            duenio = self.var_nombre_duenio.get()
            if self.validacion.validar_campos_str(nombre) and self.validacion.validar_campos_str(duenio):
                self.service.crear_mascota(nombre, duenio, self.tipo)
                if self.service._mascota:
                    game = Game(self.service._mascota)
                    game.run()
                else:
                    showinfo("", "No se creó su mascota virtual. Intente de nuevo.")
            else:
                showinfo("", "Los datos ingresados contienen carácteres inválidos. Intente de nuevo.")
                self.limpiar()
        except Exception as error:
            print(error)
            showinfo("", "Los campos no deben estar en blanco.")
            log(error)
            self.limpiar()

    def obtener_perro(self):
        self.tipo = self.boton_perro["text"]
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        self.tipo = self.boton_gato["text"]
        self.boton_perro["state"] = "disabled"
    
    def buscar_mascota(self):
        self.ventana_principal = VentanaPrincipal(Toplevel())
        self.ventana_principal.root.mainloop()

    def limpiar(self):
        self.var_nombre_mascota.set("")
        self.var_nombre_duenio.set("")
        self.boton_gato["state"] = "active"
        self.boton_perro["state"] = "active"

# --------------------------------------------------
# Ventana Principal 
# --------------------------------------------------
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.service = MascotaService()
        self.validacion = Validacion()
        self.root.geometry('700x450')
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
        self.titulo_2.place(x=500, y=40)

        self.lab_nom_mascota = Label(self.root, text="Nombre", bg="#c689e3")
        self.lab_nom_mascota.place(x=500, y=70)

        self.lab_nom_duenio = Label(self.root, text="Dueño", bg="#c689e3")
        self.lab_nom_duenio.place(x=500, y=100)

        self.lab_tipo = Label(self.root, text="Tipo", bg="#c689e3")
        self.lab_tipo.place(x=500, y=130)

        # --------------------------------------------------
        # ENTRYS 
        # --------------------------------------------------
        self.entry_nom_mascota = Entry(self.root, textvariable=self.var_nombre_mascota, width=19)
        self.entry_nom_mascota.place(x=560, y=70)

        self.entry_nom_duenio= Entry(self.root, textvariable=self.var_nombre_duenio, width=19)
        self.entry_nom_duenio.place(x=560, y=100)

        # --------------------------------------------------
        # TREEVIEW 
        # --------------------------------------------------
        self.tree = Treeview(self.root, height=17)

        # --- COLUMNS
        self.tree["columns"] = ("Nombre", "Dueño", "Tipo", "Energia", "Limpieza", "Hambre", "Felicidad")
        self.tree.column("#0", width=30, minwidth=30)
        self.tree.column("Nombre", width=70, minwidth=70, anchor=W)
        self.tree.column("Dueño", width=70, minwidth=70, anchor=W)
        self.tree.column("Tipo", width=70, minwidth=70, anchor=W)
        self.tree.column("Energia", width=60, minwidth=60, anchor=W)
        self.tree.column("Limpieza", width=60, minwidth=60, anchor=W)
        self.tree.column("Hambre", width=60, minwidth=60, anchor=W)
        self.tree.column("Felicidad", width=60, minwidth=60, anchor=W)
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

        # --------------------------------------------------
        # BUTTONS
        # --------------------------------------------------
        self.boton_perro = Button(self.root, text="Perro", command=lambda:self.obtener_perro(), width=6)
        self.boton_perro.place(x=560, y=130)

        self.boton_gato = Button(self.root, text="Gato", command=lambda:self.obtener_gato(), width=6)
        self.boton_gato.place(x=630, y=130)
        
        self.boton_buscar = Button(self.root, text="Buscar", command=lambda:self.filtrar_mascota(), width=25)
        self.boton_buscar.place(x=500, y=160)
        
        self.boton_jugar = Button(self.root, text="Jugar", command=lambda:self.jugar(), width=25, state="disabled")
        self.boton_jugar.place(x=500, y=195)

        self.boton_consulta = Button(self.root, text="Ver todas las mascotas", command=lambda:self.consulta(), width=25)
        self.boton_consulta.place(x=500, y=250)

        self.boton_seleccionar = Button(self.root, text="Seleccionar", command=lambda:self.seleccionar(), width=25, state="disabled")
        self.boton_seleccionar.place(x=500, y=290)

        self.boton_eliminar = Button(self.root, text="Eliminar", command=lambda:self.eliminar(), width=25, state="disabled")
        self.boton_eliminar.place(x=500, y=330)
    
    # --------------------------------------------------
    # FUNCIONES
    # --------------------------------------------------
    def obtener_perro(self):
        self.tipo = self.boton_perro["text"].lower()
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        self.tipo = self.boton_gato["text"].lower()
        self.boton_perro["state"] = "disabled"
        
    def filtrar_mascota(self):
        nombre = self.var_nombre_mascota.get()
        dueño = self.var_nombre_duenio.get()

        try:
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
                                        data["felicidad"]))
                self.boton_jugar["state"] = "active"
            else:
                showinfo("", f"No existe la mascota llamada:{nombre}. Intente con otro nombre.")
          else:
            showinfo("", "Los datos ingresados contienen carácteres inválidos. Intente de nuevo.")
        except Exception as error:
            log(error)

    def jugar(self):
        self.valor = self.tree.focus()
        item = self.tree.item(self.valor)
        self.datos_mascota = item['values']
        print(self.datos_mascota)
        try:
            self.service.crear_objeto_mascota(nombre=self.datos_mascota[0], 
                                            duenio=self.datos_mascota[1], 
                                            tipo=self.datos_mascota[2],
                                            energia=self.datos_mascota[3],
                                            limpieza=self.datos_mascota[4],
                                            hambre=self.datos_mascota[5],
                                            felicidad=self.datos_mascota[6])
            if self.service._mascota:
                game = Game(self.service._mascota)
                game.run()
                self.limpiar_vista()
            else:
                showinfo("", "No se creó su mascota virtual. Intente de nuevo.")
        except Exception as error:
            log(error)
    
    def consulta(self):
        self.limpiar_vista()
        try:
            datos = self.service.obtener_todas_las_mascotas()
            for fila in datos:
                self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))
                self.boton_seleccionar["state"] = "active"
        except Exception as error:
            log(error)
    
    def seleccionar(self):
        self.valor = self.tree.selection()
        item = self.tree.item(self.valor)
        self.datos_mascota = item['values']
        self.var_nombre_mascota.set(self.datos_mascota[0])
        self.var_nombre_duenio.set(self.datos_mascota[1])
        self.boton_gato["state"] = "disabled"
        self.boton_perro["state"] = "disabled"
        self.boton_jugar["state"] = "active"
        self.boton_eliminar["state"] = "active"

    def eliminar(self):
        if askyesno("Atención", f"¿Desea confirmar la eliminación de la mascota: {self.datos_mascota[0]}?"):
            try:
                mensaje = self.service.eliminar(self.datos_mascota[0], self.datos_mascota[1])
                self.tree.delete(self.valor)
                self.valor = 0
                showinfo("", mensaje)
                self.limpiar_vista_eliminar()
            except Exception as error:
                log(error)
        else:
            showinfo("", "No se han efectuado cambios")
    
    def limpiar_vista(self):
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
        Es para la limpiar la vista después de usar la función eliminar.
        """
        self.boton_gato["state"] = "active"
        self.boton_perro["state"] = "active"
        self.boton_eliminar["state"] = "disabled"
        self.boton_jugar["state"] = "disabled"
        self.var_nombre_duenio.set("")
        self.var_nombre_mascota.set("")

