def read_sales(filename):

    dic = {}
    with open(filename, "r") as archivo:
        contenido = archivo.read()
        contenido = contenido.split(";")
        for partes in contenido:
            if partes == "":
                continue
            partes = partes.split(":")

            if partes[0] in dic:
                dic[partes[0]].append(float(partes[-1]))
            else:
                dic[partes[0]] = [float(partes[-1])]
    return dic

def process_sales(data):

    for producto in data:
        lista = data[producto]
        suma = sum(lista)
        avg = suma / len(lista)
        print(f"{producto}: ventas totales ${suma:.2f}, promedio ${avg:.2f}")

