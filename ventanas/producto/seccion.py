from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from baseDeDatos import conector
import ventanas.ventanaEliminar as ventanaEliminar
import ventanas.producto.ventanaAgregar as ventanaAgregar
import ventanas.producto.ventanaVer as ventanaVer
import ventanas.producto.ventanaModificar as ventanaModificar
from texto import acortarTexto

class SeccionProductos:
    def __init__(self, marco):
        self.marco = marco
        self.conector = conector.Conector()

    def main(self):

        self.valorBuscar = StringVar()
        entradaBuscar = Entry(self.marco, textvariable=self.valorBuscar)
        entradaBuscar.pack(side=TOP, anchor=CENTER, ipadx=15, pady=10)
        botonBuscar = Button(self.marco, text="Buscar",
                             command=self.buscar)
        botonBuscar.pack(side=TOP, anchor=CENTER)

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
        self.marcoBotones.pack(side=BOTTOM, fill=X, pady=40)

        self.botonAgregar = Button(self.marcoBotones, text="Agregar",
                                   command=self.agregar)
        self.botonVer = Button(self.marcoBotones,
                               text="Ver",
                               command=self.ver)
        self.botonModificar = Button(self.marcoBotones, text="Modificar",
                                     command=self.modificar)
        self.botonEliminar = Button(self.marcoBotones, text="Eliminar",
                                    command=lambda: self.eliminar())

        self.botonAgregar.pack(side=LEFT, padx=20)
        self.botonVer.pack(side=LEFT, padx=20)
        self.botonModificar.pack(side=LEFT, padx=20)
        self.botonEliminar.pack(side=LEFT, padx=20)


    def actualizarLista(self):
        for producto in self.conector.mostrar("productos"):
            self.lista.insert("", END, text=producto[1], values=(producto[3],
                                                            acortarTexto(producto[2], 40),
                                                            producto[4]))


    def eliminar(self):
        try:
            productoSeleccionado = self.selecionadoInfo()[1]
            eliminador = ventanaEliminar.Eliminar(self.marco, "productos", productoSeleccionado, "nombre")
            if eliminador.ventana():
                self.lista.delete(self.selecionadoInfo()[0])
        except IndexError:
            ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")

    def agregar(self):
        agregar = ventanaAgregar.AgregarProducto()
        agregar.ventana()


    def ver(self):
        try:
            productoSeleccionado = self.selecionadoInfo()[1]
            ver = ventanaVer.VerProducto(productoSeleccionado)
            ver.ventana()
        except IndexError:
            ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")


    def modificar(self):
        try:
            productoSeleccionado = self.selecionadoInfo()[1]
            modificar = ventanaModificar.ModificarProducto(productoSeleccionado)
            modificar.ventana()
        except IndexError:
            ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")

    def buscar(self):
        self.lista.delete(*self.lista.get_children())
        if len(self.valorBuscar.get()) > 0:
            nuevaLista = self.conector.buscar("productos",
                                       "nombre",
                                       self.valorBuscar.get()
                                       )
            for producto in nuevaLista:
                self.lista.insert("", END,
                                  text=producto[1],
                                  values=(producto[3],
                                  acortarTexto(producto[2],40),
                                  producto[4]))
        else:
            self.actualizarLista()

    def selecionadoInfo(self):
        info = [self.lista.selection()[0]]
        info.extend([self.lista.item(self.lista.selection()[0])["text"]])
        info.extend(self.lista.item(self.lista.selection()[0])['values'])
        return info


