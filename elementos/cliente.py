class Cliente:
    def __init__(self, celular, nombre, pedidos):
        self.celular = celular
        self.nombre = nombre
        self.pedidos = pedidos

    def getCelular(self):
        return self.celular
    def setCelular(self, nuevoCelular):
        self.celular = nuevoCelular

    def getNombre(self):
        return self.nombre
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getPedidos(self):
        return self.pedidos