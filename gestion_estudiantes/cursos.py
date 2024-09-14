class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes_inscritos = []

    def inscribir_estudiante(self, estudiante):
        self.estudiantes_inscritos.append(estudiante)

# Función para agregar un curso
def agregar_curso(cursos):
    nombre_curso = input("Ingrese el nombre del curso: ")
    curso = Curso(nombre_curso)
    cursos.append(curso)
    print(f"Curso {nombre_curso} agregado con éxito.")

# Función para buscar un curso por nombre
def encontrar_curso(nombre_curso, cursos):
    for curso in cursos:
        if curso.nombre_curso == nombre_curso:
            return curso
    return None
