# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  DEMO: Métodos
# ---------------------------------------------------------------------

# Importamos las librerías necesarias
import random
from functools import reduce


# Declaración de funciones
def simular_asistencias(est_curso, n_clases):
    """
    Param_1: matriz est_curso
    Param_2: cantidad de asistencias a simular
    Return: nada, recibe lista por referencia
    """
    for item in est_curso:
        item.append([True if random.randint(0, 1) == 1 else False for _ in range(n_clases)])


def computar_asistencias(est_cursos_asistencias):
    """
    Param_1: matriz est_curso con las asistencias simuladas
    Return: una nueva lista, con el cómputo de las asistencias
    """
    computo_asistencias = []
    for item in est_cursos_asistencias:
        computo1 = []
        computo1.extend(item[:2])
        computo1.append(reduce(lambda a, b: a + b, item[-1]))
        computo_asistencias.append(computo1)
    return computo_asistencias


def computar_asistencias_map(est_cursos_asistencias):
    """
    Param_1: matriz est_curso con las asistencias simuladas
    Return: una nueva lista, con el cómputo de las asistencias
    """
    computo_asistencias = list(
        map(lambda item: [item[0], item[1], reduce(lambda a, b: a + b, item[-1])], est_cursos_asistencias)
    )
    return computo_asistencias


def get_curso_nombre(curso_id, cursos):
    """
    Param_1: id del curso a convertir
    Param_2: matriz de cursos
    Return: str con el nombre del curso o none si no encuentra
    """
    return next((curso[1] for curso in cursos if curso[0] == curso_id), None)


def get_estudiante_nombre(estudiante_id, estudiantes):
    """
    Param_1: id del estudiante a convertir
    Param_2: matriz de estudiantes
    Return: str con el nombre del estudiante o none si no encuentra
    """
    return next(
        (" ".join(estudiante[1:3]) for estudiante in estudiantes if estudiante[0] == estudiante_id), None
    )


def generar_reporte_asistencia(computo_asistencias, cursos, estudiantes):
    """
    Param_1: el computo de las asistencias
    Param_2: matriz de cursos
    Param_3: matriz de estudiantes
    Return: una nueva matriz, con curso_nombre, estudiante_nombre, computo_asistencia
    """
    reporte = []
    for asistencia in computo_asistencias:
        item = []
        item.append(get_curso_nombre(asistencia[0], cursos))
        item.append(get_estudiante_nombre(asistencia[1], estudiantes))
        item.append(asistencia[2])
        reporte.append(item)
    return reporte

def imprimir_reporte_asistencia(reporte_asistencia):
    """
    Param_1: la matriz de reporte
    """
    for item in reporte_asistencia:
        print(f"Curso {item[0]} - Estudiante: {item[1]} - Asistencia: {item[2]}")


