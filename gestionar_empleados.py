import utilerias as u

def menu_empleados(empleados: dict):
    """
    Menú principal para gestionar empleados.

    Datos de entrada:
        empleados (dict): Diccionario que contiene la información de los empleados registrados.

    Proceso:
        - Muestra un menú con opciones para agregar, actualizar, cambiar estado o consultar empleados.
        - Ejecuta las acciones correspondientes según la opción seleccionada.
        - Permite regresar al menú principal al seleccionar la opción 5 o completar las tareas.

    Salida:
        None

    Argumentos:
        empleados: Diccionario con la información de los empleados, donde las claves son los IDs y los valores son sub-diccionarios con los datos de cada empleado.
    """
    while True:
        print("-----Gestion de empleados")
        print("1.-Agregar un nuevo empleado")
        print("2.-Actualizar informacion de un empleado")
        print("3.-Cambiar el estado de un empleado (activo/inactivo)")
        print("4.-Consultar listado de empleados.")
        print("5.-Regresar al menu principal")
        opcion = u.validar_numerico("Ingrese una opcion: ")
        if opcion == 5:
            return
        elif opcion == 1:
            agregar_empleado(empleados)
        elif opcion == 2:
            if actualizar_informacion(empleados):
                return
        elif opcion == 3:
            if cambiar_estado_empleado(empleados):
                return
        elif opcion == 4:
            if listado_empleados(empleados):
                return
        else:
            print("no valido porfavor ingrese otra vez")


def agregar_empleado(empleados: dict):
    """
    Agrega un nuevo empleado al diccionario de empleados.

    Datos de entrada:
        empleados (dict): Diccionario que contiene la información de los empleados registrados.

    Proceso:
        - Solicita datos del nuevo empleado (ID, nombre, teléfono).
        - Verifica si el ID ya está registrado.
        - Si no está registrado, solicita confirmación para agregar el empleado al diccionario.

    Salida:
        None

    Argumentos:
        empleados: Diccionario donde se almacena la información de los empleados.
    """
    while True:
        idEmpleado = u.validar_numerico("Ingrese el id del empleado")
        if idEmpleado in empleados.keys():
            print("El ID del empleado ya esta registrado. Intente con otro ID")
            continue
        else:
            nombreEmpleado = input("Ingrese el nombre del empleado: ")
            telefonoEmpleado = input("Ingresa el numero de telefono del empleado: ")
            estado = "activo"
            print("datos del empleado a agregar")
            nuevoEmpleado = {
                "id": idEmpleado,
                "nombre": nombreEmpleado,
                "telefono": telefonoEmpleado,
                "estado": estado
            }
            print(nuevoEmpleado)
            confirmar = u.validar_s_n("Desea confirmar el registro del empleado? (s/n)")
            if confirmar == "s":
                empleados[idEmpleado] = {
                    "nombre": nombreEmpleado,
                    "telefono": telefonoEmpleado,
                    "estado": estado
                }
                print("Empleado registrado exitosamente")
                return
            elif confirmar == "n":
                print("proceso cancelado")
                return


def actualizar_informacion(empleados: dict):
    """
    Actualiza la información de un empleado existente.

    Datos de entrada:
        empleados (dict): Diccionario que contiene la información de los empleados registrados.

    Proceso:
        - Solicita el ID del empleado a modificar.
        - Si el empleado existe, permite actualizar el nombre y el teléfono.
        - Pregunta si desea realizar otra operación.

    Salida:
        bool: True si se desea regresar al menú principal, False en caso contrario.

    Argumentos:
        empleados: Diccionario donde se almacena la información de los empleados.
    """
    while True:
        _, idEmpleado = u.validar_empleado(empleados)
        dictEmpleado = empleados.get(idEmpleado)
        if dictEmpleado:
            nuevoNombre = input("Ingrese el nuevo nombre")
            dictEmpleado['nombre'] = nuevoNombre
            nuevoTelefono = input("Ingrese el nuevo numero de telefono")
            dictEmpleado['telefono'] = nuevoTelefono
            print("Informacion actualizada exitosamente")
            realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n)")
            if realizar == 's':
                return False
            elif realizar == 'n':
                return True
        else:
            print("El id ingresado no corresponde a ningun empleado registrado")


def cambiar_estado_empleado(empleados: dict):
    """
    Cambia el estado de un empleado entre activo e inactivo.

    Datos de entrada:
        empleados (dict): Diccionario que contiene la información de los empleados registrados.

    Proceso:
        - Solicita el ID del empleado cuyo estado se desea cambiar.
        - Si el empleado existe, alterna su estado entre activo e inactivo.
        - Pregunta si desea realizar otra operación.

    Salida:
        bool: True si se desea regresar al menú principal, False en caso contrario.

    Argumentos:
        empleados: Diccionario donde se almacena la información de los empleados.
    """
    while True:
        _, idEmpleado = u.validar_empleado(empleados)
        dictEmpleado = empleados.get(idEmpleado)
        if dictEmpleado:
            if dictEmpleado["estado"] == "activo":
                dictEmpleado["estado"] = "inactivo"
            elif dictEmpleado["estado"] == "inactivo":
                dictEmpleado["estado"] = "activo"
            print("el estado del empleado ha sido actualizado")
            print(f"{dictEmpleado}")
            realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n)")
            if realizar == 's':
                return False
            elif realizar == 'n':
                return True
        else:
            print("El id ingresado no corresponde a ningun empleado registrado")


def listado_empleados(empleados: dict):
    """
    Muestra el listado de empleados registrados.

    Datos de entrada:
        empleados (dict): Diccionario que contiene la información de los empleados registrados.

    Proceso:
        - Recorre y muestra cada empleado con su información.
        - Pregunta si desea realizar otra operación.

    Salida:
        bool: True si se desea regresar al menú principal, False en caso contrario.

    Argumentos:
        empleados: Diccionario donde se almacena la información de los empleados.
    """
    print("Listado de empleados:")
    for idEmpleado, info in empleados.items():
        print(f"ID: {idEmpleado}, Nombre: {info['nombre']}, Teléfono: {info['telefono']}, Estado: {info['estado']}")
    realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n)")
    if realizar == 's':
        return False
    elif realizar == 'n':
        return True


if __name__ == "__main__":
    empleados = {
        101: {
            "nombre": "María López",
            "telefono": "6441234567",
            "estado": "activo"
        },
        102: {
            "nombre": "Pedro Martínez",
            "telefono": "6449876543",
            "estado": "inactivo"
        }
    }
    menu_empleados(empleados)
