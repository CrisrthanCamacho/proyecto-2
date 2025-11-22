from menu import *

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_registro_usuario()

        elif opcion == "2":
            menu_registro_cliente()

        elif opcion == "3":
            menu_inicio_sesion()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")



main()