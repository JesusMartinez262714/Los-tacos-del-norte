import utilerias as u

fechaHoy = u.fecha()  # Obtener la fecha del día actual

def consultar_ventas(comandas, empleados):
    totalP = 0
    totalT = 0
    print(f"{'':^12}{' Ventas del Día: ':->26}{fechaHoy:-<20}")
    print("")
    print(f"{'folio':<9}{'Mesa':<7}{'Cliente':<19}{'Empleado':<17}{'Total':<10}Propina")
    print(f"{'':-^73}")
    
    for folio, datos in comandas.items():
        if datos['estado'] == 'pagada':
            print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
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
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{'':-^73}")
                    mesa_encontrada = True
            if not mesa_encontrada:
                print(f"No hay ventas registradas para la mesa {mesa}.")
        elif filtro == 2:
            Empleado, id = u.validar_empleado(empleados)
            empleado_encontrado = False
            for folio, datos in comandas.items():
                if datos['estado'] == 'pagada' and datos['empleado'] == Empleado:
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{'':-^73}")
                    empleado_encontrado = True
            if not empleado_encontrado:
                print(f"No hay ventas registradas para el empleado {Empleado}.")
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    comandas = {
        1: {
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
        2: {
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "no pagada"
        },
        3: {
            "mesa": 1,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
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
    
    consultar_ventas(comandas, empleados)
