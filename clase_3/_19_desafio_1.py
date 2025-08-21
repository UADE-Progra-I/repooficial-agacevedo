# Definir la lista de estudiantes
estudiantes = [
    [101, "Ana María Fernández", 88.5],
    [102, "Luis Miguel Pérez", 92.0],
    [103, "Pedro Sánchez", 85.0],
    [104, "María José González", 90.5],
    [105, "Ana Fernández", 87.0],  # Nombre repetido con promedio diferente
    [106, "Luis Pérez", 89.0],  # Nombre repetido con promedio diferente
]

# Recortar los nombres a un máximo de 12 caracteres
estudiantes_recortados = [[id, nombre[:12], promedio] for id, nombre, promedio in estudiantes]

# Ordenar la lista por promedio (descendente) y luego por nombre (ascendente)
estudiantes_ordenados = sorted(estudiantes_recortados, key=lambda x: (-x[2], x[1]))

# Imprimir la lista ordenada con formato de f-strings
print(f"{'ID':>4} {'Nombre':<12} {'Promedio':>10}")
print("-" * 26)
for id, nombre, promedio in estudiantes_ordenados:
    print(f"{id:>4} {nombre:<12} {promedio:>10.2f}")
