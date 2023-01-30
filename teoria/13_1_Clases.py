

# Clases
# La clase animal no haria nada porque no estaria implementada
class Animal:
    pass

class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def nombreCompleto(self):
        print(f"Mi nombre completo es {self.name} {self.surname}")
    
persona = Persona("Daniel","Fernández")
print(f"{persona.name} {persona.surname}")
persona.nombreCompleto()

# Atributos privados

class Animal:
    def __init__(self,nombre,numPatas,raza):
        self.__nombre = nombre
        self.__numPatas = numPatas
        self.__raza = raza
        
    def get_nombre(self):
        return self.__nombre
    
    def get_numPatas(self):
        return self.__numPatas
    
    def get_raza(self):
        return self.__raza
        
    def ficha(self):
        print(f"Raza: {self.__raza}, Nombre: {self.__nombre}, Numero de patas: {self.__numPatas}")

perro = Animal("Sergio",4,"Pastor Alemán")

perro.ficha()