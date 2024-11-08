class Universidad:
    def __init__(self, nombre, cursos):
        self.nombre = nombre
        self.cursos = cursos if cursos else []    

    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def __str__(self):
        return  f"La universidad {self.nombre} tiene los cursos de {self.cursos}"

universidad1 = Universidad("SPOCH", ["1mer ciclo", "2do ciclo", "3er ciclo"])
print(universidad1)    
    