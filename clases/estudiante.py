from .persona import Persona

#clase estudiante hereda de persona
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        #Iniciando constructor de los atributos
        #metodo super trae los datos heredados de persona 
        super().__init__(nombre, edad, sexo)
        self.carnet = carnet
        self.carrera = carrera
     
    def __str__(self):
        #representacion cadena de estudiantes 
        return f"{super().__str__()}, Carnet: {self.carnet}, Carrera: {self.carrera}"
        #return f"El estudiante {self.nombre} tiene {self.edad} años de edad y su sexo es {self.sexo} su carnet es de {self.carnet} y su carrera es de {self.carrera}"

