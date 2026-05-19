def parse_log(filename):

    diccionario = {}
    with open(filename, "r") as archivo:
        contenido = archivo.readlines()
        for lineas in contenido:
            lineas = lineas.strip()
            if lineas =="":
                continue
            if ":" not in lineas:
                raise ValueError("invalid log line")
            lineas = lineas.split(":", 1)
            if lineas[0] not in diccionario:
                diccionario[lineas[0].strip()] = [lineas[1].strip()]
            elif lineas[0] in diccionario:
                diccionario[lineas[0]].append(lineas[1].strip())

    return diccionario
