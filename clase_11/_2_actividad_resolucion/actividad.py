
# Ejercicio 1
"""
Desarrollar la función write_productos()
que guarde una lista de listas en el archivo productos.csv del directorio data 
con formato csv.

- La función recibe como argumento una lista con los productos a persistir.
- La función persiste los datos en el archivo productos.csv.
- Debe validar que la lista de productos no esté vacía ni sea de tipo incorrecto.
- Si la validación falla, debe generar una excepción.
- Abrir el archivo en modo escritura ("w").
- Usar csv.writer() y el método writerows(data).

Ejemplo de estructura esperada:
productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00]
]
"""
print("\n\nEjercicio 1\n")

import os
import csv

productos_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),"data","productos.csv"))

def write_productos(path, data):
    if not isinstance(data,list):
        raise ValueError("[ERROR] productos no es una lista.") 
    if productos == []:
        raise ValueError("[ERROR] productos es una lista vacia.")
    
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00]
]
try:
    write_productos(productos_path, productos)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)


# Ejercicio 2

"""
Desarrollar la función read_productos()
que retorne el contenido del archivo productos.csv del directorio data
en forma de lista de listas.

- Abrir el archivo en modo lectura ("r").
- Leer su contenido usando el módulo csv.
- Retornar una lista de listas con los registros.
- Manejar el caso en que el archivo no exista (FileNotFoundError) devolviendo una lista vacía.

"""
print("\n\nEjercicio 2\n")
def read_productos(path):
    lista=[]
    with open(path, "r") as f:
        content = csv.reader(f)

        if content == None:
            return lista
        
        for _ in content:
            lista.append(_)
        return lista
    
        
try:
    a = read_productos(productos_path)
    print(a)
except FileNotFoundError:
    print("Archivo no encontrado en la ruta: ", productos_path)

# Ejercicio 3
"""
A partir de la siguiente lista de productos base:

productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00],
    [3, "Campera de Jean", "Indumentaria", 23000.00]
]

Desarrollar la función inicializar_productos()
que cree el archivo productos.csv y lo inicialice con esta lista modelo.

- Utilizar internamente la función write_productos() para persistir los datos.
- Si el archivo ya existe, debe sobrescribirse.
"""
print("\n\nEjercicio 3\n")

def inicializar_productos(path,data):
    if os.path.exists(path):
        print(f"Archivo '{path}' existente, sobreescribiendo...")
        write_productos(path, data)
    else:
        print(f"Creando Archivo '{path}' ...")
        write_productos(path, data)


productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00],
    [3, "Campera de Jean", "Indumentaria", 23000.00]
]

inicializar_productos(productos_path, productos)

try:
    a = read_productos(productos_path)
    print(a)
except FileNotFoundError:
    print("Archivo no encontrado en la ruta: ", productos_path)


# Ejercicio 4
"""
Desarrollar la función insert_productos()
que recibe una lista con los datos de un solo producto y lo inserta al final del archivo productos.csv.

- Abrir el archivo productos.csv en modo "a" (append).
- Usar csv.writer() y el método writerow(producto).
- Validar que el producto sea una lista no vacía y con 4 campos.
- Si el archivo no existe, mostrar un mensaje de error o llamar a inicializar_productos().
"""
print("\n\nEjercicio 4\n")

def insert_productos(path, data):
    try:
        if not isinstance(data, list):
            raise ValueError("Dato a ingresar incorrecto, debe ser una lista.")
        elif len(data) != 4:
            raise ValueError("Dato a insertar incorrecto, debe tener 4 campos.")

        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo '{path}' no existe.")

        with open(path, "a") as f:
            writer = csv.writer(f)
            writer.writerow(data)
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print(e)


# Ejercicio 5
"""
Desarrollar la función input_productos()
que lea por consola los datos de un nuevo producto y los almacene en una lista.

- Solicitar al usuario: nombre_producto, categoría y precio_unitario.
- Calcular el id automáticamente leyendo el último registro del archivo.
- Validar los datos ingresados (por ejemplo, precio sea numérico).
- Invocar a insert_productos() para persistir el registro en el archivo productos.csv.

Ejemplo de ejecución:
--------------------------------
Ingrese el nombre del producto: Zapatillas Urbanas
Ingrese la categoría: Calzado
Ingrese el precio unitario: 32000
Producto agregado correctamente.
--------------------------------
"""
print("\n\nEjercicio 5\n")
# Corregir para aceptar numeros con . ej: 1234.5
def input_productos(path):
    nombre_producto = input("Ingresar Nombre del Producto: ")
    if nombre_producto.isdigit(): 
        raise ValueError("Nombre ingresado incorrecto, favor de no ingresar numeros.")
    categoria_producto = input("Ingresar Categoria del Producto: ")
    if categoria_producto.isdigit(): 
        raise ValueError("Categoria ingresada incorrecta, favor de no ingresar numeros.")
    precio_producto = input("Ingresar Precio del Producto: ")
    if not precio_producto.isdigit(): 
        raise ValueError("Precio ingresado incorrecto, favor de ingresar valor numerico.")

    productos = read_productos(path)
    producto_id = int(productos[-1][0]) + 1

    lista = []
    lista.append(producto_id)
    lista.append(nombre_producto)
    lista.append(categoria_producto)
    lista.append(precio_producto)
    insert_productos(path, lista)
    

try:
    input_productos(productos_path)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)

try:
    a = read_productos(productos_path)
    print(a)
except FileNotFoundError:
    print("Archivo no encontrado en la ruta: ", productos_path)
    

# Ejercicio 6
"""
Test Unitarios con Pytest

Crear un archivo test_productos.py y escribir pruebas unitarias para las funciones:

- read_productos()
- write_productos()
- insert_productos()
- inicializar_productos()

Recomendaciones:
 Utilizar un archivo temporal (por ejemplo test_productos.csv).
 Verificar que se escriben las líneas correctas.
 Verificar que insert_productos() agrega una línea al final.
 Asegurarse de que read_productos() maneje correctamente el caso de archivo inexistente.

Ejemplo:

def test_insert_productos():
    producto = [4, "Buzo Negro", "Indumentaria", 21000.0]
    insert_productos("test_productos.csv", producto)
    data = read_productos("test_productos.csv")
    assert any(row[1] == "Buzo Negro" for row in data)
"""

print("\n\nEjercicio 6\n")
