from tkinter import *
import ventanas.producto.seccion as seccionProductos

class Programa:

    def __init__(self):
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




    def mostrarVentana(self):
        self.ventana.mainloop()

    def Secciones(self):
        self.marcoSecciones = Frame(self.ventana,
                               height=40
                               )
        self.marcoSecciones.config(bg="grey")
        self.marcoSecciones.pack_propagate(False)

        self.marcoHerramientas = Frame(self.ventana,
                                  height=660)
        self.marcoHerramientas.config(bg="green")
        self.marcoHerramientas.pack_propagate(False)
        self.marcoHerramientas.pack(fill=X, side=BOTTOM)
        self.marcoSecciones.pack(fill=X)

        self.textoSeccion = StringVar()


        self.botonProductos = Button(self.marcoSecciones,
                                text="Productos",
                                command=self.seccionProductos,
                                state=DISABLED
                                )
        self.botonCompra = Button(self.marcoSecciones,
                             text="Compra",
                             command=self.seccionCompra
                             )
        self.botonPedidos = Button(self.marcoSecciones,
                              text="Pedidos",
                              command=self.seccionPedidos
                              )
        self.botonUsuarios = Button(self.marcoSecciones,
                               text="Usuarios",
                               command=self.seccionUsuarios
                               )

        self.seccionProductos()

        self.botonProductos.pack(side=LEFT, fill=Y)
        self.botonCompra.pack(side=LEFT, fill=Y)
        self.botonPedidos.pack(side=LEFT, fill=Y)
        self.botonUsuarios.pack(side=LEFT, fill=Y)

        Label(self.marcoSecciones,
              textvariable=self.textoSeccion,
              font=("Arial", 25)
              ).pack(anchor=CENTER)






    def seccionProductos(self):
        self.limpiarMarco(self.marcoHerramientas)
        self.textoSeccion.set("Productos")
        self.botonProductos['state'] = DISABLED
        self.botonCompra["state"] = NORMAL
        self.botonPedidos["state"] = NORMAL
        self.botonUsuarios["state"] = NORMAL
        secProductos = seccionProductos.SeccionProductos(self.marcoHerramientas)
        secProductos.main()
        secProductos.actualizarLista()

    def seccionCompra(self):
        self.limpiarMarco(self.marcoHerramientas)
        self.textoSeccion.set("Compra")
        self.botonProductos["state"] = NORMAL
        self.botonCompra["state"] = DISABLED
        self.botonPedidos["state"] = NORMAL
        self.botonUsuarios["state"] = NORMAL

    def seccionPedidos(self):
        self.limpiarMarco(self.marcoHerramientas)
        self.textoSeccion.set("Pedidos")
        self.botonProductos["state"] = NORMAL
        self.botonCompra["state"] = NORMAL
        self.botonPedidos["state"] = DISABLED
        self.botonUsuarios["state"] = NORMAL

    def seccionUsuarios(self):
        self.limpiarMarco(self.marcoHerramientas)
        self.textoSeccion.set("Usuarios")
        self.botonProductos["state"] = NORMAL
        self.botonCompra["state"] = NORMAL
        self.botonPedidos["state"] = NORMAL
        self.botonUsuarios["state"] = DISABLED

    def limpiarMarco(self,marco):
        for elementos in marco.winfo_children():
            elementos.destroy()

