class Profesor:
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return (f"Profesor: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, "
                f"Código: {self.codigo}, Especialidad: {self.especialidad}")

        
        