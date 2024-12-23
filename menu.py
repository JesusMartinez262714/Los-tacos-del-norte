"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
Implementar un sistema de gestión para una taquería, que permita realizar tareas como registrar y actualizar comandas, 
consultar el estado de mesas, gestionar empleados, calcular propinas, y generar reportes de ventas y platillos más vendidos. 
"""
import registrar_comanda as rc
import actualizar_comanda as ac
import comandas_abiertas as ab
import cerrar_comanda as cc
import consultar_estado_mesas as cem
import consultar_ventas as cv
import consultar_platillos_mas_vendidos as cpmv
import calcular_propina as cp
import imprimir_platillos as ip
import gestionar_empleados as ge
import utilerias as u
# Estructuras iniciales
"""
Descripción de la comanda, es un diccionario de diccionarios, donde:
la llave es el folio, el value:
    mesa: Número de la mesa asociada a la comanda.
    cliente: Nombre del cliente. Si no se proporciona, es "Cliente Anónimo".
    empleado: Nombre del empleado que atiende.
    platillos: Lista de tuplas, donde cada tupla incluye:
        Nombre del platillo.
        Cantidad pedida.
        Subtotal (cantidad × precio unitario).
    total: Total acumulado de la comanda.
    propina: propina dada por el usuario, se deja como 0 al inicio, o se puede agregar despues
    estado: indica el estado de la comanda (pagada o no pagada)
"""

#Lista para agrupar todas los datos de la comanda en registrar comanda


#Comandas

comandas = {

}


"""
Mesas es un diccionario donde:

La llave es el número único de la mesa.
El valor indica el estado actual de la mesa, con los posibles valores:
"disponible": La mesa está libre y puede asignarse a una nueva comanda.
"no disponible": La mesa está ocupada por una comanda activa.
"""
mesas = {
        1: "disponible",
        2: "disponible",
        3: "disponible",
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

"""
Empleados 3s un diccionario donde:

La llave es el ID único del empleado.
El valor es otro diccionario que contiene los siguientes datos:
    nombre: Nombre completo del empleado.
    telefono: Número de contacto del empleado.
    estado: Indica si el empleado está disponible para trabajar:
        "activo": El empleado está trabajando y disponible para asignaciones.
        "inactivo": El empleado no está disponible.
"""
empleados = {
    101: {
        "nombre": "María López",
        "telefono": "6441234567",
        "estado": "activo"
    },
    102: {
        "nombre": "Pedro Martínez",
        "telefono": "6449876543",
        "estado": "activo"
    }
}

"""
Los platillos se almacenan como una tupla de tuplas, ya que el menú es fijo y no debe modificarse. Cada elemento de la tupla principal representa un platillo, y su estructura interna es:

ID (int): Número único del platillo en el menú.
Nombre (str): Nombre del platillo.
Precio (float): Precio del platillo en pesos mexicanos

Al ser una tupla de tuplas, el menú es inmutable, asegurando que no se modifique accidentalmente durante la ejecución del programa.

"""

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

"""
Propinas por Empleado
Propósito: Calcular y almacenar las propinas acumuladas para cada empleado.
Estructura: Diccionario donde:
Llave: ID del empleado.
Valor: Total de propinas acumuladas.
"""
propinas_empleados = {
    101: 50.00,  # María López
    102: 35.00   # Pedro Martínez
}



# Función de menu

def menu_principal():
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720

    Muestra el menú principal de la taquería y permite al usuario seleccionar 
    una opción para realizar diversas acciones relacionadas con las comandas, 
    mesas, empleados, ventas, y platillos.
    """
    while True:
        print("")
        print("---- Taqueria Los Tacos del Norte -----")
        print("---------- Menú Principal ----------")
        print("1. Registrar una nueva comanda.")
        print("2. Actualizar una comanda existente.")
        print("3. Consultar comandas abiertas.")
        print("4. Cerrar una comanda y generar cuenta.")
        print("5. Consultar el estado de las mesas (ocupadas/disponibles).")
        print("6. Consultar ventas del día.")
        print("7. Consultar platillos más vendidos.")
        print("8. Calcular propinas de un empleado.")
        print("9. Imprimir platillos disponibles.")
        print("10. Gestionar empleados.")
        print("11. Salir del sistema.")
        print("--------------------------------------")

        # Validar que la opción ingresada sea válida
        opcion = u.validar_numerico("Seleccione una opción:  ")
        
        if opcion == 1:
            # registrar_comanda(comandas, mesas, empleados, platillos)
            rc.crear_comanda(comandas,mesas,empleados,platillos)
        elif opcion == 2:
            # actualizar_comanda(comandas, platillos)
            ac.menu_actualizaciones(comandas,platillos,es_menu="si")
        elif opcion == 3:
             ab.comandas_abiertas(comandas,nombre_empleado="")
            # consultar_comandas_abiertas(comandas)
        elif opcion == 4:
             cc.cerrar_comanda(comandas,mesas,propinas_empleados,empleados)
            # cerrar_comanda(comandas, mesas, historial_ventas)
        elif opcion == 5:
             cem.consultar_estado_mesas(mesas)
            # consultar_estado_mesas(mesas)
        elif opcion == 6:
             cv.consultar_ventas(comandas,empleados)
            # consultar_ventas_dia(historial_ventas)
        elif opcion == 7:
              cpmv.consultar_platillos_mas_vendidos(comandas,platillos)
            # consultar_platillos_mas_vendidos(historial_ventas, platillos)
        elif opcion == 8:
              cp.calcular_propina(comandas,empleados,propinas_empleados)
            # calcular_propinas(empleados, historial_ventas)
        elif opcion == 9:
              ip.imprimirPlatillos(platillos,es_menu=True)
            # imprimir_platillos(platillos)
        elif opcion == 10:
              ge.menu_empleados(empleados)
            # gestionar_empleados(empleados)
        elif opcion == 11:
            print("Saliendo del sistema. ¡Gracias por visitar la Taqueria los Tacos del Norte!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 11.")
        
        print("")



#Mandamos llamar la funcion menu, para que inicie el programa
menu_principal()