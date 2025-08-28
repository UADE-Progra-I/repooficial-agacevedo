from _2_metodos_mostrar import *

matriz_grupos = []
matriz_integrantes = [[5, 4, 3]]

for i in range(0, 29, 5):
    for j in range(0, 29, 4):
        for k in range(0, 31, 3):
            if i == 0 or j == 0 or k == 0:
                continue
            if (i + j + k) == 29:
                matriz_grupos.append([i / 5, j / 4, k / 3])


print("Matriz de integrantes:\n")
mostrar_matriz(matriz_integrantes)

print("\nMatriz de grupos:")
mostrar_matriz(matriz_grupos)
