def merge_files(file1, file2, output):

    with open(file1, "r") as archivo1:
        with open(file2, "r") as archivo2:
            contenido_1 = archivo1.read()
            contenido_2 = archivo2.read()

            with open(output, "w") as archivo3:
                archivo3.write(contenido_1 + contenido_2)