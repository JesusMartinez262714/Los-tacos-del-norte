"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
Consultar las ventas del día, mostrando un resumen de las comandas pagadas, propinas y totales. Permitir al usuario filtrar las ventas por número de mesa o por empleado.

Descripción general:
Este código muestra un resumen de las ventas realizadas durante el día, incluyendo el total de las comandas pagadas y las propinas. Permite al usuario filtrar las ventas por mesa o por empleado. Si no se han registrado ventas para el filtro seleccionado, se muestra un mensaje indicativo. El resumen de ventas también incluye el total acumulado del día.
"""

import utilerias as u

fechaHoy = u.fecha()  # Obtener la fecha del día actual

def consultar_ventas(comandas, empleados):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Consulta las ventas del día, mostrando un resumen de las comandas pagadas, propinas y totales.
    Permite filtrar las ventas por mesa o por empleado.

    Parámetros:
    - comandas (dict): Diccionario que contiene las comandas, donde cada clave es el folio y cada valor es un diccionario con los detalles de la comanda.
    - empleados (dict): Diccionario con los empleados, donde cada clave es el ID del empleado y el valor es su nombre.

    Proceso:
        - Muestra el resumen de todas las comandas pagadas con su total y propina.
        - Muestra un total del día con la suma de todos los totales y propinas.
        - Permite al usuario filtrar las ventas por número de mesa o empleado.
        - Si se selecciona un filtro, muestra las comandas que coincidan con los criterios especificados.
    
    Salida:
    - Imprime en pantalla el resumen de ventas del día, con el total de ventas y propinas.
    - Si el usuario selecciona un filtro, muestra las comandas correspondientes a la mesa o empleado seleccionado.
    - Si no hay ventas registradas para la mesa o empleado seleccionado, muestra un mensaje indicativo.

    Argumentos:
    - comandas: Un diccionario que contiene las comandas pagadas con sus detalles, incluyendo total y propina.
    - empleados: Un diccionario con los empleados registrados y su información.
    """
    
    if all(datos["estado"] == "no pagada" for datos in comandas.values()):
        print(f"No hay ventas registradas para el dia {fechaHoy}")
        return
    totalP = 0
    totalT = 0
   
    print(f"{'':^12}{' Ventas del Día: ':->26}{fechaHoy:-<20}")
    print("")
    print(f"{'folio':<9}{'Mesa':<7}{'Cliente':<19}{'Empleado':<17}{'Total':<10}Propina")
    print(f"{'':-^73}")
    ordenado_por_folio = (
    dict(sorted(comandas.items(), key=lambda x: x[0]))
    if comandas else {}
    )
    for folio, datos in ordenado_por_folio.items():
        if datos['estado'] == 'pagada':
            print(f"{folio:<9}{datos['mesa']:<7}{datos['cliente']:<19}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
            print(f"{'':-^73}")
            totalP += int(datos['propina'])
            totalT += int(datos['total'])
    
    print(f"{'Total del Día:':<48}${totalT:<10}${totalP}")
    
    while True:
        filtro = u.validar_numerico("Desea filtrar por mesa (1) o empleado (2)? (-1 para salir): ")
        if filtro == -1:
            return
        elif filtro == 1:
            mesa = u.validar_numerico("Ingrese el número de la mesa: ")
            mesa_encontrada = False
           
            for folio, datos in comandas.items():
                if datos['estado'] == 'pagada' and datos['mesa'] == mesa:
                    if not mesa_encontrada:
                        print(f"{'folio':<9}{'Mesa':<7}{'Cliente':<19}{'Empleado':<17}{'Total':<10}Propina")
                        print(f"{'':-^73}")
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{'':-^73}")
                    mesa_encontrada = True
            if not mesa_encontrada:
                print(f"No hay ventas registradas para la mesa {mesa}.")
        elif filtro == 2:
            Empleado, id = u.validar_empleado(empleados)
            empleado_encontrado = False

            # Primero validamos si hay ventas registradas para el empleado
            for folio, datos in comandas.items():
                if datos['estado'] == 'pagada' and datos['empleado'] == Empleado:
                    if not empleado_encontrado:
                        # Solo imprimimos el encabezado si encontramos ventas para el empleado
                        print(f"{'folio':<9}{'Mesa':<7}{'Cliente':<19}{'Empleado':<17}{'Total':<10}Propina")
                        print(f"{'':-^73}")
                    
                    # Imprimimos la información de la comanda
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{'':-^73}")
                    
                    empleado_encontrado = True
            # Si no se han encontrado ventas, mostramos el mensaje
            if not empleado_encontrado:
                print(f"No hay ventas registradas para el empleado {Empleado}.")
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    comandas = {
        5: {
            "mesa": 5,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        3: {
            "mesa": 5,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        1: {
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        6: {
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        2: {
            "mesa": 1,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "no pagada"
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
    
    consultar_ventas(comandas,empleados)
