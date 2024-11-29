"""
Desarrolladores: Jesús Manuel Martínez Cortez (262714), Contreras Ávila Ramsés Norberto (262720)
Objetivo:
El objetivo del programa es gestionar comandas en un restaurante. Esto incluye validar la disponibilidad de mesas, 
registrar los pedidos de clientes, asignar empleados a comandas, calcular costos y mostrar detalles de las comandas.
"""
import utilerias as u
import comandas_abiertas as ca
import imprimir_platillos as ip

folio = 1  # Número de folio global para identificar las comandas


def validar_mesa(mesas: dict, num_mesas: int) -> bool:
    """
    Valida si una mesa está disponible para registrar una nueva comanda.

    Parámetros:
    - mesas (dict): Diccionario con el estado de las mesas.
    - num_mesas (int): Número de la mesa a validar.

    Proceso:
    - Verifica si la mesa en el diccionario `mesas` está marcada como "Disponible".

    Retorna:
    - bool: True si la mesa está disponible, False en caso contrario.
    """
    return mesas[num_mesas] == "disponible"


def crear_comanda(comandas: dict, mesas: dict, empleados: dict, platillos: tuple):
    """
    Registra una nueva comanda asignándola a una mesa, cliente y empleado.

    Parámetros:
    - comandas (dict): Diccionario que almacena las comandas registradas.
    - mesas (dict): Diccionario con el estado de las mesas.
    - empleados (dict): Diccionario con los IDs de empleados.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.

    Proceso:
    - Solicita datos al usuario: número de mesa, cliente y empleado.
    - Valida la disponibilidad de la mesa y solicita platillos.
    - Calcula el total y almacena los datos en el diccionario de comandas.

    Salida:
    - Actualiza los diccionarios `comandas` y `mesas` con los datos ingresados.
    """
    global folio
    while True:
        num_mesas: int = u.validar_numerico("Ingrese el número de la mesa: ")
        if num_mesas < 0:
            return
        if not validar_mesa(mesas, num_mesas):
            print("La mesa seleccionada ya tiene una comanda abierta.")
        else:
            break

    nombre_cliente: str = input("Ingrese el nombre del cliente: ")
    nombre_cliente = "Cliente anónimo" if nombre_cliente == "" else nombre_cliente

    empleado, id_empleado = u.validar_empleado(empleados)
    ip.imprimirPlatillos()
    lista_platillos: list = []
    total: float = registrar_platillos(lista_platillos, platillos)
    mostrarComanda(lista_platillos, nombre_cliente, empleado, num_mesas, total)

    continuar: str = input("¿Desea registrar esta comanda? (s/n): ").lower()
    if continuar == "s":
        mesas[num_mesas] = "no disponible"
        print("Comanda registrada correctamente.")

        if folio in comandas:
            folio += 1

        comandas[folio] = {
            "mesa": num_mesas,
            "cliente": nombre_cliente,
            "empleado": empleado,
            "platillos": lista_platillos,
            "total": total,
            "propina": 0,
            "estado": "no pagada"
        }
        ca.comandas_abiertas(comandas)


def registrar_platillos(lista_platillos: list, platillos: tuple) -> float:
    """
    Permite al cliente seleccionar platillos, indicando su cantidad, y calcula el total.

    Parámetros:
    - lista_platillos (list): Lista para almacenar los platillos seleccionados.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.

    Proceso:
    - Solicita al usuario un número de platillo y la cantidad deseada.
    - Calcula el subtotal basado en la cantidad y el precio del platillo.

    Retorna:
    - float: Total acumulado de la selección de platillos.
    """
    total: float = 0.0
    while True:
        platillo: int = u.validar_numerico("Platillo: ")
        if platillo - 1 in range(len(platillos)):
            nombre_platillo: str = u.validar_mismo_platillo(platillo)
            cantidad_platillo: int = u.validar_numerico("Ingrese la cantidad del platillo: ")
            if cantidad_platillo >= 1:
                for i in lista_platillos:
                    if nombre_platillo == i[0]:
                        cantidad_platillo += i[1]
                        lista_platillos.remove(i)
                costo, subtotal = Calculos_Comandas(platillo, cantidad_platillo, platillos)
                lista_platillos.append((nombre_platillo, cantidad_platillo, costo))
                total += subtotal
        else:
            print("Ese platillo no existe")
        continuar: str = input("¿Desea pedir otro platillo? (s/n): ").lower()
        if continuar == "n":
            return total


def mostrarComanda(lista_platillos: list, nombre_cliente: str, empleado: str, num_mesas: int, total: float):
    """
    Muestra los detalles de una comanda registrada.

    Parámetros:
    - lista_platillos (list): Lista con los platillos seleccionados.
    - nombre_cliente (str): Nombre del cliente.
    - empleado (str): ID del empleado que atendió la comanda.
    - num_mesas (int): Número de la mesa asignada.
    - total (float): Total acumulado de la comanda.

    Proceso:
    - Imprime los datos de la comanda en un formato legible.
    """
    print(f"\n{'Resumen de la comanda':->25} {folio}:")
    print(f"Mesa: {num_mesas}")
    print(f"Cliente: {nombre_cliente}")
    print(f"Empleado: {empleado}")
    print("Platillos:")
    for platillo in lista_platillos:
        print(f"    - {platillo[0]} ({platillo[1]}) - ${platillo[2]:.2f}")
    print(f"Total: ${total:.2f}")


def Calculos_Comandas(platillo: int, cantidad_platillo: int, platillos: tuple) -> tuple:
    """
    Calcula el costo y subtotal de un platillo seleccionado.

    Parámetros:
    - platillo (int): Número del platillo seleccionado.
    - cantidad_platillo (int): Cantidad de ese platillo.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.

    Proceso:
    - Calcula el costo unitario multiplicado por la cantidad.
    - Retorna una tupla con el costo y subtotal.

    Retorna:
    - tuple: Costo por platillo y subtotal calculado.
    """
    costo: float = cantidad_platillo * platillos[platillo - 1][2]
    subtotal: float = costo
    return costo, subtotal



if __name__ == "__main__":
    
   
    platillos = (
        (1, "Tacos de Asada", 20.00),
        (2, "Tacos de Pastor", 18.00),
        (3, "Quesadilla", 25.00),
        (4, "Refresco", 15.00),
        (5, "Burrito de Asada", 40.00),
        (6, "Burrito de Pastor", 38.00),
        (7, "Torta de Asada", 45.00),
        (8, "Torta de Pastor", 43.00),
        (9, "Agua Fresca (1L)", 20.00),
        (10, "Flautas (3 piezas)", 30.00)
    )

    
    comandas = {
    1:{
        "mesa": 3,
        "cliente": "Juan Pérez",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00)
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "No pagada" #Pueden ser pagadas o no pagadas
    },
    2:{
        "mesa": 3,
        "cliente": "Juan Pérez",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00)
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "pagada" #Pueden ser pagadas o no pagadas
    },
    3:{
        "mesa": 3,
        "cliente": "Juan Pérez",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00)
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "pagada" #Pueden ser pagadas o no pagadas
    }
    }
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
    mesas = {
        1: "disponible",
        2: "disponible",
        3: "no disponible",
        4: "disponible",
        5: "disponible",
        6: "disponible",
        7: "disponible",
        8: "disponible",
        9: "disponible",
        10: "disponible",
        11: "disponible",
        12: "disponible",
        13: "disponible",
        14: "disponible",
        15: "disponible"

}
    crear_comanda(comandas,mesas,empleados,platillos)