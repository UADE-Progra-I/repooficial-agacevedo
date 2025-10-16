import print_console
import read_console
import menu_handlers

def main():

    while True:
        print_console.print_menu()
        opcion = read_console.get_menu_opcion()
        match opcion:
            case "1":
                menu_handlers.handle_opcion_1()
            case "2":
                print("buscar estudiante por legajo")
            case "3":
                menu_handlers.handle_opcion_3()
            case "4":
                print("editar estudiante")
            case "5":
                menu_handlers.handle_opcion_5()
            case "6":
                break

    print(f"Gracias por usar nuestra APP")



if __name__ == "__main__":
    main()