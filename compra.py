class Compra:
    def __init__(self, nombre, precio,cantidad ,descripcion, peidosId):
        self.nombre = nombre
        self.precio = precio
        self.cantidad =cantidad
        self.descripcion = descripcion
        self.pedidosId = peidosId

    def getNombre(self):
        return self.nombre
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getPrecio(self):
        return self.precio
    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def getCantidad(self):
        return self.cantidad
    def setCantidad(self, nuevoCantidad):
        self.cantidad = nuevoCantidad

    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self, nuevoDescripcion):
        self.descripcion = nuevoDescripcion

    def getPedidosId(self):
        return self.pedidosId