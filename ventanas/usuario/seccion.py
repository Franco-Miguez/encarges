# por el momento comente la parte donde aparece la opcion
# ver ya que más adelante lo agregare

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from baseDeDatos import conector
import ventanas.ventanaEliminar as ventanaEliminar
import ventanas.usuario.ventanaAgregar as ventanaAgregar
#import ventanas.usuario.ventanaVer as ventanaVer
import ventanas.usuario.ventanaModificar as ventanaModificar
from texto import acortarTexto


class SeccionUsuarios:
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
                                  columns=("Nombre")

                                  )

        self.lista.column("#0", width=300)
        self.lista.column("Nombre", width=400)


        self.lista.heading("#0", text="Celular", anchor=CENTER)
        self.lista.heading("Nombre", text="Nombre", anchor=CENTER)





        self.lista.pack(anchor=CENTER, side=TOP, pady=30, ipady=80)



        self.marcoBotones = Frame(self.marco, height=50)
        self.marcoBotones.pack(side=BOTTOM, fill=X, pady=40)

        self.botonAgregar = Button(self.marcoBotones, text="Agregar",
                                   command=self.agregar)

        # self.botonVer = Button(self.marcoBotones,
        #                        text="Ver",
        #                        command=self.ver)

        self.botonModificar = Button(self.marcoBotones, text="Modificar",
                                     command=self.modificar)
        self.botonEliminar = Button(self.marcoBotones, text="Eliminar",
                                    command=lambda: self.eliminar())

        self.botonAgregar.pack(side=LEFT, padx=20)
        # self.botonVer.pack(side=LEFT, padx=20)
        self.botonModificar.pack(side=LEFT, padx=20)
        self.botonEliminar.pack(side=LEFT, padx=20)


    def actualizarLista(self):
        for usuario in self.conector.mostrar("clientes"):
            self.lista.insert("", END, text=usuario[1], values=(usuario[2]))


    def eliminar(self):
        try:
            selecionado = self.selecionadoInfo()[1]
            eliminador = ventanaEliminar.Eliminar(self.marco, "clientes", selecionado, "celular")
            if eliminador.ventana():
                self.lista.delete(self.selecionadoInfo()[0])
        except IndexError:
            ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")

    def agregar(self):
        agregar = ventanaAgregar.Agregar()
        agregar.ventana()

    # def ver(self):
    #     try:
    #         productoSeleccionado = self.selecionadoInfo()[1]
    #         ver = ventanaVer.VerProducto(productoSeleccionado)
    #         ver.ventana()
    #     except IndexError:
    #         ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")


    def modificar(self):
        try:
            seleccionado = self.selecionadoInfo()[1]
            modificar = ventanaModificar.Modificar(seleccionado)
            modificar.ventana()
        except IndexError:
            ms.showinfo("Cuidado", "No a seleccionado ningun\nelemento de la lista")

    def buscar(self):
        self.lista.delete(*self.lista.get_children())
        if len(self.valorBuscar.get()) > 0:
            nuevaLista = self.conector.buscar("clientes",
                                       "celular",
                                       self.valorBuscar.get()
                                       )
            for usuario in nuevaLista:
                self.lista.insert("", END, text=usuario[1], values=(usuario[2]))
        else:
            self.actualizarLista()

    def selecionadoInfo(self):
        info = [self.lista.selection()[0]]
        info.extend([self.lista.item(self.lista.selection()[0])["text"]])
        info.extend(self.lista.item(self.lista.selection()[0])['values'])
        return info




