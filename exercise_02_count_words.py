
def count_words(filename):
    diccionario = {}

    with open(filename, "r") as archivo:
        contenido = archivo.read()
        lista = contenido.split()
        for palabra in lista:
            palabra = palabra.lower()
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1



    return diccionario