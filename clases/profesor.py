from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad,sexo, codigo, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return f"El docente {self.nombre} tiene {self.edad} años de edad, su sexo es {self.sexo}, su codigo es {self.codigo} y su especialidad es {self.especialidad}"
#profesor1 = Profesor("John Calle", 28, "hombre", "ABC123", "Sistemas")
#print(profesor1)
        
        