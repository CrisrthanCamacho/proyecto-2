from menu import *


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_registro()

        elif opcion == "2":
            menu_inicio_sesion()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")



main()