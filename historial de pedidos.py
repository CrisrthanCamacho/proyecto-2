# ==============================================
# SISTEMA DE COSTURERÍA - HISTORIAL DE PEDIDOS
# Versión con Programación Orientada a Objetos
# ==============================================


# -------------------------------
# CLASE PEDIDO
# -------------------------------
class Pedido:
    def __init__(self, cliente, prenda, tela, fecha_registro, fecha_entrega):
        self.cliente = cliente
        self.prenda = prenda
        self.tela = tela
        self.fecha_registro = fecha_registro
        self.fecha_entrega = fecha_entrega
        self.estado = "En confección"

    def __str__(self):
        return (f"Cliente: {self.cliente} | Prenda: {self.prenda} | Tela: {self.tela} | "
                f"Estado: {self.estado} | Registro: {self.fecha_registro} | "
                f"Entrega: {self.fecha_entrega}")


# -------------------------------
# CLASE QUE MANEJA TODOS LOS PEDIDOS
# -------------------------------
class SistemaPedidos:
    def __init__(self):
        self.pedidos = []

    # 1. Registrar pedido
    def registrar_pedido(self):
        print("\n --- REGISTRAR NUEVO PEDIDO ---")
        cliente = input("Nombre del cliente: ")
        prenda = input("Tipo de prenda: ")
        tela = input("Tipo de tela: ")
        fecha_registro = input("Fecha de registro (dd/mm/aaaa): ")
        fecha_entrega = input("Fecha de entrega (dd/mm/aaaa): ")

        nuevo = Pedido(cliente, prenda, tela, fecha_registro, fecha_entrega)
        self.pedidos.append(nuevo)
        print(" Pedido registrado exitosamente.")

    # 2. Ver pedidos
    def ver_pedidos(self):
        print("\n --- LISTA DE PEDIDOS ---")
        if not self.pedidos:
            print("No hay pedidos registrados.")
        else:
            for i, p in enumerate(self.pedidos, start=1):
                print(f"{i}. {p}")

    # 3. Buscar pedido
    def buscar_pedido(self):
        print("\n --- BUSCAR PEDIDO POR CLIENTE ---")
        nombre = input("Ingrese el nombre del cliente: ").lower()

        encontrados = [p for p in self.pedidos if p.cliente.lower() == nombre]

        if encontrados:
            print(f"\nPedidos encontrados para {nombre}:")
            for p in encontrados:
                print(f"- {p.prenda} | Tela: {p.tela} | Estado: {p.estado} | Entrega: {p.fecha_entrega}")
        else:
            print(" No se encontraron pedidos para ese cliente.")

    # 4. Cambiar estado
    def cambiar_estado_pedido(self):
        print("\n --- CAMBIAR ESTADO DE PEDIDO ---")
        nombre = input("Ingrese el nombre del cliente: ").lower()

        for p in self.pedidos:
            if p.cliente.lower() == nombre:
                print(f"Pedido encontrado: {p.prenda} | Estado actual: {p.estado}")
                nuevo_estado = input("Nuevo estado (En costura / Plancha / Entregado): ")
                p.estado = nuevo_estado
                print(" Estado actualizado correctamente.")
                return
        print(" Pedido no encontrado.")

    # 5. Eliminar pedido
    def eliminar_pedido(self):
        print("\n --- ELIMINAR PEDIDO ---")
        nombre = input("Ingrese el nombre del cliente: ").lower()

        for p in self.pedidos:
            if p.cliente.lower() == nombre:
                self.pedidos.remove(p)
                print(" Pedido eliminado exitosamente.")
                return
        print(" No se encontró un pedido con ese nombre.")

    # 6. Menú principal
    def menu(self):
        while True:
            print("\n===== MÓDULO: HISTORIAL DE PEDIDOS (POO) =====")
            print("1. Registrar nuevo pedido")
            print("2. Ver todos los pedidos")
            print("3. Buscar pedido por cliente")
            print("4. Cambiar estado de pedido")
            print("5. Eliminar pedido")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_pedido()
            elif opcion == "2":
                self.ver_pedidos()
            elif opcion == "3":
                self.buscar_pedido()
            elif opcion == "4":
                self.cambiar_estado_pedido()
            elif opcion == "5":
                self.eliminar_pedido()
            elif opcion == "6":
                print(" Saliendo del sistema de pedidos...")
                break
            else:
                print(" Opción no válida.")


# -------------------------------
# EJECUCIÓN PRINCIPAL
# -------------------------------
if __name__ == "__main__":
    sistema = SistemaPedidos()
    print(" Bienvenido al sistema de Costurería - Historial de Pedidos (POO)")
    sistema.menu()
