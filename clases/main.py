from universidad import Universidad
from estudiante import Estudiante
from profesor import Profesor  
from cursos import Cursos


def main():
    universidad1 = Universidad("SPOCH", ["1mer ciclo", "2do ciclo", "3er ciclo"])
    persona1 = Estudiante("John Calle", 28, "hombre", "primer ciclo", "sistemas")
    profesor1 = Profesor("Ing. John Calle", 28, "hombre", "ABC123", "Matemáticas")
    curso1 = Cursos("Pimer ciclo de matematicas", "ABC123", "John Calle")
    # Imprimir la información del profesor
    print(universidad1)
    print(persona1)
    print(profesor1)
    print(curso1)
    

if __name__ == "__main__":
    main()