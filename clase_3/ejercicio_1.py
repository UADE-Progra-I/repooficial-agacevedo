"""
Matrices:
Tomar una matriz previamente construida que almacene datos y ordenar sus filas
en orden ascendente basándose en una columna específica seleccionada por el usuario.

Pasos sugeridos:
1.Seleccionar la columna: pedir al usuario que ingrese el número de la columna
por la cual desea ordenar la matriz. Validar el número de columna.
2.Ordenar la matriz: Implementar una función que ordene la matriz en
forma ascendente según la columna seleccionada, aplicar métodos de ordenamiento vistos
en la materia anterior.
3.Mostrar la matriz ordenada: Implementar una función que muestre la matriz ordenada,
manteniendo el formato legible con encabezados."""

# Matriz de ejemplo con encabezados
encabezados = ["ID", "Nombre", "Edad", "Nota"]
matriz = [[1, "Ana", 22, 8.5], [2, "Luis", 20, 9.1], [3, "María", 21, 7.8], [4, "Pedro", 23, 6.9]]


def mostrar_matriz(matriz, encabezados):
    """Muestra la matriz en formato tabular."""
    print(f"{' | '.join(encabezados)}")
    print("-" * 40)
    for fila in matriz:
        print(" | ".join(str(x) for x in fila))


def ordenar_matriz(matriz, columna):
    """Ordena la matriz por la columna especificada (ascendente)."""
    return sorted(matriz, key=lambda fila: fila[columna])


# --- Programa principal ---
mostrar_matriz(matriz, encabezados)

try:
    # Pedir columna al usuario
    col = int(input(f"\nIngrese el número de columna para ordenar (0-{len(encabezados)-1}): "))

    # Validación
    if 0 <= col < len(encabezados):
        matriz_ordenada = ordenar_matriz(matriz, col)
        print(f"\nMatriz ordenada por '{encabezados[col]}':\n")
        mostrar_matriz(matriz_ordenada, encabezados)
    else:
        print("❌ Número de columna inválido")

except ValueError:
    print("❌ Debe ingresar un número entero")
