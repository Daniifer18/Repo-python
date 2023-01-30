# Excepciones 

n1 = 1
n2 = 3
n3 = "4" 

# Esto soltaria una excepcion porque no puedes sumar un int con un string
# print(n2+n3)
# Se manejaria con esta estructura
try: 
    print(n1+n3)
    print("Suma realizada correctamente")
except:
    print("Se ha producido un error")
    
    
# Tambien hay mas clausulas

try:
    print(n1+n2)
    print("Suma realizada correctamente")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no hay ninguna excepcion
    print("La ejecucion continua correctamente")
finally:
    # Siempre se ejecuta
    print("La ejecucion continua")
    
# Mensajes del lenguaje

try: 
    print(n1+n3)
    print("Suma realizada correctamente")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)