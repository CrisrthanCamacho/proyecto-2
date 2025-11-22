# ==========================================
# CLASE CONFECCIONISTA
# ==========================================

class Confeccionista:
    contador_id = 100   # contador global de IDs

    def __init__(self, nombre):
        Confeccionista.contador_id += 1
        self.id = Confeccionista.contador_id
        self.nombre = nombre
        self.pedidos = []  # lista de pedidos asignados


# Lista global donde guardamos los confeccionistas
confeccionistas = []


# -------------------------------------------------------
# Registrar un confeccionista
# -------------------------------------------------------
def registrar_confeccionista():
    print("\n--- REGISTRAR CONFECCIONISTA ---")
    
    nombre = input("Ingrese el nombre del confeccionista: ").strip()

    nuevo = Confeccionista(nombre)
    confeccionistas.append(nuevo)

    print("\n Confeccionista registrado correctamente.")
    print(f" ID: {nuevo.id}")
    print(f" Nombre: {nuevo.nombre}\n")


# -------------------------------------------------------
# Eliminar confeccionista
# -------------------------------------------------------
def eliminar_confeccionista():
    print("\n--- ELIMINAR CONFECCIONISTA ---")

    if not confeccionistas:
        print("No hay confeccionistas registrados.\n")
        return

    for i, c in enumerate(confeccionistas, start=1):
        print(f"{i}. ID {c.id} - {c.nombre}")

    try:
        opcion = int(input("Seleccione un número para eliminar: "))
        eliminado = confeccionistas.pop(opcion - 1)
        print(f"\n Confeccionista '{eliminado.nombre}' eliminado.\n")
    except:
        print(" Opción no válida.\n")


# -------------------------------------------------------
# Ver información completa de un confeccionista
# -------------------------------------------------------
def ver_info_confeccionista():
    print("\n--- VER INFORMACIÓN DE CONFECCIONISTA ---")

    if not confeccionistas:
        print("No hay confeccionistas registrados.\n")
        return

    # Mostrar lista tipo:
    # 1. ID 101 pablo
    # 2. ID 102 mateo
    for i, c in enumerate(confeccionistas, start=1):
        print(f"{i}. ID {c.id} - {c.nombre}")

    try:
        opcion = int(input("Seleccione un confeccionista por número: "))
        seleccionado = confeccionistas[opcion - 1]
    except:
        print(" Opción no válida.\n")
        return

    # Mostrar detalles
    print("\n--- INFORMACIÓN COMPLETA ---")
    print(f" ID: {seleccionado.id}")
    print(f" Nombre: {seleccionado.nombre}")
    print(" Pedidos asignados:")

    if seleccionado.pedidos:
        for p in seleccionado.pedidos:
            print(f" - {p}")
    else:
        print("   No tiene pedidos asignados.")

    print()


# -------------------------------------------------------
# Asignar VARIOS pedidos a un confeccionista
# -------------------------------------------------------
def asignar_pedidos_confeccionista():
    print("\n--- ASIGNAR PEDIDOS A CONFECCIONISTA ---")

    if not confeccionistas:
        print("No hay confeccionistas registrados.\n")
        return

    # Mostrar lista
    for i, c in enumerate(confeccionistas, start=1):
        print(f"{i}. ID {c.id} - {c.nombre}")

    try:
        opcion = int(input("Seleccione un confeccionista por número: "))
        seleccionado = confeccionistas[opcion - 1]
    except:
        print(" Opción no válida.\n")
        return

    print("\nIngrese varios pedidos separados por coma (,)")
    print("Ejemplo: vestido rojo, camisa azul, arreglo cierre\n")

    pedidos_txt = input("Pedidos: ").strip()

    pedidos_lista = [p.strip() for p in pedidos_txt.split(",") if p.strip()]

    seleccionado.pedidos.extend(pedidos_lista)

    print(f"\n {len(pedidos_lista)} pedidos fueron asignados a {seleccionado.nombre}.\n")


# ==========================================
# MENÚ GESTIÓN DE CONFECCIONISTAS
# ==========================================
def menu_gestion_confeccionista():
    while True:
        print("\n===== MENÚ GESTION DE CONFECCIONISTAS =====")
        print("1. Registrar confeccionistas")
        print("2. Eliminar confeccionistas")
        print("3. Ver info de confeccionistas")
        print("4. Asignar pedidos a confeccionista")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_confeccionista()
        elif opcion == "2":
            eliminar_confeccionista()
        elif opcion == "3":
            ver_info_confeccionista()
        elif opcion == "4":
            asignar_pedidos_confeccionista()
        elif opcion == "5":
            print("Saliendo de gestión de confeccionistas...")
            break
        else:
            print(" Opción inválida.\n")


# Ejecutar el menú solo si es el archivo principal
if __name__ == "__main__":
    menu_gestion_confeccionista()
