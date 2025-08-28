# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  DEMO: Avances del Proyecto Final
# ---------------------------------------------------------------------
"""
En esta demo se contemplan "tres tablas" representadas por matrices (lista de listas)

La primera matriz estudiantes, contiene:
estudiante_id, estudiante_nombre, estudiante_apellido, estudiante_edad

La segunda matriz cursos, contiene:
curso_id, curso_nombre, campus, dia, horario

La tercer matriz, est_cursos, vincula de alguma manera las primeras dos matrices
y contiene:
curso_id, estudiante_id 
Pueden ver esta matriz, como una tabla de matriculación al curso.

Luego se generan las siguientes funciones:
simular_asistencias: agrega como tercer elemento, una lista simulada de asistencias
computar_asistencias: trabaja con la lista simulada, retornando una lista nueva con la cantidad de asistencias
computar_asistencias_map: lo mismoque computar_asistencias pero con map
get_curso_nombre: a partir del curso_id, retorna el curso_nombre
get_estudiante_nombre: a partir del curso_id, retorna el curso_nombre
generar_reporte_asistencia: genera una nueva matriz, donde cada lista contiene:
curso_nombre, estudiante_nombre, computo_asistencia
imprimir_reporte_asistencia: imprime con algún estilo el reporte en pantalla

"""
# Importamos los módulos necesarios
from metodos import *
from datos import *

def main():
    # Llamdas a función
    # 1. Simulamos las asistencias
    """
    Invocamos a la función simular_asistencias,
    no necesita retorno porque pasa la lista por referencia"""
    simular_asistencias(est_cursos, 16)

    # 2. Computamos las asistencias
    # asistencias = computar_asistencias(est_cursos)
    computo_asistencias = computar_asistencias_map(est_cursos)

    # 3. Generar reporte
    reporte_asistencia = generar_reporte_asistencia(computo_asistencias, cursos, estudiantes)
    imprimir_reporte_asistencia(reporte_asistencia)

if __name__ == "__main__":
    main()