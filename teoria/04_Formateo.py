# Formateo 

name,surname,age = "Daniel","Fernández Benavente",22

print("Me llamo {} {} y tengo {} años".format(name,surname,age))
print("Me llamo %s %s y tengo %d años" %(name,surname,age))
print(f"Me llamo {name} {surname} y tengo {age} años")
print("Me llamo "+ name +" "+ surname +" y tengo "+ str(age) +" años") # No usar esta porque hay que convertir todos los valores a string
