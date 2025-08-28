# 1. Introducción funciones Lambda

# Declaro una función que suma 2 parámetros
def funcionSumar(num1, num2):
    return num1 + num2


print(f"Sumando con funcionSumar {funcionSumar(2, 3)}")


# Transformamos la funcionSumar en una función lambda

lambdaSumar = lambda num1, num2: num1 + num2

print(f"Sumando con funcionLambda {lambdaSumar(2, 3)}")
