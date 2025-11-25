from datetime import datetime
from prueba import GestionConfeccionistas
gestion_confeccionistas = GestionConfeccionistas()
#----------------------------------------------------------------

class Pedido:
    contador_pedidos = 101

    def __init__(self, cliente, talla, tela, imagen, color_tela, cantidad, detalles_extras, estado = "pendiente", precio_unitario = None):
        self.id_pedido = Pedido.contador_pedidos
        Pedido.contador_pedidos += 1

        self.cliente = cliente  
        self.talla = talla
        self.tela = tela
        self.imagen = imagen
        self.color_tela = color_tela
        self.cantidad = cantidad
        self.detalles_extras = detalles_extras
        self.estado = estado
        self.precio_unitario = precio_unitario
        self.monto_pagar = self.calcular_monto()
        self.fecha_creacion = datetime.now()
        self.confeccionista_asignado = None
        self.anticipos = []

    def calcular_monto(self):
        if self.precio_unitario is None:
            return 0
        return self.cantidad * self.precio_unitario
    
    def total_anticipos(self):
        return sum(a["monto"] for a in self.anticipos)
    
    def restante_por_pagar(self):
        return self.monto_pagar - self.total_anticipos()
     

    def __str__(self):

        return (f"\nID Pedido: {self.id_pedido}\n"
                f"fecha de registro: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Cliente: {self.cliente.nombre} (ID: {self.cliente.id})\n"
                f"Talla: {self.talla}\n"
                f"Tela: {self.tela}\n"
                f"Imagen referencia: {self.imagen}\n"
                f"Color de tela: {self.color_tela}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Detalles extras: {self.detalles_extras}\n"
                f"Estado: {self.estado}\n"
                f"Precio unitario: {self.precio_unitario}\n"
                f"Monto a pagar: {self.monto_pagar}\n"
                f"Total anticipado: {self.total_anticipos()}\n"
                f"Confeccionista asignado: {self.confeccionista_asignado if self.confeccionista_asignado else 'No asignado'}\n")

#----------------------------------------------------------------




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

#----------------------------------------------------------------



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
            print("9. Salir de edición")

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
                print("Saliendo del editor...")
                break
            else:
                print("Opción no válida.")

        print("\n¡Pedido actualizado correctamente!\n")

#----------------------------------------------------------------



# gestion de pedidos
class GestorPedidos:

    def __init__(self):
        self.pedidos = []
        self.editor = GestorEdicion(EditorPedido())
# --------------------------------------------------

    def agregar_pedido(self, cliente):
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
        

        nuevo = Pedido(cliente=cliente, talla = talla, tela = tela, imagen = imagen, color_tela = color_tela, cantidad = cantidad, detalles_extras = detalles_extras)
        self.pedidos.append(nuevo)
        print("\nPedido registrado.\n")
# --------------------------------------------------
    def mostrar_pedidos(self):
        print("\n--- LISTA DE PEDIDOS ---\n")
        if not self.pedidos:
            print("No hay pedidos registrados.\n")
            return
        for pedido in self.pedidos:
            print(pedido)
            print("---------------------------")

    def mostrar_pedidos_cliente(self, cliente):
        print("\n--- LISTA DE TUS PEDIDOS ---\n")

        pedidos_cliente = [p for p in self.pedidos if p.cliente == cliente]

        if not pedidos_cliente:
            print("No tienes pedidos registrados.")
            return

        for pedido in pedidos_cliente:
            print(pedido)
            print("---------------------------")
# --------------------------------------------------

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
# --------------------------------------------------

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
# --------------------------------------------------

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
# --------------------------------------------------

    def pagar_pedido(self):
        if not self.pedidos:
            print("No hay pedidos registrados.")
            return
        
        print("\nPedidos disponibles para pagar:")
        for p in self.pedidos:
            print(f"ID: {p.id_pedido} | Monto total: {p.self.monto_pagar} | Restante por pagar: {self.restante_por_pagar}")
        
        try:
            id_pedido = int(input("Ingrese el ID del pedido que desea pagar: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in self.pedidos if p.id_pedido == id_pedido), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        # Elegir método de pago
        print("\nSeleccione método de pago:")
        print("1. Nequi")
        print("2. Bancolombia")
        opcion = input("Opción: ")

        if opcion == "1":
            metodo = "Nequi"
        elif opcion == "2":
            metodo = "Bancolombia"
        else:
            print("Método de pago inválido.")
            return

        try:
            monto = float(input("Ingrese el monto que va a pagar como anticipo: "))
        except ValueError:
            print("Monto inválido.")
            return

        # Registrar anticipo con fecha y hora
        pedido.anticipos.append({
            "monto": monto,
            "fecha": datetime.now(),
            "metodo": metodo
        })

        print(f"Anticipo de {monto} registrado para el pedido {pedido.id_pedido} mediante {metodo}.")

        # Cambiar estado si ya se pagó todo
        total_pagado = sum([a['monto'] for a in pedido.anticipos])
        if total_pagado >= pedido.monto_pagar:
            pedido.estado = "Pagado"
            print(f"Pedido {pedido.id_pedido} completamente pagado.")
# --------------------------------------------------


    def mostrar_anticipos_pedido(self):
        if not self.pedidos:
            print("No hay pedidos registrados.")
            return
        
        print("\nPedidos disponibles:")
        for p in self.pedidos:
            print(f"ID: {p.id_pedido} | Monto total: {p.monto_pagar}")

        try:
            id_pedido = int(input("Ingrese el ID del pedido para ver sus anticipos: "))
        except ValueError:
            print("ID inválido.")
            return

        pedido = next((p for p in self.pedidos if p.id_pedido == id_pedido), None)
        if not pedido:
            print("Pedido no encontrado.")
            return

        if not pedido.anticipos:
            print("No hay anticipos registrados para este pedido.")
            return

        print(f"\nAnticipos del pedido {pedido.id_pedido}:")
        for a in pedido.anticipos:
            fecha_str = a['fecha'].strftime("%d/%m/%Y %H:%M:%S")
            print(f"Fecha: {fecha_str} | Monto: {a['monto']} | Método: {a['metodo']}")

        
        print(f"\nTotal pagado hasta ahora: {self.total_anticipos}")
        print(f"restante: {self.restante_por_pagar}")
# --------------------------------------------------



    
    

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
        print("7. pagar pedido")
        print("8. mostrar anticipos de un pedido")
        print("9. Salir")
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
            gestor.pagar_pedido()
        elif opcion == "8":
            gestor.mostrar_anticipos_pedido()

        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")



if __name__ == "__main__":
    menu()
