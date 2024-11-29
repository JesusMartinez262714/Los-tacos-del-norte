import utilerias as u
""""""

fechaHoy=u.fecha()#Obtener la fecha del dia actual

def consultar_ventas(comandas: dict, empleados: dict) -> None:
    """
    Función para consultar las ventas realizadas en el día.

    Datos de entrada:
        - Comandas (Dict): Contiene información sobre las comandas, su estado, mesa, cliente, empleado, total y propina.
        - Empleados (Dict): Contiene información de los empleados para validar filtros por empleado.

    Proceso:
        1. Se imprimen las ventas realizadas durante el día, mostrando detalles de cada comanda pagada.
        2. Se calculan e imprimen los totales acumulados de ventas y propinas.
        3. Se ofrece la opción de filtrar las ventas por número de mesa o por empleado.
        4. Si se selecciona un filtro, se valida el criterio y se muestran los registros correspondientes.
        5. Si no hay ventas registradas que coincidan con el filtro, se muestra un mensaje de advertencia.

    Salida:
        - Impresión de las ventas del día, totales de ventas y propinas.
        - Impresión de los registros filtrados por mesa o empleado, en caso de seleccionar un filtro.

    Argumentos:
        - comandas (Dict): Información de las comandas registradas.
        - empleados (Dict): Información de los empleados para validación en los filtros.

    """
      #formateo y hacer que se muestre al registrar una comanda
    totalP=0
    totalT=0
    print(f"{"":^12}{" Ventas del Día: ":->26}{fechaHoy:-<20}")
    print("")
    print(f"{"folio":<9}{"Mesa":<7}{"Cliente":<19}{"Empleado":<17}{"Total":<10}Propina")
    print(f"{"":-^73}")
    for folio,datos in comandas.items():

        if datos['estado'] == 'pagada':
            #agrega la fecha con el daytime
            print(f"{folio:<9}{datos['mesa']:<7}{datos['cliente']:<19}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
            print(f"{"":-^73}")
            totalP+=int(datos['propina'])
            totalT+=int(datos['total'])
            print(f"{"Total del Día:":<48}${totalT:<10}${totalP}")


            filtro=u.validar_numerico("Desea filtrar por mesa (1) o empleado (2)? (-1 para salir)")
            if filtro == -1:
                return
            elif filtro==1:
                mesa=u.validar_numerico("Ingrese el numero de la mesa: ")
                if mesa == datos['mesa']:
                    print(f"{"":-^73}")
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{"":-^73}")
                else:
                    print(f"No hay ventas registradas para la mesa {mesa}")  
            elif filtro==2:
                Empleado,id=u.validar_empleado(empleados)
                if Empleado == datos['empleado']:
                    print(f"{"":-^73}")
                    print(f"{folio:<9}{datos['mesa']:<6}{datos['cliente']:<16}{datos['empleado']:<17}${datos['total']:<10}${datos['propina']}")
                    print(f"{"":-^73}")
                else:
                    print(f"No hay ventas registradas para el empleado {Empleado}")
    return


if __name__ == "__main__":
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
    consultar_ventas(comandas,empleados)