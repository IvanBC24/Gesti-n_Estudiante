def registrar_nota(estudiante, curso, nota):
    """Registra una calificación para un estudiante en un curso."""
    if curso in estudiante.cursos:
        estudiante.cursos[curso].append(nota)
        print(f"Calificación {nota} agregada para {estudiante.nombre} en {curso}.")
    else:
        print(f"El estudiante no está inscrito en el curso {curso}.")
