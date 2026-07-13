invitados = []

while True : 
    nombre = input("ingrese el nombre del invitado(escriba ¨fin¨ para terminar):")

    if nombre == "fin":
        break
    invitados.append(nombre)

print (invitados)
print ("cantidad:", len (invitados))


