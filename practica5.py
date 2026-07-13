opccion = 0

while opccion != 3: 
    print("menu")
    print ("1. sumar")
    print ("2. restar")
    print ("3 salir")

    opccion = int (input ("elija una opccion:"))

    if opccion == 1:
        num1 = float (input("ingrese el primer numero:"))
        num2 = float (input("ingrese el segundo numero:"))
        suma = num1 + num2
        print ("la suma es:",suma)

    elif opccion == 2:
        num1 = float (input("ingrese el primer numero:"))
        num2 = float (input("ingrese el segundo numero:"))
        resta = num1 - num2 
        print ("la resta es:", resta)

    elif opccion == 3:
        print ("programa finalizado.")

    else: 
        print ("opccion invalida. intente nuevamente.")
        

