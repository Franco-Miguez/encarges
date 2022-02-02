import _tkinter
import tkinter
from tkinter import *
from tkinter import messagebox as ms
from baseDeDatos import conector
from elementos import producto

conector = conector.Conector()

class AgregarProducto:
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

        self.valorPrecio = DoubleVar()
        self.textoPrecio = Label(self.ventanaSecundaria, text="Precio: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria, width=20, textvariable=self.valorPrecio).pack(side=TOP, anchor=W, padx=30, pady=10)

        self.valorDescripcion = StringVar()
        self.textoDescripcion = Label(self.ventanaSecundaria, text="Descripción: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaDescripcion = tkinter.Text(self.ventanaSecundaria, height=5)
        self.entradaDescripcion.insert("insert", "")
        self.entradaDescripcion.pack(side=TOP, anchor=W, padx=30, pady=10)

        self.botonGuardar = Button(self.ventanaSecundaria,text="Guardar", command=self.guardar)
        self.botonCancelar = Button(self.ventanaSecundaria,text="Cancelar", command=self.cancelar)

        self.botonCancelar.pack(side=BOTTOM, anchor=CENTER, pady=10)
        self.botonGuardar.pack(side=BOTTOM, anchor=CENTER, pady=10, padx=30)



    def guardar(self):
        try:
            nuevoProducto = producto.Producto(self.valorNombre.get(),
                                              self.entradaDescripcion.get(1.0,END),
                                              self.valorPrecio.get(),
                                              None)
            conector.guardarProducto(nuevoProducto)
            self.ventanaSecundaria.destroy()
        except _tkinter.TclError:
            ms.showerror("ERROR", "Ingrese un numero en precio\ny que sea con . y no ,")


    def cancelar(self):
        self.ventanaSecundaria.destroy()



