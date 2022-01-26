from tkinter import *
from tkinter import ttk
from baseDeDatos import conector
import ventanas.ventanaEliminar as ventanaEliminar

class SeccionProductos:
    def __init__(self, marco):
        self.marco = marco
        self.conector = conector.Conector()

    def main(self):
        labelBuscar = Label(self.marco,text="Buscar", font=("Arial",20))
        labelBuscar.pack(side=TOP, anchor=CENTER, pady=10)
        entradaBuscar = Entry(self.marco)
        entradaBuscar.pack(side=TOP, anchor=CENTER, ipadx=15)

        self.lista = ttk.Treeview(self.marco,
                                  columns=("Precio",
                                            "Descripción",
                                            "Categoria")

                                  )

        self.lista.column("#0", width=300)
        self.lista.column("Precio", width=80)
        self.lista.column("Descripción", width=400)
        self.lista.column("Categoria", width=150)

        self.lista.heading("#0", text="Nombre", anchor=CENTER)
        self.lista.heading("Precio", text="Precio", anchor=CENTER)
        self.lista.heading("Descripción", text="Descripción", anchor=CENTER)
        self.lista.heading("Categoria", text="Categoria", anchor=CENTER)




        self.lista.pack(anchor=CENTER, side=TOP, pady=30, ipady=80)



        self.marcoBotones = Frame(self.marco, height=50)
        self.marcoBotones.config(bg="grey")
        self.marcoBotones.pack(side=BOTTOM, fill=X, pady=40)

        self.botonAgregar = Button(self.marcoBotones, text="Agregar")
        self.botonVer = Button(self.marcoBotones, text="Ver")
        self.botonModificar = Button(self.marcoBotones, text="Modificar")
        self.botonEliminar = Button(self.marcoBotones, text="Eliminar",
                                    command=lambda: self.eliminar())

        self.botonAgregar.pack(side=LEFT, padx=20)
        self.botonVer.pack(side=LEFT, padx=20)
        self.botonModificar.pack(side=LEFT, padx=20)
        self.botonEliminar.pack(side=LEFT, padx=20)


    def actualizarProductos(self):
        for producto in self.conector.mostrar("productos"):
            self.lista.insert("", END, text=producto[1], values=(producto[3],
                                                            producto[2],
                                                            producto[4]))


    def eliminar(self):
        productoSeleccionado = self.selecionadoInfo()[1]
        eliminador = ventanaEliminar.Eliminar(self.marco, "productos", productoSeleccionado, "nombre")
        if eliminador.eliminar():
            self.lista.delete(self.selecionadoInfo()[0])

    def agregar(self):
        pass


    def selecionadoInfo(self):
        info = [self.lista.selection()[0]]
        info.extend([self.lista.item(self.lista.selection()[0])["text"]])
        info.extend(self.lista.item(self.lista.selection()[0])['values'])

        return info
