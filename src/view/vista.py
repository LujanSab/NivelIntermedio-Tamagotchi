from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import W
from tkinter.ttk import Treeview
from tkinter.messagebox import askyesno, showinfo
from src.models.mascotas.mascotaService import MascotaService
from src.view.game import Game

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
            self.service.crear_mascota(nombre, duenio, self.tipo)
            if self.service._mascota:
                game = Game(self.service._mascota)
                game.run()
            else:
                showinfo("", "No se creó su mascota virtual. Intente de nuevo.")
        except Exception as error:
            print(error)
            showinfo("", "Los campos no deben estar en blanco.")
    
    def obtener_perro(self):
        self.tipo = self.boton_perro["text"]
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        self.tipo = self.boton_gato["text"]
        self.boton_perro["state"] = "disabled"
    
    def buscar_mascota(self):
        self.ventana_principal = VentanaPrincipal(self.root)
        self.ventana_principal.root.mainloop()

# --------------------------------------------------
# Ventana Principal 
# --------------------------------------------------
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.service = MascotaService()
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
        self.tree["columns"] = ("Nombre", "Dueño", "Tipo", "Energia", "Felicidad", "Hambre", "Limpieza")
        self.tree.column("#0", width=30, minwidth=30)
        self.tree.column("Nombre", width=70, minwidth=70, anchor=W)
        self.tree.column("Dueño", width=70, minwidth=70, anchor=W)
        self.tree.column("Tipo", width=70, minwidth=70, anchor=W)
        self.tree.column("Energia", width=60, minwidth=60, anchor=W)
        self.tree.column("Felicidad", width=60, minwidth=60, anchor=W)
        self.tree.column("Hambre", width=60, minwidth=60, anchor=W)
        self.tree.column("Limpieza", width=60, minwidth=60, anchor=W)
        self.tree.place(x=5, y=40)

        # --- HEADERS
        self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dueño", text="Dueño")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Energia", text="Energia")
        self.tree.heading("Felicidad", text="Felicidad")
        self.tree.heading("Hambre", text="Hambre")
        self.tree.heading("Limpieza", text="Limpieza")

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

        # self.boton_eliminar = Button(self.root, text="Modificar", width=25, state="disabled")
        # self.boton_eliminar.place(x=500, y=330)

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
        data = self.service.obtener_datos_mascota(nombre, dueño, self.tipo)
        if data:
            self.tree.insert("", 0, 
                             text=data["id"], 
                             values=(data["nombre_mascota"], 
                                    data["nombre_dueño"], 
                                    data["tipo"], 
                                    data["energia"], 
                                    data["felicidad"], 
                                    data["hambre"], 
                                    data["limpieza"]))
            self.boton_jugar["state"] = "active"
        else:
            showinfo("", f"No existe la mascota llamada:{nombre}. Intente con otro nombre.")
        
    
    def jugar(self):
        records = self.tree.get_children()
        self.datos_mascota = records['values']
        self.service.crear_mascota(self.datos_mascota[0], self.datos_mascota[1], self.datos_mascota[2])
        game = Game(self.service._mascota)
        game.run()
    
    # def consulta(self):
    #     datos = self.controlador.consulta()
    #     for fila in datos:
    #        self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))
    #     self.boton_seleccionar["state"] = "active"
    
    def seleccionar(self):
        self.valor = self.tree.selection()
        item = self.tree.item(self.valor)
        self.datos_mascota = item['values']
        self.var_nombre_mascota.set(self.datos_mascota[0])
        self.var_nombre_duenio.set(self.datos_mascota[1])

        if self.datos_mascota[2] == "perro":
            self.boton_perro["state"] = "active"
        elif self.datos_mascota[2] == "gato":
            self.boton_gato["state"] = "active"

        self.boton_modificar["state"] = "active"
        self.boton_eliminar["state"] = "active"

    def eliminar(self):
        if askyesno("Atención", f"¿Desea confirmar la eliminación de la mascota: {self.datos_mascota[0]}?"):
            self.controlador.eliminar(self.datos_mascota[0], self.datos_mascota[1])
            self.tree.delete(self.valor)
            self.valor = 0
            showinfo("", "Se ha eliminado con éxito.")
        else:
            showinfo("", "No se han efectuado cambios")
    
    def modificar(self):
        pass

# if __name__ == "__main__":
#     vista = VentanaRegistro(root=Tk())
#     vista.root.mainloop()