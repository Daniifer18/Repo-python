# Diccionarios funcionan como clave : valor

diccionario = {}
diccionario1 = dict()

diccionario = {
    "Nombre":"Pepe",
    "Apellidos":"Flores Abad",
    "Edad":22,
    1:"Python",
    "Lenguajes":{"C++","Java","C#"}
}

print("Pepe" in diccionario) # Esta es false y la de abajo true
print("Nombre" in diccionario) # Busca por clave no por valor
print(diccionario["Lenguajes"])
print(diccionario["Nombre"])
print(diccionario[1])

print(list(diccionario)) # Solo nos daria las claves del dict
print(tuple(diccionario)) # Solo nos daria las claves del dict
print(set(diccionario))

# Para obtener los valores habria que hacer esto 

print(list(diccionario.values()))
print(type(list(diccionario.values())))