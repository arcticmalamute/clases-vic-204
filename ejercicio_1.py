continuar = "s"

while (continuar == "s"):

    edad = int (input("ingrese su edad: "))
    print (f"edad: {edad}")

    dias = int (input("cuantos dias de anticipacion compro su entrada: "))
    print (f"dias: {dias}")

    if edad >= 18 and dias >=7:
        print ("su acceso es: vip")
    elif edad >= 18 or dias >=7:
        print ("su acceso es: general")
    else:
        print ("su acceso es: sin acceso")
    
    continuar = input("realizar otro calculo?: (s/n)")

print ("gracias por usar")