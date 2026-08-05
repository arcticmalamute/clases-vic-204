precio = 8000

estudiante = (input("es un estudiante?"))
if estudiante == "si":
    descuento = precio * 0.20
    precio_final = precio - descuento
    print (f"el precio final es de: {precio_final}")
else:
    print (f"el precio final es de: {precio}")