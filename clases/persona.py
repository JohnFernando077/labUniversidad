class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def correr(self):
        return f"Usted {self.nombre} tiene {self.edad} años de edad, su sexo es {self.sexo} y está corriendo."
persona1 = Persona("John Calle", 28, "masculino")
print(persona1.correr())
 