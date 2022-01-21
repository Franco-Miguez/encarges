import producto
import conector
import entorno_grafico

conector = conector.Conector()

programa = entorno_grafico.Programa(conector)

programa.ejecutar()
programa.Secciones()
programa.mostrar()