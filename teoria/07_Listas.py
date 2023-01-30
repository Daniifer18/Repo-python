# Listas

lista = list()
lista1 = []

print(len(lista))

lista = [23,4,35,4,65768,8786,5]

print(lista)
print(len(lista))

lista1 = [1.23,3,5,6,"Pepe",True]

print(type(lista))
print(type(lista1))

# Puedes acceder a elementos por su indice siempre que existan
# Si la lista tiene 4 elementos puedes acceder hasta 3 y -4 el -1 es el 3 y el -4 es el 0 
# Si pones 4 o -4 en adelante salta un error de indice no encontrado

print(lista1[0])
print(lista1[3])
print(lista1[-1])
print(lista1[-2])

# Añadir y remover datos a una lista

lista.append("Pepe")
lista.insert(23,"Lolo")
print(lista)
lista.remove("Pepe")

print(lista)

lista.pop(4)
print(lista)

# Darle la vuelta a la lista
lista.reverse() 
print(lista)

# Ordenar la lista de un tipo de dato concreto
lis = [1,23,4,5,6,7]

lis.sort()
print(lis)