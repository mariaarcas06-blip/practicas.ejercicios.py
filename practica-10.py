productos = {"papas","coca","salame","queso"} 

while True:
    entrada = input ("ingrese un producto a buscar:")
    if entrada.lower() in productos:
        print ("producto disponible")
    else:
        print ("producto no encontrado")

    entrada2 = input ("¿desea buscar otro producto?(si/no):")
    if entrada2.lower() == "si":
        pass
    else:
        print ("programa finalizado")
        break
