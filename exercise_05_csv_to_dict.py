
def csv_to_dict(filename):

    resultao = []
    with open(filename, mode = "r") as archivo:
        header = archivo.readline().strip()
        categoria = header.split(",")

        for line in archivo:
            datos = line.strip().split(",")
            diccionario = {}
            for i, valores in enumerate(categoria):
                diccionario[valores] = datos[i]
            diccionario["age"] = int(diccionario["age"])
            resultao.append(diccionario)

        return resultao
