from gestion_estudiantes.estudiantes import agregar_estudiante, encontrar_estudiante
from gestion_estudiantes.cursos import agregar_curso, encontrar_curso
from gestion_estudiantes.notas import registrar_nota

# Listas para almacenar estudiantes y cursos
estudiantes = []
cursos = []

def mostrar_menu():
    """Despliega el menú y permite al usuario elegir una opción."""
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar estudiante")
        print("2. Agregar curso")
        print("3. Inscribir estudiante en curso")
        print("4. Registrar notas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            agregar_curso(cursos)
        elif opcion == "3":
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            nombre_curso = input("Ingrese el nombre del curso: ")

            estudiante = encontrar_estudiante(id_estudiante, estudiantes)
            curso = encontrar_curso(nombre_curso, cursos)

            if estudiante and curso:
                curso.inscribir_estudiante(estudiante)
                estudiante.agregar_curso(nombre_curso)
                print(f"Estudiante {estudiante.nombre} inscrito en {nombre_curso}.")
            else:
                print("Estudiante o curso no encontrado.")
        elif opcion == "4":
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            nombre_curso = input("Ingrese el nombre del curso: ")
            notas = float(input("Ingrese la nota: "))

            estudiante = encontrar_estudiante(id_estudiante, estudiantes)
            if estudiante:
                registrar_nota(estudiante, nombre_curso, notas)
            else:
                print("Estudiante no encontrado.")
        elif opcion == "5":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
