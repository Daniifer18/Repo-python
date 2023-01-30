b = "Esternocleidomastoideo"

# Funcion len te devuelve la longitud de la cadena 
print(len(b))

# Modo de declaracion e inicializacion de variables en una linea (No abusar mucho)
nombre , apellidos , edad , alias = "Daniel","Fernández Benavente",22,"Rubio"
print("Me llamo", nombre , apellidos,".Tengo ", edad,"años. Y me llaman",alias)

# División de cadenas 

lenguaje = "Python"

print(lenguaje)
print(lenguaje[1:3])
print(lenguaje[2:5])
print(lenguaje[1:3:5])
print(lenguaje[-2]) # Te devuelve la penultima letra

# Reverse (cadena dada la vuelta)

print(lenguaje[::-1])

# Funciones de string

print(lenguaje.capitalize()) # Te devuelve la primera letra de la cadena en mayusculas y el resto en minusculas
print(lenguaje.upper()) # Te transforma la cadena a todo mayusculas
print(lenguaje.count("t")) # Te cuenta las letras que hay en la cadena y te la letra la pasas por parametro
print(lenguaje.lower()) # Te transforma la cadena a minusculas
print(lenguaje.isnumeric()) # Returna True o False si es numero te da True si no False
print("1".isnumeric())
print(lenguaje.isupper()) # Devuelve True o False tambien hay islower se basa en como este la cadena entera
print(lenguaje.startswith("Py")) # Devuelve True o False si la cadena empieza por las letras pasadas por parametro