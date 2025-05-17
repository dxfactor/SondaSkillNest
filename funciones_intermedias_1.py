matriz = [ [10, 15, 20], [3, 7, 14] ]

# Ejercicio 1
matriz[1][0] = 6
print(matriz)

# Ejercicio 2
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

# Ejercicio 3
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

# Ejercicio 4
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

# Crea la función iterarDiccionario(lista)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for i in lista:
        print(f"nombre - {i['nombre']}, pais - {i['pais']}")
        
iterarDiccionario(cantantes)

# Crea la función iterarDiccionario2(llave, lista)

def iterarDiccionario2(llave, lista):
    for i in lista:
        print(f"{i[llave]}")

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

# Crea la función imprimirInformacion(diccionario)
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Crea la función imprimirInformacion2(diccionario, llave)  
def imprimirInformacion(diccionario, llave):
    print(str(len(diccionario[llave])) + ' ' + llave.upper())
    for i in diccionario[llave]:
        print(i)
imprimirInformacion(costa_rica, "ciudades")
imprimirInformacion(costa_rica, "comidas")

