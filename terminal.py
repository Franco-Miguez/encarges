import producto

class Programa:
    def __init__(self,conector):
        self.conector = conector

    def ejecutar(self):
        print("""
        Menu:
        1. Agregar producto
        2. Ver Productos
        3. Eliminar producto
        4. modificar producto
        """)
        eleccion = ""
        try:
            while True:
                eleccion = int(input("Ingrese un valor: "))
                if (eleccion > 0 and eleccion < 5):
                    break
        except NameError:
            print("Ingrese un valor numerico valido")

        if eleccion == 1:
            nombre = input("Nombre: ")
            descripcion = input("descripcion: ")
            precio = float(input("precio: $"))
            categoria = input("Categoria: ")
            nuevoProducto = producto.Producto(nombre, descripcion, precio, categoria)
            self.conector.guardarProducto(nuevoProducto)

        elif eleccion == 2:
            for articulo in self.conector.mostrar("productos"):
                productoAMostrar = producto.Producto(articulo[1], articulo[2], articulo[3], articulo[4])
                print(productoAMostrar.datos())
        elif eleccion == 3:
            print("##### ELIMINAR PRODUCTO #####")
            productoAEliminar = input("nombre: ")
            self.conector.eliminar(productoAEliminar, "productos")
        elif eleccion == 4:
            print("##### MODIFICAR PRODUCTO #####")
            for articulo in self.conector.mostrar("productos"):
                print("\n- " + articulo[1])
            nombre = input("Nombre: ")
            columna = input("elije la seccion a modificar: ")
            nuevoValor = input("Ingrese la nueva modificación: ")
            self.conector.modificar(nombre, columna, nuevoValor, "productos")
