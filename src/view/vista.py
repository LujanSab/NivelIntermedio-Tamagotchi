from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import W
from tkinter.ttk import Treeview
from tkinter.messagebox import askyesno, showinfo
from controller.controlador import Controlador

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.controlador = Controlador()
        self.root.geometry('700x400')
        self.root.title("Mascotas")
        self.root.configure(bg="#c689e3")
        self.var_nombre_mascota = StringVar()
        self.var_nombre_duenio = StringVar()
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
        self.tree = Treeview(self.root, height=15)

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
        
        self.boton_alta = Button(self.root, text="Guardar", command=lambda:self.alta(), width=25)
        self.boton_alta.place(x=500, y=160)

        self.boton_consulta = Button(self.root, text="Consultar", command=lambda:self.consulta(), width=25)
        self.boton_consulta.place(x=500, y=220)

        self.boton_seleccionar = Button(self.root, text="Seleccionar", command=lambda:self.seleccionar(), width=25, state="disabled")
        self.boton_seleccionar.place(x=500, y=260)

        self.boton_eliminar = Button(self.root, text="Modificar", width=25, state="disabled")
        self.boton_eliminar.place(x=500, y=300)

        self.boton_eliminar = Button(self.root, text="Eliminar", command=lambda:self.eliminar(), width=25, state="disabled")
        self.boton_eliminar.place(x=500, y=340)

    def alta(self):
        nombre = self.ventana.var_nombre_mascota.get()
        duenio = self.ventana.var_nombre_duenio.get()
        self.controlador.alta(nombre, duenio, self.tipo)
    
    def obtener_perro(self):
        self.tipo = self.boton_perro["text"]
        self.boton_gato["state"] = "disabled"
        
    def obtener_gato(self):
        self.tipo = self.boton_gato["text"]
        self.boton_perro["state"] = "disabled"
    
    def consulta(self):
        datos = self.controlador.consulta()
        for fila in datos:
           self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))
        self.boton_seleccionar["state"] = "active"
    
    def seleccionar(self):
        self.valor = self.tree.selection()
        item = self.tree.item(self.valor)
        self.datos_mascota = item['values']
        self.var_nombre_mascota.set(self.datos_mascota[0])
        self.var_nombre_duenio.set(self.datos_mascota[1])
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