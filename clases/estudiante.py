from persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.carnet = carnet
        self.carrera = carrera
     
    def __str__(self):
        return f"El estudiante {self.nombre} tiene {self.edad} años de edad y su sexo es {self.sexo} su carnet es de {self.carnet} y su carrera es de {self.carrera}"

#persona1 = Estudiante("John Calle", 28, "hombre", "primer ciclo", "sistemas")
#print(persona1)