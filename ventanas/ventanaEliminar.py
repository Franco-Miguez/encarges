from tkinter import messagebox
from baseDeDatos import conector

conector = conector.Conector()

class Eliminar:
    def __init__(self,marco,tabla,id,columna):
        self.marco = marco
        self.tabla = tabla
        self.id = id
        self.columna = columna

    def eliminar(self):
        respuesta =  messagebox.askyesno("ELIMINAR!!", message="¿Seguro que quieres eliminarlo?")
        if respuesta:
            conector.eliminar(self.columna,self.id,self.tabla)

        return respuesta
