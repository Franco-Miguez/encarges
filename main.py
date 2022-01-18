import producto
import conector

conector = conector.Conector()

print("""
Menu:
1. Agregar producto
2. Ver Productos
3. Eliminar producto
""")
eleccion = ""
while True:
    eleccion = input("Ingrese un valor: ")
    if(eleccion== "1" or eleccion=="2" or eleccion == "3"):
        break

if eleccion == "1":
    nombre = input("Nombre: ")
    descripcion = input("descripcion: ")
    precio = float(input("precio: $"))
    categoria = input("Categoria: ")
    nuevoProducto = producto.Producto(nombre, descripcion, precio, categoria)
    conector.guardar(nuevoProducto)

elif eleccion == "2":
    for articulo in conector.mostrar():
        productoAMostrar = producto.Producto(articulo[1],articulo[2],articulo[3],articulo[4])
        print (productoAMostrar.datos())
elif eleccion == "3":
    print ("##### ELIMINAR PRODUCTO #####")
    productoAEliminar = input("nombre: ")
    conector.eliminar(productoAEliminar)

