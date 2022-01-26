import mysql.connector

database = mysql.connector.connect(
        port= 3307,
        host= "localhost",
        user="root",
        passwd="",
        database="multicolor"
    )

cursor = database.cursor(buffered=True)

class Conector:

    def guardarProducto(self, producto):
        sql = "INSERT INTO productos (nombre,descripcion,precio,categoria) VALUES (%s,%s,%s,%s)"
        datos = (producto.getNombre(), producto.getDescripcion(),
                 producto.getPrecio(), producto.getCategoria())
        cursor.execute(sql,datos)
        database.commit()

    def guardarCliente(self, cliente):
        sql = "INSERT INTO productos (celular,nombre) VALUES (%s,%s)"
        datos = (cliente.celular, cliente.celular)
        cursor.execute(sql,datos)
        database.commit()

    def guardarPedido(self, pedido):
        sql = "INSERT INTO productos (fecha,entrega,informacion,seña,clientes_id) VALUES (%s,%s,%s,%s,%s)"
        datos = (pedido.getFecha(), pedido.getEntrega(),
                 pedido.getInformacion(), pedido.getsena(),
                 pedido.getClientesId())
        cursor.execute(sql,datos)
        database.commit()

    def guardarCompra(self, compra):
        sql = "INSERT INTO productos (nombre,precio,cantidad,descripcion,pedidos_id) VALUES (%s,%s,%s,%s,%s)"
        datos = (compra.getNombre(), compra.getPrecio(),
                 compra.getCantidad(), compra.getCantidad,
                 compra.getPedidosId())
        cursor.execute(sql,datos)
        database.commit()

    def mostrar(self,tabla):
        sql = "SELECT * FROM %s" % tabla
        cursor.execute(sql)
        return (cursor.fetchall())

    def eliminar(self,columna,id,tabla):
        sql = "DELETE FROM %s WHERE %s = '%s' " % (tabla,columna,id)
        cursor.execute(sql)
        database.commit()

    def modificar(self,nombreProducto,columnaModificar,valorNuevo,tabla):
        sql = "UPDATE %s SET %s = '%s' WHERE nombre = '%s'" % (tabla,
                                                               columnaModificar,
                                                                valorNuevo,
                                                                nombreProducto)
        cursor.execute(sql)
        database.commit()
