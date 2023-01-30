# Bucles

num1 = 3
num2 = 4

# While: Se le puede añadir un else al final y es opcional

while num1 > 1:
    print(num1)
    num1 -= 1
else:
    print("El numero es menor que 0")


# For

array = [1,2,3,4,5,6,7,8]

for a in array:
    print(a)
    
# Funciones se definen al principio del programa

def saludar(nombre):
    print(f"Buenas tardes {nombre}")

def sumaNum(n1,n2):
    return n1 + n2

print(f"La suma de los numeros es:{sumaNum(2,5)}")
print(f"La suma de los numeros es:{sumaNum(-6,-4)}")
print(f"La suma de los numeros es:{sumaNum(-2,8)}")

saludar("Pepe")
saludar("Jose")
saludar("Laura")