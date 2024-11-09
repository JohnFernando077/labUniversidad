from clases.cursos import Cursos
from clases.profesor import Profesor
from clases.universidad import Universidad
from clases.estudiante import Estudiante

def main():
    # Crear una universidad
    universidad1 = Universidad("Universidad el Salvador")

    # Crear profesores
    profesor1 = Profesor("Ing. John Calle", 28, "masculino", "ABC123", "Matemáticas")
    profesor2 = Profesor("Ing. Juan Lopez", 30, "masculino", "ABD456", "Física")
    profesor3 = Profesor("Doc. Leo Lopez", 35, "femenino", "AZC976", "Biología")

    # Crear cursos asignados a los profesores
    curso_matematicas = Cursos("Matemáticas", "AXS126", profesor1)
    curso_fisica = Cursos("Física", "ACV465", profesor2)
    curso_biologia = Cursos("Biología", "AXS126", profesor3)

    # Agregar cursos a la universidad
    universidad1.agregar_curso(curso_matematicas)
    universidad1.agregar_curso(curso_fisica)
    universidad1.agregar_curso(curso_biologia)

    # Crear un estudiante
    estudiante_carlos = Estudiante("Carlos Perez", 20, "masculino", 202010101, "Ingeniería de Sistemas")

    # Imprimir la información
    print(universidad1)
    print("___________________")
    print(estudiante_carlos)
    print("___________________")
    print(profesor1)
    print("___________________")
    print(curso_matematicas)

if __name__ == "__main__":
    main()
