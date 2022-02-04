import _tkinter
import tkinter
from tkinter import *
from tkinter import messagebox as ms
from baseDeDatos import conector
from elementos import cliente

conector = conector.Conector()

class Agregar:
    def __init__(self):
        self.ventanaSecundaria = Toplevel()
        self.ventanaSecundaria.geometry("500x500")

    def ventana(self):

        titulo = Label(self.ventanaSecundaria, text="Agregar")
        titulo.config(font=("Arial",20))
        titulo.pack(side=TOP, anchor=CENTER)

        self.valorNombre = StringVar()
        self.textoNombre = Label(self.ventanaSecundaria, text="Nombre: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria, width=50, textvariable=self.valorNombre).pack(side=TOP, anchor=W, padx=30, pady=10, ipady=5)

        self.valorCelular = IntVar()
        self.textoCelular = Label(self.ventanaSecundaria, text="Celular: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaCelular = Entry(self.ventanaSecundaria, width=20, textvariable=self.valorCelular).pack(side=TOP, anchor=W, padx=30, pady=10)


        self.botonGuardar = Button(self.ventanaSecundaria,text="Guardar", command=self.guardar)
        self.botonCancelar = Button(self.ventanaSecundaria,text="Cancelar", command=self.cancelar)

        self.botonCancelar.pack(side=BOTTOM, anchor=CENTER, pady=10)
        self.botonGuardar.pack(side=BOTTOM, anchor=CENTER, pady=10, padx=30)



    def guardar(self):
        try:
            nuevoUsuario = cliente.Cliente(self.valorCelular.get(),
                                           self.valorNombre.get())
            conector.guardarCliente(nuevoUsuario)
            self.ventanaSecundaria.destroy()
        except _tkinter.TclError:
            ms.showerror("ERROR", "Ingrese un numero en precio\ny que sea con . y no ,")


    def cancelar(self):
        self.ventanaSecundaria.destroy()



