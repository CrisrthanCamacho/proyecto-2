from datetime import datetime
from prueba import GestionConfeccionistas
gestion_confeccionistas = GestionConfeccionistas()
#  pedido

class Pedido:
    contador_pedidos = 101

    def __init__(self, talla, tela, imagen, color_tela, cantidad, detalles_extras, estado, precio_unitario, metodo_pago):
        self.id_pedido = Pedido.contador_pedidos
        Pedido.contador_pedidos += 1

        self.talla = talla
        self.tela = tela
        self.imagen = imagen
        self.color_tela = color_tela
        self.cantidad = cantidad
        self.detalles_extras = detalles_extras
        self.estado = estado
        self.precio_unitario = precio_unitario
        self.metodo_pago = metodo_pago
        self.monto_pagar = self.calcular_monto()
        self.fecha_creacion = datetime.now()
        self.confeccionista_asignado = None

    def calcular_monto(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return (f"\nID Pedido: {self.id_pedido}\n"
                f"fecha de registro: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Talla: {self.talla}\n"
                f"Tela: {self.tela}\n"
                f"Imagen referencia: {self.imagen}\n"
                f"Color de tela: {self.color_tela}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Detalles extras: {self.detalles_extras}\n"
                f"Estado: {self.estado}\n"
                f"Precio unitario: {self.precio_unitario}\n"
                f"Método de pago: {self.metodo_pago}\n"
                f"Monto a pagar: {self.monto_pagar}\n"
                f"Confeccionista asignado: {self.confeccionista_asignado if self.confeccionista_asignado else 'No asignado'}\n")



# editor de pedidos

class EditorPedido:

    def editar_talla(self, pedido, nueva_talla):
        pedido.talla = nueva_talla

    def editar_tela(self, pedido, nueva_tela):
        pedido.tela = nueva_tela

    def editar_imagen(self, pedido, nueva_imagen):
        pedido.imagen = nueva_imagen

    def editar_color(self, pedido, nuevo_color):
        pedido.color_tela = nuevo_color

    def editar_cantidad(self, pedido, nueva_cantidad):
        pedido.cantidad = nueva_cantidad
        pedido.monto_pagar = pedido.calcular_monto()

    def editar_detalles(self, pedido, nuevos_detalles):
        pedido.detalles_extras = nuevos_detalles

    def editar_estado(self, pedido, nuevo_estado):
        pedido.estado = nuevo_estado

    def editar_precio(self, pedido, nuevo_precio):
        pedido.precio_unitario = nuevo_precio
        pedido.monto_pagar = pedido.calcular_monto()

    def editar_metodo_pago(self, pedido, nuevo_metodo):
        pedido.metodo_pago = nuevo_metodo



# menu de edicion de pedido

class GestorEdicion:

    def __init__(self, editor):
        self.editor = editor

    def mostrar_menu_edicion(self, pedidos):
        print("\n--- EDITAR PEDIDO ---")
        if not pedidos:
            print("No hay pedidos para editar.")
            return

        try:
            id_editar = int(input("Ingrese el ID del pedido a editar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in pedidos if p.id_pedido == id_editar), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        while True:
            print("\n¿Qué desea editar?")
            print("1. Talla")
            print("2. Tela")
            print("3. Imagen")
            print("4. Color de la tela")
            print("5. Cantidad")
            print("6. Detalles extras")
            print("7. Estado")
            print("8. Precio unitario")
            print("9. Método de pago")
            print("10. Salir de edición")

            opcion = input("Seleccione: ")

            if opcion == "1":
                nuevo = input("Nueva talla: ")
                self.editor.editar_talla(pedido, nuevo)
            elif opcion == "2":
                nuevo = input("Nueva tela: ")
                self.editor.editar_tela(pedido, nuevo)
            elif opcion == "3":
                nuevo = input("Nueva imagen: ")
                self.editor.editar_imagen(pedido, nuevo)
            elif opcion == "4":
                nuevo = input("Nuevo color de tela: ")
                self.editor.editar_color(pedido, nuevo)
            elif opcion == "5":
                try:
                    nuevo = int(input("Nueva cantidad: "))
                    self.editor.editar_cantidad(pedido, nuevo)
                except ValueError:
                    print("Cantidad inválida.")
            elif opcion == "6":
                nuevo = input("Nuevos detalles: ")
                self.editor.editar_detalles(pedido, nuevo)
            elif opcion == "7":
                nuevo = input("Nuevo estado: ")
                self.editor.editar_estado(pedido, nuevo)
            elif opcion == "8":
                try:
                    nuevo = float(input("Nuevo precio unitario: "))
                    self.editor.editar_precio(pedido, nuevo)
                except ValueError:
                    print("Precio inválido.")
            elif opcion == "9":
                nuevo = input("Nuevo método de pago: ")
                self.editor.editar_metodo_pago(pedido, nuevo)
            elif opcion == "10":
                print("Saliendo del editor...")
                break
            else:
                print("Opción no válida.")

        print("\n¡Pedido actualizado correctamente!\n")



# gestion de pedidos

class GestorPedidos:

    def __init__(self):
        self.pedidos = []
        self.editor = GestorEdicion(EditorPedido())

    def agregar_pedido(self):
        print("\n--- REGISTRAR NUEVO PEDIDO ---")
        talla = input("Talla: ")
        tela = input("Tela: ")
        imagen = input("Imagen o referencia: ")
        color_tela = input("Color de la tela: ")

        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida. Se asigna 1 por defecto.")
            cantidad = 1

        detalles_extras = input("Detalles extras: ")
        estado = input("Estado del pedido (Pendiente/Pagado/Entregado): ")

        try:
            precio_unitario = float(input("Precio unitario: "))
        except ValueError:
            print("Precio inválido. Se asigna 0 por defecto.")
            precio_unitario = 0.0

        metodo_pago = input("Método de pago: ")

        nuevo = Pedido(talla, tela, imagen, color_tela, cantidad, detalles_extras, estado, precio_unitario, metodo_pago)
        self.pedidos.append(nuevo)
        print("\nPedido registrado.\n")

    def mostrar_pedidos(self):
        print("\n--- LISTA DE PEDIDOS ---\n")
        if not self.pedidos:
            print("No hay pedidos registrados.\n")
            return
        for pedido in self.pedidos:
            print(pedido)
            print("---------------------------")


    def eliminar_pedido(self):
        if not self.pedidos:
            print("No hay pedidos para eliminar.")
            return

        try:
            id_eliminar = int(input("Ingrese el ID del pedido a eliminar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in self.pedidos if p.id_pedido == id_eliminar), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        self.pedidos.remove(pedido)
        print(f"Pedido {id_eliminar} eliminado correctamente.")


    def cancelar_pedido(self):
        if not self.pedidos:
            print("No hay pedidos para cancelar.")
            return

        try:
            id_cancelar = int(input("Ingrese el ID del pedido a cancelar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in self.pedidos if p.id_pedido == id_cancelar), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        if pedido.estado.lower() == "cancelado":
            print("El pedido ya está cancelado.")
            return

        pedido.estado = "Cancelado"
        print(f"Pedido {pedido.id_pedido} cancelado correctamente.")


    def asignar_pedido(self, gestion_empleados):
    # Verificar si hay pedidos disponibles
        pedidos_sin_asignar = [p for p in self.pedidos if p.confeccionista_asignado is None]
        if not pedidos_sin_asignar:
            print("No hay pedidos disponibles para asignar.")
            return

        if not gestion_empleados.empleados:
            print("No hay confeccionistas registrados.")
            return

    # Mostrar solo pedidos sin confeccionista asignado
        print("\nPedidos disponibles para asignar:")
        for p in pedidos_sin_asignar:
            print(f"ID Pedido: {p.id_pedido} | Estado: {p.estado} | Talla: {p.talla}")
        try:
            id_pedido = int(input("Ingrese el ID del pedido a asignar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in pedidos_sin_asignar if p.id_pedido == id_pedido), None)
        if not pedido:
            print("Pedido no encontrado o ya tiene un confeccionista asignado.")
            return

    # Mostrar solo confeccionistas que no tienen pedidos asignados
        empleados_disponibles = [e for e in gestion_empleados.empleados 
                                 if not any(p.confeccionista_asignado == e.nombre for p in self.pedidos)]
        if not empleados_disponibles:
            print("No hay confeccionistas disponibles sin pedidos asignados.")
            return

        print("\nConfeccionistas disponibles:")
        for e in empleados_disponibles:
            print(f"ID: {e.id} | Nombre: {e.nombre}")

        try:
            id_empleado = int(input("Ingrese el ID del confeccionista para asignar el pedido: "))
        except ValueError:
            print("ID inválido.")
            return

        empleado = next((e for e in empleados_disponibles if e.id == id_empleado), None)
        if not empleado:
            print("Confeccionista no encontrado o ya tiene un pedido asignado.")
            return

        pedido.confeccionista_asignado = empleado.nombre
        print(f"Pedido {pedido.id_pedido} asignado a {empleado.nombre} correctamente.")


    
    

# menú pricipal

def menu():
    gestor = GestorPedidos()

    while True:
        print("\n====== SISTEMA DE PEDIDOS DE COSTURERÍA ======")
        print("1. Registrar pedido")
        print("2. Mostrar pedidos")
        print("3. Editar pedido")
        print("4. eliminar pedido")
        print("5. cancelar pedido")
        print("6. asignar pedido")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            gestor.agregar_pedido()
        elif opcion == "2":
            gestor.mostrar_pedidos()
        elif opcion == "3":
            gestor.editor.mostrar_menu_edicion(gestor.pedidos)
        elif opcion == "4":
            gestor.eliminar_pedido()
        elif opcion == "5":
            gestor.cancelar_pedido()
        elif opcion == "6":
            gestor.asignar_pedido(gestion_confeccionistas)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")



if __name__ == "__main__":
    menu()
