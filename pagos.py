
class Pedido:
    def __init__(self, id_pedido, descripcion, precio_unitario=None):
        self.id_pedido = id_pedido
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.anticipos = []

    def agregar_anticipo(self, monto, metodo):
        self.anticipos.append({"monto": monto, "metodo": metodo})
        print(f"Anticipo de {monto} registrado con {metodo}.")

    def total_anticipos(self):
        return sum(p["monto"] for p in self.anticipos)


class GestorPagos:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def abonar_pedido(self):
        if not self.pedidos:
            print("No hay pedidos para abonar.")
            return

        try:
            id_pedido = int(input("Ingrese el ID del pedido a abonar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in self.pedidos if p.id_pedido == id_pedido), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        if pedido.precio_unitario is None:
            print("El precio del pedido aún no está definido. El admin debe establecerlo primero.")
            return

        try:
            monto = float(input("Ingrese el monto del anticipo: "))
        except ValueError:
            print("Monto inválido.")
            return

        print("Seleccione método de pago:")
        print("1. Nequi")
        print("2. Bancolombia")
        opcion = input("Opción: ")
        if opcion == "1":
            metodo_pago = "Nequi"
        elif opcion == "2":
            metodo_pago = "Bancolombia"
        else:
            print("Opción inválida.")
            return

        pedido.agregar_anticipo(monto, metodo_pago)

    def mostrar_anticipos(self, pedido):
        if not pedido.anticipos:
            print("No hay anticipos realizados.")
            return

        print(f"\nAnticipos del pedido {pedido.id_pedido} ({pedido.descripcion}):")
        for pago in pedido.anticipos:
            print(f"Monto: {pago['monto']} | Método: {pago['metodo']}")
        print(f"Total abonado: {pedido.total_anticipos()}")


def mostrar_menu():
    print("\n=== MENÚ DE GESTIÓN DE PAGOS ===")
    print("1. Abonar un pedido")
    print("2. Mostrar anticipos de un pedido")
    print("3. Listar todos los pedidos")
    print("4. Salir")
    return input("Seleccione una opción: ")


def main():
    # Pedidos de ejemplo
    pedidos = [
        Pedido(1, "Producto A", 100),
        Pedido(2, "Producto B", 200),
        Pedido(3, "Producto C")  # Precio no definido aún
    ]

    gestor = GestorPagos(pedidos)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            gestor.abonar_pedido()
        elif opcion == "2":
            try:
                id_pedido = int(input("Ingrese el ID del pedido: "))
            except ValueError:
                print("ID inválido.")
                continue

            pedido = next((p for p in pedidos if p.id_pedido == id_pedido), None)
            if not pedido:
                print("Pedido no encontrado.")
                continue

            gestor.mostrar_anticipos(pedido)

        elif opcion == "3":
            print("\nPedidos actuales:")
            for p in pedidos:
                print(f"ID: {p.id_pedido}, Descripción: {p.descripcion}, Precio: {p.precio_unitario}, Total abonado: {p.total_anticipos()}")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
