"""
Desarrolladores: Jesús Manuel Martínez Cortez (262714), Contreras Ávila Ramsés Norberto (262720)
Objetivo:
El objetivo del programa es gestionar comandas en un restaurante. Esto incluye validar la disponibilidad de mesas, 
registrar los pedidos de clientes, asignar empleados a comandas, calcular costos y mostrar detalles de las comandas.
"""


def validar_mesa(mesas, num_mesas) -> bool:
    """
    Valida si una mesa está disponible para registrar una nueva comanda.

    Parámetros:
    - mesas (dict): Diccionario con el estado de las mesas.
    - num_mesas (int): Número de la mesa a validar.

    Retorna:
    - bool: True si la mesa está disponible, False en caso contrario.
    """

    if mesas[num_mesas] == "Disponible":
        return True
    else:
        return False
    


def imprimirPlatillos():
    """
    Muestra el menú de platillos disponibles, incluyendo sus precios.
    """
    #formateo
    print("Menu platillos: ")
    print(f"{"":-^24}")
    print("1.-Tacos de asada - $20")
    print("2.-Tacos de pastor - $18")
    print("3.- Quesadillas -  $25")
    print("4.-Refresco - $15")


def validar_empleado(empleados) -> int:
    """
    Valida si un empleado se encuentra registrado en el sistema.

    Parámetros:
    - empleados (dict): Diccionario con los IDs de los empleados.

    Retorna:
    - int: ID del empleado válido.
    """
    while True:
        empleado = int(input("Ingrese el id del empleado: "))
        if empleado in empleados:
            return empleado
        else:
            print("Empleado no válido, intente nuevamente")


def crear_comanda(comandas,mesas,empleados,platillos,folio,lista_Temporal_Comandas_Abiertas):
    """
    Registra una nueva comanda asignándola a una mesa, cliente y empleado.

    Parámetros:
    - mesas (dict): Diccionario con el estado de las mesas.
    - platillos (tuple): Tupla con los nombres y precios de los platillos.
    - empleados (dict): Diccionario con los IDs de empleados.
    - Comandas (dict): Diccionario que almacena las comandas registradas.
    - folio (int): Número único que identifica cada comanda.
    """
    while True: 
        num_mesas = int(input("Ingrese el número de la mesa: "))
        if num_mesas<0:
            break
        if validar_mesa(mesas, num_mesas):
            print("La mesa seleccionada ya tiene una comanda abierta. No se puede registrar otra comanda hasta que la actual sea cerrada.")
        else:
             break
    if num_mesas<0:
            return

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    if nombre_cliente == "":
        nombre_cliente = "Cliente anónimo"
    
    empleado = validar_empleado(empleados)
    imprimirPlatillos()
    lista_platillos = []
    total=registrar_platillos(lista_platillos, platillos)
    mostrarComanda(lista_platillos, nombre_cliente, empleado, num_mesas,total,folio)

    continuar = input("Desea registrar esta comanda? s/n ").lower()
    if continuar == "s":
        mesas[num_mesas] = "No disponible"
        
        print("Comanda registrada correctamente")
        comandas[folio] = {
            "mesa": num_mesas,
            "empleado": empleado,
            "platillos": lista_platillos,
            "estado": "No disponible"
        }
        lista_Temporal_Comandas_Abiertas.append([num_mesas,nombre_cliente,empleado,total])
        comandas_abiertas(lista_Temporal_Comandas_Abiertas)
        folio+=1
    return folio
   

    

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
        platillo = int(input("Platillo: "))
        if platillo - 1 in range(len(platillos)):
            cantidad_platillo = int(input("Ingrese la cantidad del platillo: "))
            if cantidad_platillo >= 1:
                costo, subtotal = Calculos_Comandas(platillo, cantidad_platillo)
                lista_platillos.append([platillo, cantidad_platillo, costo])
                total += subtotal
        else:
            print("Ese platillo no existe")
        continuar = input("¿Desea pedir otro platillo? (s/n): ").lower()
        if continuar == "n":
            break
    return total

def mostrarComanda(lista_platillos: list, nombre_cliente: str, empleado: str, num_mesas: int, total: float, folio: int):
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
        if platillo[0]== 1:
            mensajePlatillo="Tacos de asada"
        if platillo[0]== 2:
            mensajePlatillo="Tacos de pastor"
        if platillo[0]== 3:
            mensajePlatillo="Quesadilla"
        if platillo[0]== 4:
            mensajePlatillo="Refresco"
        print(f"    - Platillo: {mensajePlatillo} ({platillo[1]}) - ${platillo[2]:.2f}")
    print(f"Total: ${total:.2f}")


def Calculos_Comandas(platillo, cantidad_platillo):
    """
    Calcula el costo y subtotal de un platillo seleccionado.

    Parámetros:
    - platillo (int): Número del platillo seleccionado.
    - cantidad_platillo (int): Cantidad de ese platillo.

    Retorna:
    - tuple: Costo por platillo y subtotal calculado.
    """
    costo = cantidad_platillo * 20 if platillo == 1 else cantidad_platillo * 18 if platillo == 2 else cantidad_platillo * 25 if platillo == 3 else cantidad_platillo * 15 if platillo == 4 else 0
    subtotal = 0
    subtotal += costo
    return costo, subtotal





def comandas_abiertas(lista_Temporal_Comandas_Abiertas):
    #formateo y hacer que se muestre al registrar una comanda
    contador=0
    print("Comandas Abiertas:")
    print(f"{"":-^65}")
    print(f"{"Mesa":<9}{"Cliente":<16}{"Empleado":<17}Total ($)")
    print(f"{"":-^65}")
    for pocision in lista_Temporal_Comandas_Abiertas:
        print(f"{pocision[0]:<9}{pocision[1]:<16}{pocision[2]:<17}{pocision[3]}")
        contador+=1
    print(f"{"":-^65}")
    print(f"Total de Comandas Abiertas: {contador}")
"""
if __name__ == "__main__":
    # Ejemplo de inicialización de estructuras
    mesas = {
    1: "disponible",
    2: "disponible",
    3: "disponible",
    4: "disponible",
    5: "disponible",
    6: "disponible",
    7: "disponible",
    8: "disponible"
}
    Comandas = {
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
    crear_comanda(mesas, empleados, Comandas, platillos)
"""
"""
if __name__ == "__main__":
    # Ejemplo de inicialización de estructuras
    listaPlatillos = []
    platillos = (
        ("tacos de asada", 20),
        ("tacos de pastor", 18),
        ("quesadillas", 25),
        ("Refresco", 15)
    )

    registrar_platillos(listaPlatillos, platillos)
"""