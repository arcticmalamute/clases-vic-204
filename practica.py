continuar = "s"

while (continuar == "s"):

    distancia_km = float(input("ingrese la distancia en km: "))

    print(f"distancia_km: {distancia_km}")

    if distancia_km <= 3:
        costo_domicilio =3000
    elif distancia_km <= 8:
        costo_domicilio = 7000
    else:
        costo_domicilio = 0

    if costo_domicilio == 0:
        print ("por fuera del area - no hay domicilios")
    else:
        print (f"costo del domicilio ${costo_domicilio}")

    continuar = input("realizar otro calculo?: (s/n)")

print ("gracias por usar")