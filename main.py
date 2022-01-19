import producto
import conector

conector = conector.Conector()

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
        if(eleccion > 0 and eleccion < 5):
            break
except NameError:
    print("Ingrese un valor numerico valido")


if eleccion == 1:
    nombre = input("Nombre: ")
    descripcion = input("descripcion: ")
    precio = float(input("precio: $"))
    categoria = input("Categoria: ")
    nuevoProducto = producto.Producto(nombre, descripcion, precio, categoria)
    conector.guardar(nuevoProducto)

elif eleccion == 2:
    for articulo in conector.mostrar():
        productoAMostrar = producto.Producto(articulo[1],articulo[2],articulo[3],articulo[4])
        print (productoAMostrar.datos())
elif eleccion == 3:
    print ("##### ELIMINAR PRODUCTO #####")
    productoAEliminar = input("nombre: ")
    conector.eliminar(productoAEliminar)
elif eleccion == 4:
    print ("##### MODIFICAR PRODUCTO #####")
    for articulo in conector.mostrar():
        print("\n- " + articulo[1])
    nombre = input("Nombre: ")
    columna = input("elije la seccion a modificar: ")
    nuevoValor = input("Ingrese la nueva modificación: ")
    conector.modificar(nombre, columna, nuevoValor)
