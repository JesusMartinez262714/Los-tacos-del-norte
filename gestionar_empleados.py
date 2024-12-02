"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
Consultar las ventas del día, mostrando un resumen de las comandas pagadas, propinas y totales. Permitir al usuario filtrar las ventas por número de mesa o por empleado.

Descripción general:
Este código permite mostrar un resumen de las ventas realizadas durante el día, destacando las comandas que han sido pagadas, el total de las ventas y las propinas generadas. Además, ofrece al usuario la posibilidad de filtrar las ventas por mesa o empleado, mostrando los detalles de las comandas que coincidan con el filtro. Si no existen ventas para el filtro seleccionado, se muestra un mensaje indicativo. El sistema proporciona una visión clara y organizada de las transacciones del día.
"""

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
            if agregar_empleado(empleados):
                return
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
        idEmpleado = u.validar_numerico("Ingrese el id del empleado: ")
        if idEmpleado<=0:
            print("El numero ingresado es invalido, intentelo de nuevo.")
            continue
        if idEmpleado in empleados.keys():
            print("El ID del empleado ya esta registrado. Intente con otro ID")
            continue
        else:
            nombreEmpleado = input("Ingrese el nombre del empleado: ")
            telefonoEmpleado = input("Ingresa el numero de telefono del empleado: ")
            estado = "activo"
            #formateo
            print("Datos del empleado a agregar: ")
            print(f"ID: {idEmpleado}")
            print(f"Nombre: {nombreEmpleado}")
            print(f"Telefono: {telefonoEmpleado}")
            print(f"Estado: {estado}")
            confirmar = u.validar_s_n("Desea confirmar el registro del empleado? (s/n): ")
            if confirmar == "s":
                empleados[idEmpleado] = {
                    "nombre": nombreEmpleado,
                    "telefono": telefonoEmpleado,
                    "estado": estado
                }
                print("Empleado registrado exitosamente")
            elif confirmar == "n":
                print("proceso cancelado")
        realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n): ")
        if realizar == 's':
            return False
        elif realizar == 'n':
            return True


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
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            nuevoTelefono = input("Ingrese el nuevo numero de telefono: ")
            print("Informacion actualizada exitosamente")
            print("Datos del empleado a agregar: ")
            print(f"ID: {idEmpleado}")
            print(f"Nombre: {nuevoNombre}")
            print(f"Telefono: {nuevoTelefono}")
            print(f"Estado: {dictEmpleado['estado']}")
            confirmar=u.validar_s_n('Desea confirmar los cambios? s/n: ')
            if confirmar=='s':
                dictEmpleado['nombre'] = nuevoNombre
                dictEmpleado['telefono'] = nuevoTelefono
            else:
                print("Cambios Cancelados")
            realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n): ")
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
        nombreEmpleado, idEmpleado = u.validar_empleado(empleados)
        dictEmpleado = empleados.get(idEmpleado)
        if dictEmpleado:
            if dictEmpleado["estado"] == "activo":
                dictEmpleado["estado"] = "inactivo"
            elif dictEmpleado["estado"] == "inactivo":
                dictEmpleado["estado"] = "activo"
            #formateo
            print("El estado del empleado ha sido actualizado: ")
            print(f"ID: {idEmpleado}")
            print(f"Nombre: {nombreEmpleado}")
            print(f"Nuevo estado: {dictEmpleado["estado"]}")
            print(" ")
            realizar = u.validar_s_n("Desea realizar otra operacion de gestion de empleados? (s/n):")
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
    empleados_ordenados = dict(sorted(empleados.items(), key=lambda x: x[0]))

    if empleados_ordenados:  # Verifica si hay empleados registrados
        print(f"{' Listado de Empleados ':-^52}")
        print(f"{'ID':<8}{'Nombre':<20}{'Telefono':<15}Estado")
        print(f"{'':-^52}")
        for idEmpleado, info in empleados_ordenados.items():
            print(f"{idEmpleado:<8}{info['nombre']:<20}{info['telefono']:<15}{info['estado']}")
            print(f"{'':-^52}")

        print(f"Total de empleados: {len(empleados_ordenados)}")
    else:  # Si no hay empleados
        print("No hay empleados registrados en el sistema.")

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
