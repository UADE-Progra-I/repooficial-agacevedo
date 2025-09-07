# def comun
def multiplicar(num1, num2):
    return num1*num2

# print(multiplicar(3,5) )

# # lambda
# multiplicarLambda = lambda num1, num2 : num1*num2
# print(multiplicarLambda(3,5) )

# --------------------------
# map

calificaciones = [8, 8.5, 9, 9.75]

calificaciones_int = list(map( lambda calificacion : round(calificacion) , calificaciones  ))
print(calificaciones_int)
