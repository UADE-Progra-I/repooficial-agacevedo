# Declaro una función que suma dos números
def sumar(a,b):
  return a+b

# Declaro una función que divide dos números
def dividir(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("El primer argumento debe ser numérico (int o float).")
    if not isinstance(b, (int, float)):
        raise TypeError("El segundo argumento debe ser numérico (int o float).")
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a/b


