def read_lines(filename):

    resultado = []
    with open(filename, "r") as archivo:
        for line in archivo:
            line = line.strip()
            if line != "":
                resultado.append(line)
    return resultado
