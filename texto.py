def acortarTexto(texto, tamañoMax):
    textoNuevo = ""
    if texto != None and len(texto) - 1 > tamañoMax:
        for letra in range(tamañoMax):
            if texto[letra] != "\n":
                textoNuevo += texto[letra]
            else:
                textoNuevo += " "
        textoNuevo += "..."
        return textoNuevo
    else:
        return texto