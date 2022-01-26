import compra

class pedido:
    def __init__(self, fecha, entrega, informacion, sena, compras, clientesId):
        self.fecha = fecha
        self.entrega = entrega
        self.informacion = informacion
        self.sena = sena
        self.compras = compras
        self.clientesId = clientesId

    def getFecha(self):
        return self.fecha
    def setFecha(self, nuevoFecha):
        self.fecha = nuevoFecha

    def getEntrega(self):
        return self.entrega
    def setEntrega(self, nuevoEntrega):
        self.entrega = nuevoEntrega

    def getInformacion(self):
        return self.informacion
    def setInformacion(self, nuevoInformacion):
        self.informacion = nuevoInformacion

    def getsena(self):
        return self.sena
    def setSena(self, nuevoSena):
        self.sena = nuevoSena

    def getCompras(self):
        return self.compras

    def getClientesId(self):
        return self.clientesId