# Sets son arrays sin datos repetidos y no es una estructura ordenada

nuevoSet = set() 

print(type(nuevoSet))

otroSet = {"Pepe","Flores",24}
print(type(otroSet))

nuevoSet.add(1)
nuevoSet.add(2)
nuevoSet.add(51)

print(nuevoSet)

print(nuevoSet.union(otroSet).union("Jose","py"))