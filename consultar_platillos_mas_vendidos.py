cantidades: list = []
""""""

def consultar_platillos_mas_vendidos(comandas: dict, platillos: list) -> None:
    """
    Consulta los platillos más vendidos y calcula los ingresos generados por ellos.

    Datos de entrada:
    - comandas (dict): Diccionario con las comandas registradas. Cada comanda incluye los detalles de los platillos.
    - platillos (list): Lista de tuplas con los datos de cada platillo disponible en el menú. Cada tupla contiene:
        (id, nombre, precio).

    Proceso:
    1. Iterar sobre las comandas que tienen estado 'pagada'.
    2. Contar la cantidad de cada platillo vendido y calcular el ingreso total generado por cada uno.
    3. Almacenar los resultados en la lista global `cantidades`.
    4. Ordenar los platillos por la cantidad vendida y seleccionar los tres más vendidos.
    5. Mostrar en consola un reporte de los platillos más vendidos con sus ingresos generados.

    Salida:
    - Muestra en consola los tres platillos más vendidos y el total de ingresos generados por ellos.

    Argumentos:
    - comandas: Diccionario con información de las comandas.
    - platillos: Lista de tuplas con la información de los platillos.

    Retorno:
    - None
    """
    cantTacosAsada = 0
    cantTacosPastor = 0
    cantQuesadillas = 0
    cantRefrescos = 0
    cantBurritoAsada = 0
    cantBurritoPastor = 0
    cantTortaAsada = 0
    cantTortaPastor = 0
    cantAguaFresca = 0
    cantFlautas = 0

    for folio, datos in comandas.items():
        if datos["estado"] == "pagada":
            for platillo in datos["platillos"]:
                if platillo[0] == "Tacos de Asada":
                    cantTacosAsada += platillo[1]
                    agregar_o_actualizar(platillo[0], cantTacosAsada, platillos)
                elif platillo[0] == "Tacos de Pastor":
                    cantTacosPastor += platillo[1]
                    agregar_o_actualizar(platillo[0], cantTacosPastor, platillos)
                elif platillo[0] == "Quesadillas":
                    cantQuesadillas += platillo[1]
                    agregar_o_actualizar(platillo[0], cantQuesadillas, platillos)
                elif platillo[0] == "Refresco":
                    cantRefrescos += platillo[1]
                    agregar_o_actualizar(platillo[0], cantRefrescos, platillos)
                elif platillo[0] == "Burrito de Asada":
                    cantBurritoAsada += platillo[1]
                    agregar_o_actualizar(platillo[0], cantBurritoAsada, platillos)
                elif platillo[0] == "Burrito de Pastor":
                    cantBurritoPastor += platillo[1]
                    agregar_o_actualizar(platillo[0], cantBurritoPastor, platillos)
                elif platillo[0] == "Torta de Asada":
                    cantTortaAsada += platillo[1]
                    agregar_o_actualizar(platillo[0], cantTortaAsada, platillos)
                elif platillo[0] == "Torta de Pastor":
                    cantTortaPastor += platillo[1]
                    agregar_o_actualizar(platillo[0], cantTortaPastor, platillos)
                elif platillo[0] == "Agua Fresca (1L)":
                    cantAguaFresca += platillo[1]
                    agregar_o_actualizar(platillo[0], cantAguaFresca, platillos)
                elif platillo[0] == "Flautas (3 piezas)":
                    cantFlautas += platillo[1]
                    agregar_o_actualizar(platillo[0], cantFlautas, platillos)
        else:
            print("No se han registrado ventas de platillos.")
            return

    # Ordenar los platillos por cantidad vendida y mostrar los tres más vendidos
    top = sorted(cantidades, key=lambda x: x[1], reverse=True)[:3]
    print(f"{'':^6}{' Platillos Más Vendidos ':-^42}")
    print("\nPlatillo               Cantidad Vendida      Ingreso Generado\n")
    print(f"{'':-^56}")

    rango = min(len(top), 3)
    for i in range(rango):
        print(f"{top[i][0]:<20}{top[i][1]:<20}{top[i][2]:.2f}")
    print(f"{'':-^56}")

    totalIngresos = sum(x[2] for x in top)
    print(f"{'Total de Ingresos:':<40}{totalIngresos:.2f}")


def agregar_o_actualizar(platillo: str, cantidad: int, platillos: list) -> None:
    """
    Agrega o actualiza un platillo en la lista de cantidades vendidas.

    Datos de entrada:
    - platillo (str): Nombre del platillo vendido.
    - cantidad (int): Cantidad vendida del platillo.
    - platillos (list): Lista de tuplas con la información de los platillos disponibles.

    Proceso:
    1. Buscar si el platillo ya existe en la lista global `cantidades`.
    2. Si existe, actualizar la cantidad y calcular el nuevo ingreso generado.
    3. Si no existe, agregarlo como una nueva entrada en `cantidades`.

    Salida:
    - Actualiza la lista global `cantidades`.

    Argumentos:
    - platillo: Nombre del platillo vendido.
    - cantidad: Cantidad vendida del platillo.
    - platillos: Lista de platillos con sus precios.

    Retorno:
    - None
    """
    # Buscar si el platillo ya existe en la lista
    for i in range(len(cantidades)):
        if cantidades[i][0] == platillo:
            cant = cantidades[i][1] + cantidad
            for x in platillos:
                if x[1] == platillo:
                    cantidades[i] = (platillo, cant, cant * x[2])
            return

    # Si no existe, agregar el platillo como una nueva tupla
    for i in platillos:
        if platillo == i[1]:
            cantidades.append((platillo, cantidad, cantidad * i[2]))







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
    },
    2:{     
            "mesa": 4,
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
        "mesa": 5,
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
    consultar_platillos_mas_vendidos(comandas,platillos)