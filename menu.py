"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo:
    Sistema de gestión para una taquería que incluye funcionalidades para comandas,
    empleados, mesas, ventas y más.
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

def menu_principal() -> None:
    """
    Función principal que muestra el menú de opciones y permite interactuar con el sistema.

    Datos de entrada:
        Ninguno directamente, pero utiliza estructuras predefinidas como `comandas`, `mesas`, `empleados` y `platillos`.

    Proceso:
        - Muestra un menú principal con opciones.
        - Ejecuta las funciones correspondientes basadas en la selección del usuario.
        - Valida las opciones ingresadas para evitar errores.

    Salida:
        Ninguna directa, pero puede modificar las estructuras globales como `comandas`, `mesas`, `empleados` y registrar acciones del sistema.

    Argumentos:
        Ninguno.
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
        opcion = u.validar_numerico("Seleccione una opción: ")

        if opcion == 1:
            rc.crear_comanda(comandas, mesas, empleados, platillos)
        elif opcion == 2:
            ac.menu_actualizaciones(comandas, platillos, es_menu="si")
        elif opcion == 3:
            ab.comandas_abiertas(comandas)
        elif opcion == 4:
            cc.cerrar_comanda(comandas, platillos, mesas)
        elif opcion == 5:
            cem.consultar_estado_mesas(mesas)
        elif opcion == 6:
            cv.consultar_ventas(comandas, empleados)
        elif opcion == 7:
            cpmv.consultar_platillos_mas_vendidos(comandas, platillos)
        elif opcion == 8:
              cp.calcular_propina(comandas,empleados)
            # calcular_propinas(empleados, historial_ventas)
        elif opcion == 9:
            ip.imprimirPlatillos(es_menu=True)
        elif opcion == 10:
            ge.menu_empleados(empleados)
        elif opcion == 11:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 11.")
        print("")


# Estructuras iniciales

comandas: dict = {}
"""
Descripción de `comandas`:
Diccionario que gestiona las comandas activas.
- Clave: Folio único de la comanda.
- Valor: Diccionario con datos como mesa, cliente, empleado, platillos, total, propina y estado.
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
Descripción de `mesas`:
Diccionario que representa el estado de las mesas.
- Clave: Número único de la mesa.
- Valor: Estado actual ("disponible" o "no disponible").
"""

empleados: dict = {
    101: {"nombre": "María López", "telefono": "6441234567", "estado": "activo"},
    102: {"nombre": "Pedro Martínez", "telefono": "6449876543", "estado": "inactivo"},
}
"""
Descripción de `empleados`:
Diccionario que almacena información de los empleados.
- Clave: ID único del empleado.
- Valor: Diccionario con nombre, teléfono y estado.
"""

platillos: tuple = (
    (1, "Tacos de Asada", 20.00),
    (2, "Tacos de Pastor", 18.00),
    (3, "Quesadilla", 25.00),
    (4, "Refresco", 15.00),
    (5, "Burrito de Asada", 40.00),
    (6, "Burrito de Pastor", 38.00),
    (7, "Torta de Asada", 45.00),
    (8, "Torta de Pastor", 43.00),
    (9, "Agua Fresca (1L)", 20.00),
    (10, "Flautas (3 piezas)", 30.00),
)
"""
Descripción de `platillos`:
Tupla de tuplas que representa un menú inmutable.
- Cada elemento contiene ID, nombre del platillo y precio.
"""

# Mandar llamar la función principal
menu_principal()
