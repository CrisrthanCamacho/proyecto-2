from pedidos import GestorPedidos
gestor_pedidos = GestorPedidos()
from prueba import GestionConfeccionistas
gestion_confeccionistas = GestionConfeccionistas()
import usuarios

usuario_actual = None

# menú inicio de sesión
def mostrar_menu_principal():
    global usuario_actual

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrarme")
    print("2. Iniciar Sesión")
    print("3. Salir")

#------------------------------------------------------------


# menu del cliente
def menu_cliente():
    while True:
        print("\n===== MENÚ CLIENTE =====")
        print("1. editar perfil")
        print("2. info de perfil")
        print("3. registrar pedido")
        print("4. lista  de pedidos")
        print("5. pagar pedido")
        print("6. anticipos de pedido")
        print("7. cancelar pedido")
        print("8. Cerrar Sesión")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            usuarios.editar_perfil(usuario_actual)
        elif opcion =="2":
            usuarios.ver_perfil(usuario_actual)
        elif opcion =="3":
            gestor_pedidos.agregar_pedido(usuario_actual)
        elif opcion =="4":
            gestor_pedidos.mostrar_pedidos_cliente(usuario_actual)
        elif opcion == "5":
            gestor_pedidos.pagar_pedido()
        elif opcion == "6":
            gestor_pedidos.mostrar_anticipos_pedido()
        elif opcion == "7":
            gestor_pedidos.cancelar_pedido()
            
        elif opcion == "8":
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
        print("3. ver clientes registrados")
        print("4. editar mi info")
        print("5. info de perfil")
        print("6. cerrar sesión")

        opcion = input("Elige una opción: ")
        
        if opcion =="1":
            menu_gestion_confeccionista()
        elif opcion =="2":
            menu_gestion_pedidos()
        elif opcion =="3":
            usuarios.ver_clientes()
        elif opcion =="4":
            usuarios.editar_perfil(usuario_actual)
        elif opcion =="5":
            usuarios.ver_perfil(usuario_actual)
        elif opcion == "6":
            print("Cerrando sesión de administrador...")
            break
        else:
            print("Opción seleccionada (sin función implementada).")

# --------------------------------------------------
           

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

# --------------------------------------------------


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




def menu_registro():
    print("\n--- Registro ---")
    print("1. Registrarme como cliente")
    print("2. Registrarme como admin")
    opcion= (input("elige una opcion"))
    if opcion == "1":
        usuarios.registrar_cliente()
        

    elif opcion == "2":
        usuarios.registrar_admin()
        
    else:
        print("opcion invalida")

# --------------------------------------------------


# inicio de sesión (prueba)
def menu_inicio_sesion():
    global usuario_actual
    print("\n--- Iniciar Sesión ---")
    print("1. iniciar sesión como cliente")
    print("2. iniciar sesión como admin")
    opcion= (input("elige una opcion"))

    if opcion == "1":
        usuario_actual = usuarios.iniciar_sesion(usuarios.clientes)
        if usuario_actual:
            menu_cliente()

    elif opcion == "2":
        usuario_actual = usuarios.iniciar_sesion(usuarios.administradores)
        if usuario_actual:
            menu_admin()
    else:
        print("opcion invalida")

#------------------------------------------------------------------------------------

#menu de registro o inicio de sesión
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
            print("Opción invalida")



main()