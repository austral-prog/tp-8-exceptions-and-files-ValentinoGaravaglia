def find_longest_word(filename):

    palabra_larga = ""
    with open(filename, "r") as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        for palabra in palabras:
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra
        if palabra_larga == "":
            raise ValueError("file has no words")

        return palabra_larga


