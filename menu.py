from pedidos import GestorPedidos
gestor_pedidos = GestorPedidos()
from prueba import GestionConfeccionistas
gestion_confeccionistas = GestionConfeccionistas()
# menú inicio de sesión


def mostrar_menu_principal():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrarme como Admin")
    print("2. Registrarme como Cliente")
    print("3. Iniciar Sesión")
    print("4. Salir")

#------------------------------------------------------------


# menu del cliente


def menu_cliente():
    while True:
        print("\n===== MENÚ CLIENTE =====")
        print("1. editar perfil")
        print("2. registrar pedido")
        print("3. historial de pedidos")
        print("4. abonar pedido")
        print("5. cancelar pedido")
        print("6. pagar pedido")
        print("7. Cerrar Sesión")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("")
        elif opcion =="2":
            gestor_pedidos.agregar_pedido()
        elif opcion =="3":
            gestor_pedidos.mostrar_pedidos()
        elif opcion == "4":
            print("s")
        elif opcion == "5":
            gestor_pedidos.cancelar_pedido()
        elif opcion == "6":
            print("s")
            
        elif opcion == "7":
            print("Cerrando sesión...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")

#---------------------------------------------------------------------------


# menu de admin

def menu_admin():
    while True:
        print("\n===== MENÚ ADMINISTRADOR =====")
        print("1. gestion de confeccionistas")
        print("2. gestion de pedidos")
        print("3. editar mi info")
        print("4. cerrar sesión")

        opcion = input("Elige una opción: ")
        
        if opcion =="1":
            menu_gestion_confeccionista()
        elif opcion =="2":
            menu_gestion_pedidos()
        elif opcion =="3":
            print("")
        elif opcion == "4":
            print("Cerrando sesión de administrador...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")

           

def editar_perfil():
    while True:
        print("\n===== MENÚ DE EDDICION DE PERFIL =====")
        print("1. editar nombre")
        print("2. editar correo")
        print("3. editar contraseña")
        print("4. ver info de perfil")
        print("5. salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("s")
        elif opcion =="2":
            print("d")
        elif opcion =="3":
            print("f")
        elif opcion =="4":
            print("f")
        elif opcion == "5":
            print("saliendo de gestion de pedidos...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")


def menu_gestion_confeccionista():
    while True:
        print("\n===== MENÚ GESTION DE CONFECCIONISTAS =====")
        print("1. registrar confeccionistas")
        print("2. eliminar confeccionistas")
        print("3. ver info de confeccionistas")
        print("4. editar info de confeccionista")
        print("5. salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestion_confeccionistas.registrar_empleado()
        elif opcion =="2":
            gestion_confeccionistas.eliminar_empleado()
            
        elif opcion =="3":
            gestion_confeccionistas.ver_empleados()
        elif opcion =="4":
            gestion_confeccionistas.editar_empleado()
        elif opcion == "5":
            print("saliendo de gestion de confeccionistas...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")



def menu_gestion_pedidos():
    while True:
        print("\n===== MENÚ GESTION DE PEDIDOS =====")
        print("1. ver pedidos")
        print("2. asignar pedido")
        print("3. eliminar pedido")
        print("4. editar estado del pedido")
        print("5. salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestor_pedidos.mostrar_pedidos()
        elif opcion =="2":
            gestor_pedidos.asignar_pedido(gestion_confeccionistas)
        elif opcion =="3":
            gestor_pedidos.eliminar_pedido()
        elif opcion =="4":
            gestor_pedidos.editor.mostrar_menu_edicion(gestor_pedidos.pedidos)
        elif opcion == "5":
            print("saliendo de gestion de pedidos...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")

#------------------------------------------------------------------------------------

# registro (prueba)


def menu_registro_usuario():
    print("\n--- Registro de Usuario/Admin ---")



def menu_registro_cliente():
    print("\n--- Registro de Cliente ---")




# inicio de sesión (prueba)


def menu_inicio_sesion():
    print("\n--- Iniciar Sesión ---")
    print("1. iniciar sesión como cliente")
    print("2. iniciar sesión como admin")
    opcion= (input("elige una opcion"))

    if opcion == "1":
        print("s")
        menu_cliente()

    elif opcion == "2":
        print("")
        menu_admin()
    else:
        print("Tipo de usuario desconocido.")



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
