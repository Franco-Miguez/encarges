from tkinter import *

class Programa:

    def __init__(self,conector):
        self.conector = conector
        self.titulo = "Encarges"
        self.dimenciones = "1000x700"
        self.rescalable = False

    def ejecutar(self):
        self.ventana = Tk()
        self.ventana.title(self.titulo)
        self.ventana.geometry(self.dimenciones)
        if self.rescalable:
            self.ventana.resizable(1,1)
        else:
            self.ventana.resizable(0,0)




    def mostrar(self):
        self.ventana.mainloop()

    def Secciones(self):
        marcoSecciones = Frame(self.ventana,
                               height=40
                               )
        marcoSecciones.config(bg="grey")
        marcoSecciones.pack_propagate(False)

        self.textoSeccion = StringVar()
        self.seccionProductos()

        botonProductos = Button(marcoSecciones,
                                text="Productos",
                                command=self.seccionProductos
                                )
        botonCompra = Button(marcoSecciones,
                             text="Compra",
                             command=self.seccionCompra
                             )
        botonPedidos = Button(marcoSecciones,
                              text="Pedidos",
                              command=self.seccionPedidos
                              )
        botonUsuarios = Button(marcoSecciones,
                               text="Usuarios",
                               command=self.seccionUsuarios
                               )

        botonProductos.pack(side=LEFT, fill=Y)
        botonCompra.pack(side=LEFT, fill=Y)
        botonPedidos.pack(side=LEFT, fill=Y)
        botonUsuarios.pack(side=LEFT, fill=Y)

        Label(marcoSecciones,
              textvariable=self.textoSeccion,
              font=("Arial", 20)
              ).pack(anchor=CENTER)


        marcoSecciones.pack(fill=X)

    def seccionProductos(self):
        self.textoSeccion.set("Productos")

    def seccionCompra(self):
        self.textoSeccion.set("Compra")

    def seccionPedidos(self):
        self.textoSeccion.set("Pedidos")

    def seccionUsuarios(self):
        self.textoSeccion.set("Usuarios")