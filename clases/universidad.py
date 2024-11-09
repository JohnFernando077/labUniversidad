#from .cursos import Cursos

class Universidad:
    def __init__(self, nombre, cursos=None):
        self.nombre = nombre
        self.cursos = cursos if cursos is not None else []    

    def agregar_curso(self, curso):
        #metodo para agregar cursos en la universidad
        self.cursos.append(curso)
    
    def __str__(self):
        #return  f"La universidad {self.nombre} tiene los cursos de {self.cursos}"
        cursos_str = "\n".join([str(curso) for curso in self.cursos]) 
        return f"Universidad: {self.nombre}\nCursos:\n{cursos_str if cursos_str else "no hay cursos disponibles"}"

#universidad1 = Universidad("SPOCH", ["1mer ciclo", "2do ciclo", "3er ciclo"])
#print(universidad1)    
    