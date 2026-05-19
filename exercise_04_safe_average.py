def safe_average(filename):

    lista = []
    with open(filename, "r") as archivo:
        for line in archivo:
            line = line.strip()
            if line != "":
                try:
                    numero = float(line)
                    lista.append(numero)
                except ValueError:
                    continue



        if lista == []:
            raise ValueError("no valid numbers")

        suma = sum(lista)
        avg = suma / len(lista)
        return avg



