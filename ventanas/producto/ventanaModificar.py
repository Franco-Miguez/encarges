import tkinter
from tkinter import *
from baseDeDatos import conector

conector = conector.Conector()


class ModificarProducto:
    def __init__(self, id):
        self.ventanaSecundaria = Toplevel()
        self.ventanaSecundaria.geometry("500x500")
        self.id = id

    def ventana(self):

        titulo = Label(self.ventanaSecundaria, text="Agregar")
        titulo.config(font=("Arial",20))
        titulo.pack(side=TOP, anchor=CENTER)

        informacionProducto = conector.mostrarLinea("productos","nombre",self.id)

        self.valorNombreInicial = informacionProducto[0][1]
        self.valorDescripcionInicial = informacionProducto[0][2]
        self.valorPrecioInicial = informacionProducto[0][3]

        self.valorNombre = StringVar()
        self.valorNombre.set(self.valorNombreInicial)
        self.valorPrecio = DoubleVar()
        self.valorPrecio.set(self.valorPrecioInicial)

        self.textoNombre = Label(self.ventanaSecundaria, text="Nombre: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria,  width=50, textvariable=self.valorNombre).pack(side=TOP, anchor=W, padx=30, pady=10, ipady=5)


        self.textoPrecio = Label(self.ventanaSecundaria, text="Precio: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaNombre = Entry(self.ventanaSecundaria, width=20, textvariable=self.valorPrecio).pack(side=TOP, anchor=W, padx=30, pady=10)


        self.textoDescripcion = Label(self.ventanaSecundaria, text="Descripción: ").pack(side=TOP, anchor=W, padx=30)
        self.entradaDescripcion = tkinter.Text(self.ventanaSecundaria,height=5)
        self.entradaDescripcion.insert("insert", self.valorDescripcionInicial)
        self.entradaDescripcion.pack(side=TOP, anchor=W, padx=30, pady=10)

        self.botonGuardar = Button(self.ventanaSecundaria, text="Guardar", command=self.modificar)
        self.botonCancelar = Button(self.ventanaSecundaria, text="Cancelar", command=self.cancelar)

        self.botonCancelar.pack(side=BOTTOM, anchor=CENTER, pady=10)
        self.botonGuardar.pack(side=BOTTOM, anchor=CENTER, pady=10, padx=30)


    def modificar(self):
        if self.valorDescripcionInicial != self.entradaDescripcion.get(1.0,END):
            conector.modificar("productos",
                               "descripcion",
                               self.entradaDescripcion.get(1.0,END),
                               self.valorNombreInicial)

        if self.valorPrecio != self.valorPrecioInicial:
            conector.modificar("productos",
                               "Precio",
                               self.valorPrecio.get(),
                               self.valorNombreInicial)

        if self.valorNombre != self.valorNombreInicial:
            conector.modificar("productos",
                               "nombre",
                               self.valorNombre.get(),
                               self.valorNombreInicial)

        self.ventanaSecundaria.destroy()

    def cancelar(self):
        self.ventanaSecundaria.destroy()

