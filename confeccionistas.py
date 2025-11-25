


class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id = id_empleado

class GestionConfeccionistas:
    def __init__(self):
        self.empleados = []
        self.contador_id = 1 

   #---------------------------------------------------------


    # Registrar un nuevo empleado
    def registrar_empleado(self):
        nombre = input("Ingrese el nombre del nuevo confeccionista: ")
        empleado = Empleado(nombre, self.contador_id)
        self.empleados.append(empleado)
        self.contador_id += 1
        print(f"Empleado registrado correctamente. ID asignado: {empleado.id}")
        return empleado

   #---------------------------------------------------------


    # Ver lista de empleado
    def ver_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return []
        for e in self.empleados:
            print(f"ID: {e.id} | Nombre: {e.nombre}")
        return self.empleados

   #---------------------------------------------------------


    # Eliminar empleado por ID
    def eliminar_empleado(self):
        try:
            id_empleado = int(input("Ingrese el ID del confeccionista a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número.")
            return False

        for e in self.empleados:
            if e.id == id_empleado:
                self.empleados.remove(e)
                print(f"Empleado {id_empleado} eliminado correctamente.")
                return True

        print("No se encontró un empleado con ese ID.")
        return False

#---------------------------------------------------------


    # Editar información del empleado
    def editar_empleado(self):
        try:
            id_empleado = int(input("Ingrese el ID del empleado a editar: "))
        except ValueError:
            print("ID inválido. Debe ser un número.")
            return False

        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        for e in self.empleados:
            if e.id == id_empleado:
                e.nombre = nuevo_nombre
                print(f"Empleado {id_empleado} actualizado correctamente.")
                return True

        print("No se encontró un empleado con ese ID.")
        return False

    #--------------------------------------------------------


    # Buscar empleado por ID
    def buscar_empleado(self):
        try:
            id_empleado = int(input("Ingrese el ID del empleado a buscar: "))
        except ValueError:
            print("ID inválido. Debe ser un número.")
            return None

        for e in self.empleados:
            if e.id == id_empleado:
                print(f"Empleado encontrado: ID {e.id} | Nombre: {e.nombre}")
                return e

        print("No se encontró un empleado con ese ID.")
        return None
        
               
