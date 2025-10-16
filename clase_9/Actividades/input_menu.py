# --------------------------------------------------------
# Actividad manejo de excepciones
# --------------------------------------------------------
"""
1. Analizar que sucede cuando se ingresan opciones o caracteres
no contemplados en el menú
2. Raise exceptions cuando se ingrese un caracter no válido
3. Agregar manejo de excepciones para no interrumpir el flujo del programa

"""

def main():
    imprimir_menu()
    try:
        opcion = get_opcion()
        print(f"Opción elegida: {opcion}")
    except Exception as e:
        print(e)



def imprimir_menu():    
    print("OPCIONES DISPONIBLES")
    print("")
    print("1-Agregar Producto")
    print("2-Listar Producto")
    print("3-Actualizar Producto")
    print("4-Eliminar Producto")
    print("5-Ingreso de Stock")
    print("0-Salir")

def get_opcion():
    opcion_elegida = int(input("Ingresar opcion: "))
    return opcion_elegida

if __name__ == "__main__":
    main()