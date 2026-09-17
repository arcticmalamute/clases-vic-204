# Ejercicio 1: Recorre la lista "colores" e imprime cada uno 
# con el formato "Color: nombre"
colores = ["rojo", "azul", "verde", "amarillo"]
for colores in colores:
    print (f"colores: {colores}")

print ("-------------------------------------")

# Ejercicio 2: Recorre la lista "precios" y calcula el total 
# (suma de todos)
precios = [15000, 22000, 8000, 35000]
total = 0
for precios in precios:
    total = total + precios
    print (f"la suma total de todo es: {total}")

print ("-------------------------------------")

# Ejercicio 3: Recorre la lista "edades" y cuenta cuántas 
# personas son mayores de edad (18 o más)
edades = [15, 22, 17, 30, 12, 19]
mayores = []
for edades in edades:
    if edades > 18:
        print (f"el {edades} es mayor de edad")
        mayores.append (edades)
    else:
        print (f"el {edades} es menor de edad")
print(len(mayores))

print ("-------------------------------------")

# Ejercicio 4: Recorre la lista "notas" y encuentra la nota 
# más alta SIN usar la función max()
notas = [3.5, 4.2, 2.8, 4.8, 3.9]
mayor = notas [0]
for notas in notas:
    if notas > mayor:
        mayor = notas
print (mayor)

print ("-------------------------------------")

# Ejercicio 5: Crea una nueva lista "dobles" que contenga cada 
# número de "numeros_base" multiplicado por 2
numeros_base = [1, 2, 3, 4, 5]
dobles = []
for numeros_base in numeros_base:
    multiplicacion = numeros_base * 2
    print (f"la multiplicacion es: {multiplicacion}")
    dobles.append(multiplicacion)
print (dobles)

print ("-------------------------------------")

# Ejercicio 6: Cuenta cuántas veces aparece el valor "manzana" 
# en la lista "frutas_repetidas"
frutas_repetidas = ["manzana", "pera", "manzana", "uva", "manzana"]
repetido = []
for frutas_repetidas in frutas_repetidas:
    if frutas_repetidas == "manzana":
        repetido.append("manzana")
print ("el total de manzanas repetidas son:")
print(len(repetido))

print ("-------------------------------------")

# Ejercicio 7: Separa la lista "numeros_mixtos" en dos listas 
# nuevas: "pares" e "impares"
numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for numeros_mixtos in numeros_mixtos:
    if numeros_mixtos%2 ==0:
        pares.append(numeros_mixtos)
    else:
        impares.append(numeros_mixtos)
print (pares)
print (impares)

print ("-------------------------------------")

# Ejercicio 8: Invierte el orden de la lista "orden_original"
# Pista: pueden usar .reverse(), slicing [::-1], o investigar 
# la función .insert() para hacerlo manualmente
orden_original = ["a", "b", "c", "d", "e"]
orden_original.reverse()
print (orden_original)

print ("-------------------------------------")

# Ejercicio 9: Combina "lista_a" y "lista_b" en una sola lista 
# nueva llamada "combinada"
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
combinada = []

for lista in (lista_a, lista_b):
    for lista2 in lista:
        combinada.append(lista2)
print (combinada)