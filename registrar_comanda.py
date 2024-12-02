"""
Desarrolladores: Jesús Manuel Martínez Cortez (262714), Contreras Ávila Ramsés Norberto (262720)
Objetivo:
El objetivo del programa es gestionar comandas en un restaurante. Esto incluye validar la disponibilidad de mesas, 
registrar los pedidos de clientes, asignar empleados a comandas, calcular costos y mostrar detalles de las comandas.
"""
import utilerias as u
import comandas_abiertas as ca
import imprimir_platillos as ip
import cerrar_comanda as cc
folio=0

def validar_mesa(mesas, num_mesas) -> bool:
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Valida si una mesa está disponible para registrar una nueva comanda.

    La función verifica el estado de la mesa en el diccionario 'mesas' y retorna 'True'
    si la mesa está disponible, o 'False' si está ocupada.

    Parámetros:
    - mesas (dict): Diccionario con el estado actual de las mesas, donde las claves
      son los números de mesa y los valores son cadenas que indican su estado 
      ("disponible" o "no disponible").
    - num_mesas (int): Número de la mesa que se desea validar.

    Retorna:
    - bool: 'True' si la mesa está disponible, 'False' si está ocupada o no disponible.
    """
    if mesas[num_mesas] == "disponible":
        return True
    else:
        return False
    





def crear_comanda(comandas: dict,mesas: dict,empleados:dict,platillos:tuple):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Registra una nueva comanda asignándola a una mesa, cliente y empleado.

    La función valida que la mesa seleccionada esté disponible, registra los platillos 
    solicitados por el cliente, asigna el pedido a un empleado activo y almacena toda la
    información en el diccionario de comandas.

    Parámetros:
    - comandas (dict): Diccionario que almacena las comandas registradas. Cada comanda incluye
      información como el número de mesa, cliente, empleado, lista de platillos, total, propina,
      y estado ("no pagada" o "pagada").
    - mesas (dict): Diccionario con el estado actual de las mesas, donde las claves son los números
      de mesa y los valores indican si están "disponible" o "no disponible".
    - empleados (dict): Diccionario que almacena la información de los empleados, incluyendo su ID
      y estado (activo/inactivo).
    - platillos (tuple): Tupla con los nombres y precios de los platillos disponibles en el menú.

    Variables globales:
    - folio (int): Número único que identifica cada comanda.

    Retorna:
    - nada
    """
    while True:
        global folio
        while True: 
            num_mesas = u.validar_numerico("Ingrese el número de la mesa: ")
            if num_mesas<=0:
                break
            if num_mesas>len(mesas):
                print("Esa mesa no existe,ingrese una mesa valida")
                continue
            if not validar_mesa(mesas, num_mesas):
                print("La mesa seleccionada ya tiene una comanda abierta. No se puede registrar otra comanda hasta que la actual sea cerrada.")
            else:
                break
        if num_mesas<=0:
                return

        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente == "":
            nombre_cliente = "Cliente anónimo"
        while True:
            empleado,idempleado = u.validar_empleado(empleados)
            if not empleado and not idempleado:
                return
            if empleados[idempleado]['estado'] == 'inactivo':
                print("Este empleado no esta disponible")
                continue
            else:
                break
        ip.imprimirPlatillos(platillos,es_menu=False)
        lista_platillos = []
        total=registrar_platillos(lista_platillos, platillos)
        if total > 0:
            folio+=1
            mostrarComanda(lista_platillos, nombre_cliente, empleado, num_mesas,total)


        continuar = u.validar_s_n("Desea registrar esta comanda? s/n ")
        if continuar == "s":
            mesas[num_mesas] = "no disponible"
            print("Comanda registrada correctamente")
            for folio in range(len(comandas)+1):
                folio+=1
            comandas[folio] = {
                "mesa": num_mesas,
                "cliente":nombre_cliente,
                "empleado": empleado,
                "platillos": lista_platillos,
                "total":total,
                "propina":0,
                "estado": "no pagada"
            }
        
            ca.comandas_abiertas(comandas,empleado)
        else:
            print("Comanda cancelada")
        registrarOtra=u.validar_s_n("Desea registrar otra comanda? s/n: ")
        if registrarOtra == 's':
            #crear_comanda(comandas,mesas,empleados,platillos)
            continue
        elif registrarOtra == 'n':
            return
        

        
   

    

def registrar_platillos(lista_platillos, platillos) -> float:
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Permite al cliente seleccionar platillos, indicando su cantidad, y calcula el total.

    La función interactúa con el usuario para registrar los platillos seleccionados,
    validando que sean válidos y sumando las cantidades si el mismo platillo se elige 
    varias veces. Almacena cada selección en una lista junto con su cantidad y costo 
    individual.

    Parámetros:
    - lista_platillos (list): Lista que almacena tuplas con la información de los 
      platillos seleccionados. Cada tupla contiene:
        (nombre_platillo, cantidad, costo_unitario).
    - platillos (tuple): Tupla con los nombres y precios de los platillos disponibles 
      en el menú.

    Retorna:
    - float: El total acumulado de la selección de platillos, calculado con base en 
      las cantidades y precios.

    """
    total = 0.0
    while True:
        platillo = u.validar_numerico("Platillo: ")
        if platillo - 1 in range(len(platillos)):
            nombre_platillo=u.validar_mismo_platillo(platillo)
            while True:
                cantidad_platillo = u.validar_numerico("Ingrese la cantidad del platillo: ")
                #Obtenemos el valor que el usuario quiere agregar 
                guardar_cantidad=cantidad_platillo
                if cantidad_platillo>0:
                    break
                else:
                    print("La cantidad debe ser mayor a 0. Intente de nuevo.")
            
            if cantidad_platillo >= 1:
                
                for i in lista_platillos:
                    #Si llegara a ser el mismo platillo, la cantidad que se guardo antes se usara para calcular
                    #el total que se le debe agregar al registro de platillo con el que coincide sin añadir 
                    #el total que ya estaba registrado
                    if nombre_platillo == i[0]:
                        print("Pasa a sumar la cantidad")
                        cantidad_platillo+=i[1]

                        lista_platillos.remove(i)
                costoTotal,subtotal = u.Calculos_Comandas(platillo,guardar_cantidad,platillos,cantidad_platillo)
                lista_platillos.append((nombre_platillo, cantidad_platillo, costoTotal))
                total += subtotal
        

                        
        
            
        if platillo>10: 
            print("Opcion no valida. Seleccione un platillo del menú.")
            continue
        if platillo<=-1:
            return total
            
        continuar = u.validar_s_n("¿Desea pedir otro platillo? (s/n): ")

       
        if continuar == "n":
            return total
        elif continuar == "s":
            continue

            
        

def mostrarComanda(lista_platillos: list, nombre_cliente: str, empleado: str, num_mesas: int, total: float):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Muestra los detalles de una comanda registrada, incluyendo el cliente, mesa, empleado, platillos y total.

    La función imprime de forma estructurada la información de la comanda, como los datos del cliente, el número de la mesa, el empleado que atendió, y una lista de los platillos seleccionados con sus cantidades y costos. También muestra el total acumulado.

    Parámetros:
    - lista_platillos (list): Lista de tuplas que contiene los platillos seleccionados. Cada tupla incluye:
    - nombre_cliente (str): Nombre del cliente que realizó la comanda.
    - empleado (str): Nombre o ID del empleado que atendió la comanda.
    - num_mesas (int): Número de la mesa asignada a la comanda.
    - total (float): Total acumulado de la comanda, calculado como la suma de todos los platillos.

    Salida:
    - Muestra en consola el resumen de la comanda en un formato legible.

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
            "estado" : "no pagada" #Pueden ser pagadas o no pagadas
            },
        4:{
            "mesa": 1,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina":0,
            "estado" : "no pagada" #Pueden ser pagadas o no pagadas
        },
        5:{
            "mesa": 5,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina":0,
            "estado" : "no pagada" #Pueden ser pagadas o no pagadas
        },
        2:{
            "mesa": 2,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina":0,
            "estado" : "no pagada" #Pueden ser pagadas o no pagadas
        },
        3:{
            "mesa": 4,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina":0,
            "estado" : "no pagada" #Pueden ser pagadas o no pagadas
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
        1: "no disponible",
        2: "no disponible",
        3: "no disponible",
        4: "no disponible",
        5: "no disponible",
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