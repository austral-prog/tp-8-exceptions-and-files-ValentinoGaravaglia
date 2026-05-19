def grades_stats(filename):

    diccionario = {}
    with open(filename, "r") as archivo:
        for line in archivo:
            valores = line.split(":")
            estudiante = valores[0]
            for notas in valores[1:]:
                nota = []
                for n in notas.split(","):
                    nota.append(float(n))

                suma = sum(nota)
                avg = suma / len(nota)
                maximo = max(nota)
                minimo = min(nota)
                diccionario[estudiante] = (avg, maximo, minimo)

        return diccionario

