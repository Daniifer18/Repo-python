print("Hola mundo!!!")

# Consultar tipo de dato

a = 12
b = "Pepe"
c = 1.1
d = True

print(type(a)) # Esto nos devolvera int
print(type(a + 1j)) # Esto nos devolvera tipo complex (numeros complejos)
print(type(b)) # Esto nos devolvera tipo string
print(type(c)) # Esto nos devolvera tipo float
print(type(d)) # Esto nos devolvera tipo bool

# Decir de que tipo tiene que ser una variabe o forzar tipo

calle : int = 4
calle = "Calle Moncloa"
print(type(calle))