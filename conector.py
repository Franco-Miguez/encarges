import mysql.connector
import producto
database = mysql.connector.connect(
        port= 3307,
        host= "localhost",
        user="root",
        passwd="",
        database="multicolor"
    )

cursor = database.cursor(buffered=True)

class Conector:

    def guardar(self, producto):
        sql = "INSERT INTO productos (nombre,descripcion,Precio,categoria) VALUES (%s,%s,%s,%s)"
        datos = (producto.getNombre(), producto.getDescripcion(),
                 producto.getPrecio(), producto.getCategoria())
        cursor.execute(sql,datos)
        database.commit()

    def mostrar(self):
        cursor.execute("SELECT * FROM productos")
        return (cursor.fetchall())

    def eliminar(self,nombre):
        sql = "DELETE FROM productos WHERE nombre = '%s' " % (nombre)
        cursor.execute(sql)
        database.commit()

    def modificar(self,nombreProducto,columnaModificar,valorNuevo):
        sql = "UPDATE productos SET %s = '%s' WHERE nombre = '%s'" % (columnaModificar,
                                                                         valorNuevo,
                                                                         nombreProducto)
        cursor.execute(sql)
        database.commit()
