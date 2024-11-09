from .profesor import Profesor

class Cursos:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor  # Aquí, `profesor` es un objeto de la clase `Profesor`
        

    def __str__(self):
        return (f"Curso: {self.nombre}, Código: {self.codigo}, "
                f"Profesor: {self.profesor.nombre} - {self.profesor.especialidad}")
