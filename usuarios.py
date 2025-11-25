class Usuario:
    def __init__(self, nombre, correo, contraseña, id_usuario):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.id = id_usuario
# --------------------------------------------------

    def editar_perfil(self, nuevo_nombre=None, nuevo_correo=None, nueva_contraseña=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_correo:
            self.correo = nuevo_correo
        if nueva_contraseña:
            self.contraseña = nueva_contraseña
# --------------------------------------------------


contador_admin = 1
contador_cliente = 1


administradores = []
clientes = []
# --------------------------------------------------


def registrar_admin():
    global contador_admin

    print("\n--- Registro de Administrador ---")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    id_generado = "ADM-" + str(contador_admin)
    contador_admin += 1

    admin = Usuario(nombre, correo, contraseña, id_generado)
    administradores.append(admin)

    print(f"\nAdministrador registrado con ID: {id_generado}")
    return admin
# --------------------------------------------------


def registrar_cliente():
    global contador_cliente

    print("\n--- Registro de Cliente ---")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    id_generado = "CLI-" + str(contador_cliente)
    contador_cliente += 1

    cliente = Usuario(nombre, correo, contraseña, id_generado)
    clientes.append(cliente)

    print(f"\nCliente registrado con ID: {id_generado}")
    return cliente
# --------------------------------------------------


def iniciar_sesion(lista_usuarios):
    print("\n--- Iniciar Sesión ---")

    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")

    for usuario in lista_usuarios:
        if usuario.nombre == nombre and usuario.contraseña == contraseña:
            print(f"\nBienvenido {usuario.nombre} (ID: {usuario.id})")
            return usuario

    print("\n⚠ Usuario o contraseña incorrectos.")
    return None
# --------------------------------------------------


def editar_perfil(usuario):
    print("\n--- Editar Perfil ---")

    print("Presiona ENTER si no quieres cambiar un dato.")

    nuevo_nombre = input("Nuevo nombre: ") or None
    nuevo_correo = input("Nuevo correo: ") or None
    nueva_contraseña = input("Nueva contraseña: ") or None

    usuario.editar_perfil(
        nuevo_nombre=nuevo_nombre,
        nuevo_correo=nuevo_correo,
        nueva_contraseña=nueva_contraseña
    )

    print("\nPerfil actualizado correctamente.")
    return usuario
# --------------------------------------------------


def ver_perfil(usuario):
    print("\n===== INFORMACIÓN DEL PERFIL =====")
    print(f"ID: {usuario.id}")
    print(f"Nombre: {usuario.nombre}")
    print(f"Correo: {usuario.correo}")
    
# --------------------------------------------------


def ver_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\n===== LISTA DE CLIENTES =====")
    for cliente in clientes:
        print(f"ID: {cliente.id} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")
    print("----------------------------")
