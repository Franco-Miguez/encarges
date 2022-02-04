import tkinter
from tkinter import *
from baseDeDatos import conector

conector = conector.Conector()


class Modificar:
    def __init__(self, id):
        self.ventanaSecundaria = Toplevel()
        self.ventanaSecundaria.geometry("500x500")
        self.id = id

    def ventana(self):

        titulo = Label(self.ventanaSecundaria, text="Modificar")
        titulo.config(font=("Arial",20))
        titulo.pack(side=TOP, anchor=CENTER)

        informacionProducto = conector.mostrarLinea("clientes","celular",self.id)

        self.valorNombreInicial = informacionProducto[0][2]
        self.valorCelularInicial = informacionProducto[0][1]

        self.valorNombre = StringVar()
        self.valorNombre.set(self.valorNombreInicial)
        self.valorCelular = StringVar()
        self.valorCelular.set(self.valorCelularInicial)

        self.textoNombre = Label(self.ventanaSecundaria, text="Nombre: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria,  width=50, textvariable=self.valorNombre).pack(side=TOP, anchor=W, padx=30, pady=10, ipady=5)


        self.textoCelular = Label(self.ventanaSecundaria, text="Celular: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaCelular = Entry(self.ventanaSecundaria, width=20, textvariable=self.valorCelular).pack(side=TOP, anchor=W, padx=30, pady=10)



        self.botonGuardar = Button(self.ventanaSecundaria, text="Guardar", command=self.modificar)
        self.botonCancelar = Button(self.ventanaSecundaria, text="Cancelar", command=self.cancelar)

        self.botonCancelar.pack(side=BOTTOM, anchor=CENTER, pady=10)
        self.botonGuardar.pack(side=BOTTOM, anchor=CENTER, pady=10, padx=30)


    def modificar(self):

        if self.valorNombre != self.valorNombreInicial:
            conector.modificar("clientes",
                               "nombre",
                               self.valorNombre.get(),
                               "celular",
                               self.valorCelularInicial)

        if self.valorCelular != self.valorCelularInicial:
            conector.modificar("clientes",
                               "celular",
                               self.valorCelular.get(),
                               "celular",
                               self.valorCelularInicial)



        self.ventanaSecundaria.destroy()

    def cancelar(self):
        self.ventanaSecundaria.destroy()

