pin_correcto = 4321
saldo = 50000
intentos = 0

while intentos < 3 :
    pin = int (input("ingrese su pin:"))

    if pin == pin_correcto:
        print ("pin correcto")

        opcion = 0 

        while opcion != 3:
            print ("menu")
            print ("1. consultar saldo")
            print ("2. depositar dinero")
            print ("3. salir")

            opcion = int(input("Elija una opcion:"))

            if opcion == 1:
                print("su saldo es:",saldo)

            elif opcion == 2:
                print("operacion realizada correctamente")

            elif opcion == 3:
                print ("saliendo...")

            else:
                print ("opcion incorrecta")

            break
        else:
            print("pin incorrecto")
            intentos = intentos + 1 
if intentos == 3:
    print ("targeta bloqueada")

