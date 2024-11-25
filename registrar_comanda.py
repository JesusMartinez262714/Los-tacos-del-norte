"""
Desarrolladores: Jesús Manuel Martínez Cortez (262714), Contreras Ávila Ramsés Norberto (262720)
Objetivo:
El objetivo del programa es gestionar comandas en un restaurante. Esto incluye validar la disponibilidad de mesas, 
registrar los pedidos de clientes, asignar empleados a comandas, calcular costos y mostrar detalles de las comandas.
"""
import utilerias as u
import comandas_abiertas as ca
folio=1

def validar_mesa(mesas, num_mesas) -> bool:
    """
    Valida si una mesa está disponible para registrar una nueva comanda.

    Parámetros:
    - mesas (dict): Diccionario con el estado de las mesas.
    - num_mesas (int): Número de la mesa a validar.

    Retorna:
    - bool: True si la mesa está disponible, False en caso contrario.
    """
    if mesas[num_mesas] == "disponible":
        return True
    else:
        return False
    


def validar_empleado(empleados) -> int:
    """
    Valida si un empleado se encuentra registrado en el sistema.

    Parámetros:
    - empleados (dict): Diccionario con los IDs de los empleados.

    Retorna:
    - int: ID del empleado válido.
    """
    while True:
        empleado = u.validar_numerico("Ingrese el id del empleado: ")
        if empleado in empleados:
            return empleados[empleado]["nombre"]
        else:
            print("Empleado no válido, intente nuevamente")


def crear_comanda(comandas: dict,mesas: dict,empleados:dict,platillos:tuple):
    """
    Registra una nueva comanda asignándola a una mesa, cliente y empleado.

    Parámetros:
    - mesas (dict): Diccionario con el estado de las mesas.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.
    - empleados (dict): Diccionario con los IDs de empleados.
    - Comandas (dict): Diccionario que almacena las comandas registradas.
    - folio (int): Número único que identifica cada comanda.
    """
    global folio
    while True: 
        num_mesas = u.validar_numerico("Ingrese el número de la mesa: ")
        if num_mesas<0:
            break
        if not validar_mesa(mesas, num_mesas):
            print("La mesa seleccionada ya tiene una comanda abierta. No se puede registrar otra comanda hasta que la actual sea cerrada.")
        else:
             break
    if num_mesas<0:
            return

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    if nombre_cliente == "":
        nombre_cliente = "Cliente anónimo"
    
    empleado = validar_empleado(empleados)
    u.imprimirPlatillos()
    lista_platillos = []
    total=registrar_platillos(lista_platillos, platillos)
    mostrarComanda(lista_platillos, nombre_cliente, empleado, num_mesas,total)

    continuar = input("Desea registrar esta comanda? s/n ").lower()
    if continuar == "s":
        mesas[num_mesas] = "No disponible"
        print("Comanda registrada correctamente")
        folio+=1
        if folio in comandas:
            folio+=1
        
        comandas[folio] = {
            "mesa": num_mesas,
            "cliente":nombre_cliente,
            "empleado": empleado,
            "platillos": lista_platillos,
            "total":total,
            "propina":0,
            "estado": "No pagada"
        }
       
        ca.comandas_abiertas(comandas)
        
   

    

def registrar_platillos(lista_platillos, platillos) -> float:
    """
    Permite al cliente seleccionar platillos, indicando su cantidad, y calcula el total.

    Parámetros:
    - lista_platillos (list): Lista para almacenar los platillos seleccionados.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.

    Retorna:
    - float: Total acumulado de la selección de platillos.
    """
    total = 0.0
    while True:
        platillo = u.validar_numerico("Platillo: ")
        if platillo - 1 in range(len(platillos)):
            cantidad_platillo = u.validar_numerico("Ingrese la cantidad del platillo: ")
            if cantidad_platillo >= 1:
                costo, subtotal = Calculos_Comandas(platillo, cantidad_platillo,platillos)
                nombre_platillo=u.validar_mismo_platillo(platillo)
                lista_platillos.append([nombre_platillo, cantidad_platillo, costo])
                total += subtotal
                        
        else:
            print("Ese platillo no existe")
        continuar = input("¿Desea pedir otro platillo? (s/n): ").lower()
        if continuar == "n":
            break
    return total

def mostrarComanda(lista_platillos: list, nombre_cliente: str, empleado: str, num_mesas: int, total: float):
    """
    Muestra los detalles de una comanda registrada, incluyendo el cliente, mesa, empleado, platillos y total.

    Parámetros:
    - lista_platillos (list): Lista con los platillos seleccionados.
    - nombre_cliente (str): Nombre del cliente.
    - empleado (str): ID del empleado que atendió la comanda.
    - num_mesas (int): Número de la mesa asignada.
    - total (float): Total acumulado de la comanda.
    """
    #formateo
    print(f"\n{"Resumen de la comanda ":->25}{folio}:")
    print(f"Mesa: {num_mesas}")
    print(f"Cliente: {nombre_cliente}")
    print(f"Empleado: {empleado}")
    print("Platillos:")
    for platillo in lista_platillos:
        print(f"    - Platillo: {platillo[0]} ({platillo[1]}) - ${platillo[2]:.2f}")
    print(f"Total: ${total:.2f}")


def Calculos_Comandas(platillo, cantidad_platillo,platillos):
    """
    Calcula el costo y subtotal de un platillo seleccionado.

    Parámetros:
    - platillo (int): Número del platillo seleccionado.
    - cantidad_platillo (int): Cantidad de ese platillo.

    Retorna:
    - tuple: Costo por platillo y subtotal calculado.
    """
    costo = cantidad_platillo * platillos[0][2] if platillo == 1 else cantidad_platillo * platillos[1][2] if platillo == 2 else cantidad_platillo * platillos[2][2] if platillo == 3 else cantidad_platillo * platillos[3][2] if platillo == 4 else cantidad_platillo * platillos[4][2] if platillo == 5 else cantidad_platillo * platillos[5][2] if platillo == 6 else cantidad_platillo * platillos[6][2] if platillo == 7 else cantidad_platillo * platillos[7][2] if platillo == 8 else cantidad_platillo * platillos[8][2] if platillo == 9 else cantidad_platillo * platillos[9][2] if platillo == 10 else 0
    subtotal = 0
    subtotal += costo
    return costo, subtotal


if __name__ == "__main__":
    
   
    platillos = (
        ("tacos de asada", 20),
        ("tacos de pastor", 18),
        ("quesadillas", 25),
        ("Refresco", 15),
        ("Burrito de Asada", 40),
        ("Burrito de Pastor", 38),
        ("Torta de Asada", 45),
        ("Torta de Pastor", 43),
        ("Agua Fresca (1L)", 20), 
        ("Flautas (3 piezas)", 30)
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