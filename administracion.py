# ============================
#   SISTEMA DE COSTURERÍA
#   Versión con CLASES (ID automático + asignación automática)
# ============================

empleados = []
pedidos = []
contador_id = 1       # IDs de empleados
contador_pedido = 1    # IDs de pedidos


# ------------------------------
#   CLASES
# ------------------------------

class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id = id_empleado


class Pedido:
    def __init__(self, id_pedido, descripcion, empleado_asignado=None):
        self.id_pedido = id_pedido
        self.descripcion = descripcion
        self.empleado_asignado = empleado_asignado



# ------------------------------
#   FUNCIONES DE EMPLEADOS
# ------------------------------

def registrar_empleado():
    global contador_id

    print("\n --- REGISTRAR NUEVO EMPLEADO ---")
    nombre = input("Nombre del empleado: ")

    empleado = Empleado(nombre, contador_id)
    empleados.append(empleado)

    print(f"Empleado registrado correctamente. ID asignado: {contador_id}")
    contador_id += 1



def ver_empleados():
    print("\n --- LISTA DE EMPLEADOS ---")
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for e in empleados:
            print(f"ID: {e.id} | Nombre: {e.nombre}")



def eliminar_empleado():
    print("\n --- ELIMINAR EMPLEADO ---")
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")

    if not id_empleado.isdigit():
        print("El ID debe ser un número.")
        return

    id_empleado = int(id_empleado)

    for e in empleados:
        if e.id == id_empleado:
            empleados.remove(e)
            print("Empleado eliminado exitosamente.")
            return

    print("No se encontró un empleado con ese ID.")



# ------------------------------
#   FUNCIONES DE PEDIDOS
# ------------------------------

def asignar_pedido():
    global contador_pedido

    print("\n --- CREAR Y ASIGNAR PEDIDO ---")
    descripcion = input("Descripción del pedido: ")

    if not empleados:
        print("❌ No hay empleados registrados para asignar pedidos.")
        return

    # ASIGNACIÓN AUTOMÁTICA:
    # Se asigna el PRIMER empleado de la lista
    empleado_asignado = empleados[0].nombre

    pedido = Pedido(contador_pedido, descripcion, empleado_asignado)
    pedidos.append(pedido)

    print(f"\nPedido creado correctamente.")
    print(f"ID del pedido: {contador_pedido}")
    print(f"Asignado automáticamente al empleado: {empleado_asignado}")

    contador_pedido += 1



def ver_historial_pedidos():
    print("\n --- HISTORIAL DE PEDIDOS ---")
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    for p in pedidos:
        print(f"ID Pedido: {p.id_pedido} | Descripción: {p.descripcion} | Asignado a: {p.empleado_asignado}")



def eliminar_pedido():
    print("\n --- ELIMINAR PEDIDO ---")
    id_p = input("ID del pedido: ")

    if not id_p.isdigit():
        print("ID inválido.")
        return

    id_p = int(id_p)

    for p in pedidos:
        if p.id_pedido == id_p:
            pedidos.remove(p)
            print("Pedido eliminado correctamente.")
            return

    print("No se encontró ese pedido.")



# ------------------------------
#   MENÚ PRINCIPAL
# ------------------------------

def menu_administracion():
    while True:
        print("\n===== MÓDULO DE ADMINISTRACIÓN - COSTURERÍA =====")
        print("1. Registrar empleado")
        print("2. Ver empleados")
        print("3. Eliminar empleado")
        print("4. Asignar pedido")
        print("5. Ver historial de pedidos")
        print("6. Eliminar pedido")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            ver_empleados()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            asignar_pedido()
        elif opcion == "5":
            ver_historial_pedidos()
        elif opcion == "6":
            eliminar_pedido()
        elif opcion == "7":
            print("Saliendo del módulo de administración...")
            break
        else:
            print("Opción no válida.")



if __name__ == "__main__":
    print("Bienvenido al sistema de Costurería - Administración")
    menu_administracion()