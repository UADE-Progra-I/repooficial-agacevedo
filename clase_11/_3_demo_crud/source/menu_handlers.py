import services
import print_console
import input_handlers
import sys

def handle_opcion_1():
    try:
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
    except FileNotFoundError:
        print_console.print_warning("Debe primero crear un registro")
    except Exception as e:
        print_console.print_error(e)

def handle_opcion_3():
    try:
        estudiante = input_handlers.input_estudiante()
        services.add_estudiante(estudiante)
        print_console.print_success("Estudiante agregado exitosamente")
    except Exception as e:
        print_console.print_error(e)

def handle_opcion_5():
    try:
        # Listamos los usuarios
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
        # Usuario ingresa el id a eliminar
        id_estudiante = input_handlers.input_id_estudiante()
        # Buscamos el estudiante en el storage
        estudiante = services.get_estudiante_by_id(id_estudiante)
        if not estudiante:
            print_console.print_error("No se ha encontrado coincidencia para ese ID")
            return
        else:
            print_console.print_estudiante(estudiante)
            confirma_eliminar_estudiante = input_handlers.input_confirma_eliminar_estudiante()
            if confirma_eliminar_estudiante:
                services.delete_estudiante_by_id(id_estudiante)
                print_console.print_success("Estudiante eliminado exitosamente")
    except Exception as e:
        print_console.print_error(e)
