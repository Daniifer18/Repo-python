# Herencia

class Vehiculo:
    def __init__(self, modelo, matricula):
        self.__modelo = modelo
        self.__matricula = matricula
        
    def get_modelo(self):
        return self.__modelo
    
    def get_matricula(self):
        return self.__matricula
    
    def estadisticas(self):
        print(f"El modelo {self.__modelo} , su matricula es {self.__matricula}")
        
        
class Coche(Vehiculo):
    def __init__(self,modelo, matricula, plazas, autonomia,velocidad):
        self.__modelo = modelo
        self.__matricula = matricula
        self.__plazas = plazas
        self.__autonomia = autonomia
        self.__velocidad = velocidad
        
    def get_plazas(self):
        return self.__plazas
    
    def get_autonomia(self):
        return self.__autonomia
    
    def get_velocidad(self):
        return self.__velocidad
    
    def estadisticas(self):
        print(f"El modelo {self.__modelo}, su matricula es {self.__matricula}, tiene {self.__plazas} plazas, una autonomia de {self.__autonomia} km y una velocidad maxima de {self.__velocidad} km/h ")
        
        
BMV = Coche("X5","1982 JJB",5,600,220)

BMV.estadisticas()
        
