from profesor import Profesor

class Cursos(Profesor):
    def __init__(self, curso, codigo, nombre):
        self.curso = curso
        self.codigo = codigo
        self.nombre = nombre
        
    def __str__(self):
        return f"El curso de {self.curso} con codigo {self.codigo} sera dictado por el docente {self.nombre}"

#curso1 = Cursos("Pimer ciclo", "ABC123", "John Calle")
#print(curso1)