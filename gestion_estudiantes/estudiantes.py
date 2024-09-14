class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.cursos = {}

    def agregar_curso(self, curso):
        """Agrega un curso al estudiante."""
        self.cursos[curso] = []

# Función para agregar estudiantes
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    estudiante = Estudiante(nombre, id_estudiante)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado con éxito.")

# Función para buscar un estudiante por ID
def encontrar_estudiante(id_estudiante, estudiantes):
    for estudiante in estudiantes:
        if estudiante.id_estudiante == id_estudiante:
            return estudiante
    return None
