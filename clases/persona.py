class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def __str__(self):
        return f"{self.nombre} de {self.edad} años de edad, de sexo {self.sexo}"
    
    def correr(self):
        return f"Usted {self.nombre} tiene {self.edad} años de edad, su sexo es {self.sexo} y está corriendo."

persona0 = Persona("Juan", 20, "Hombre")
print(persona0)
persona1 = Persona("John Calle", 28, "masculino")
print(persona1.correr())
 