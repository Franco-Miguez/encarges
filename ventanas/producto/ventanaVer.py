import tkinter
from tkinter import *
from baseDeDatos import conector

conector = conector.Conector()


class VerProducto:
    def __init__(self, id):
        self.ventanaSecundaria = Toplevel()
        self.ventanaSecundaria.geometry("500x500")
        self.id = id

    def ventana(self):

        titulo = Label(self.ventanaSecundaria, text="Agregar")
        titulo.config(font=("Arial",20))
        titulo.pack(side=TOP, anchor=CENTER)

        informacionProducto = conector.mostrarLinea("productos","nombre",self.id)


        self.valorNombre = StringVar()
        self.valorNombre.set(informacionProducto[0][1])
        self.valorPrecio = DoubleVar()
        self.valorPrecio.set(informacionProducto[0][3])

        self.textoNombre = Label(self.ventanaSecundaria, text="Nombre: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria, state="disable", width=50, textvariable=self.valorNombre).pack(side=TOP, anchor=W, padx=30, pady=10, ipady=5)


        self.textoPrecio = Label(self.ventanaSecundaria, text="Precio: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria, state="disable",width=20, textvariable=self.valorPrecio).pack(side=TOP, anchor=W, padx=30, pady=10)


        self.textoDescripcion = Label(self.ventanaSecundaria, text="Descripción: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaDescripcion = tkinter.Text(self.ventanaSecundaria,height=5)
        self.entradaDescripcion.insert("insert", informacionProducto[0][2])
        self.entradaDescripcion.config(state="disable")
        self.entradaDescripcion.pack(side=TOP, anchor=W, padx=30, pady=10)


        self.botonCerrar = Button(self.ventanaSecundaria,text="Cerrar", command=self.ventanaSecundaria.destroy)
        self.botonCerrar.pack(side=BOTTOM, anchor=CENTER, pady=10, padx=30)