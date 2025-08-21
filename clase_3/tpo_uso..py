# Lista de headers para los estudiantes
estudiantes_header = ["id_estudiante", "nombre", "apellido", "email"]

# Lista de datos (matriz de alumnos)
estudiantes_datos = [
    ["Thiago", "Almada"],
    ["Agostina", "Hein"],
    ["Leandro", "Bolmaro"],
    ["Valentina", "Raposo"],
]


# Lista de headers para los cursos
cursos_header = ["id_curso", "curso_nombre", "campus", "dia", "hora"]

# Lista de datos (matriz de cursos)
cursos_datos = [
    [34069, "Fundamentos de Informatica", "Monserrat", "miercoles", "18:30"],
    [34071, "Programacion I", "Monserrat", "jueves", "18:30"],
    [31051, "Algebra", "Monserrat", "lunes", "18:30"],
]


# Lista de headers para asistencia
headers_asistencia = ["id_estudiante", "id_curso", "asistencia"]

# Lista de datos (matriz de registros de asistencia)
datos_asistencia = [
    [1, 34069, [True, True]],
    [2, 34069, [True, False]],
    [3, 34069, [False, True]],
    [4, 34069, [True, True]],
    [1, 34071, [True, True]],
    [2, 34071, [True, True]],
    [3, 34071, [True, True]],
    [4, 34071, [True, True]],
    [1, 31051, [True, True]],
    [2, 31051, [False, True]],
    [3, 31051, [True, True]],
    [4, 31051, [False, True]],
]
