class Producto:
    nombre = ""
    descripcion = ""
    precio = 0
    categoria = ""

    def __init__(self,nombre,descripcion,precio,categoria = []):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def getCategoria(self):
        return self.categoria
    def setCategoria(self, categoria):
        self.categoria.append(categoria)

    def datos(self):
        texto = "\n#################"
        texto += "\nNombre: %s" % (self.nombre)
        texto += "\nPrecio: %s" % (self.precio)
        texto += "\nDescripcion: %s" % (self.descripcion)
        return texto





