def write_inventory(filename, inventory):


    with open(filename, "w") as archivo:
        for item in sorted(inventory):

            archivo.write(f"{item}:{inventory[item]}\n")