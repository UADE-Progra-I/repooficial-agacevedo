from _9_crear_normal import *
from _10_metodos_plot import *
from _5_metodos_multiplicar import *
from _4_metodos_sumar import *
from _5_metodos_multiplicar import *


matriz1 = crear_matriz_normal(7, 7)
matriz2 = crear_matriz_normal(30, 30)
matriz3 = sumar_matrices(matriz1, matriz2)
matriz4 = matriz_por_escalar(matriz1, 5)
matriz5 = matriz_por_matriz(matriz1, matriz2)
matriz6 = crear_matriz_random(30, 30)
plot_matriz(matriz6)
