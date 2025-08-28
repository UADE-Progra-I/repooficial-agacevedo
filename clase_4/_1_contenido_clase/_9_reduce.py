# Dada una lista de calificaciones, 
# se desea conocer la nota promedio del curso.

# Primero devemos importar la función del módulo functools
from functools import reduce

calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75] 
suma_calificaciones = reduce(lambda nota1, nota2 : nota1 + nota2, calificaciones)
promedio = suma_calificaciones/len(calificaciones)
print(f"Nota promedio: {promedio:.2f}")

# Se desea calcular el factorial de un número
numero = 5
lista_factorial = list(range(1,numero+1))
factorial_numero = reduce(lambda num1, num2: num1*num2, lista_factorial)
print(factorial_numero)