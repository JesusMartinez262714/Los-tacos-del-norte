"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
Consultar y mostrar los tres platillos más vendidos y los ingresos generados, basándose en las comandas registradas como "pagadas".

Descripción general:
Este código procesa las comandas pagadas, acumula la cantidad de ventas de cada platillo, y muestra los tres platillos más vendidos junto con los ingresos generados por cada uno. Además, calcula y muestra el total de ingresos de estos platillos más vendidos.
"""

cantidades = []
def consultar_platillos_mas_vendidos(comandas, platillos):
    """
    Consulta y muestra los tres platillos más vendidos y los ingresos generados.

    Datos de entrada:
        comandas (dict): Diccionario que contiene la información de las comandas registradas, donde las claves son los folios y los valores son los detalles de cada comanda (mesa, cliente, platillos, estado, etc.).
        platillos (list): Lista de tuplas, donde cada tupla contiene información sobre un platillo (ID, nombre y precio unitario).

    Proceso:
        - Itera sobre las comandas para procesar solo aquellas con estado "pagada".
        - Extrae y acumula la cantidad vendida de cada platillo.
        - Ordena los platillos según la cantidad vendida y muestra los tres más vendidos.
        - Calcula y muestra los ingresos generados por los tres platillos más vendidos.

    Salida:
        None

    Argumentos:
        comandas: Diccionario con la información de las comandas, donde cada comanda tiene un estado, platillos y otros datos asociados.
        platillos: Lista de platillos con su nombre y precio unitario, utilizada para calcular los ingresos generados.
    """
    if not comandas:
            print("No se han registrado ventas de platillos")
            return
    else:
        venta_encontrada=False
        for folio, datos in comandas.items():
            if datos["estado"] == "pagada":  # Solo procesar comandas pagadas
                venta_encontrada=True
                for platillo in datos['platillos']:
                    agregar_o_actualizar(platillo[0], platillo[1], platillos)  # Sumar directamente
        if not venta_encontrada:
            print("No se han registrado ventas de platillos")
            return

            

    # Ordenar los 3 platillos más vendidos                     rebanada
    top = sorted(cantidades, key=lambda x: x[1], reverse=True)[:3]

    # Imprimir resultados
    print(f"{'':^6}{' Platillos Más Vendidos ':-^42}")
    print(f"{'Platillo':<20}{'Cantidad Vendida':<20}Ingreso Generado")
    print(f"{'':-^56}")
    #top=[1,2]
     # Ajustar rango si hay menos de 3 platillos
    for dentro in top:
        print(f"{dentro[0]:<20}{dentro[1]:<20}{dentro[2]:.2f}")
    print(f"{'':-^56}")

    # Calcular total de ingresos generados
    total_ingresos=0
    for x in top:
        total_ingresos +=x[2]
    print(f"{'Total de Ingresos:':<40}{total_ingresos:.2f}")


def agregar_o_actualizar(platillo, cantidad, platillos):
    """
    Agrega o actualiza el registro de un platillo en la lista de cantidades vendidas.

    Datos de entrada:
        platillo (str): Nombre del platillo a agregar o actualizar en la lista de ventas.
        cantidad (int): Cantidad del platillo que se ha vendido.
        platillos (list): Lista de tuplas, donde cada tupla contiene el ID, nombre y precio de un platillo.

    Proceso:
        - Verifica si el platillo ya existe en la lista de ventas.
        - Si el platillo ya está en la lista, actualiza la cantidad vendida y el costo total.
        - Si el platillo no está en la lista, agrega un nuevo registro con la cantidad y el costo calculado.
        
    Salida:
        None

    Argumentos:
    platillo: El nombre del platillo a agregar o actualizar.
    cantidad: La cantidad de platillos vendidos en esta comanda.
    platillos: Lista de platillos disponibles, donde se obtiene el precio unitario para calcular el costo total.
    """
    # Encontrar el precio unitario del platillo
    precio_unitario = 0
    for posicion in platillos:
        if posicion[1] == platillo:
            precio_unitario = posicion[2]
            break

    # Buscar si el platillo ya está en la lista
    for i in range(len(cantidades)):
        if cantidades[i][0] == platillo:        
            # Actualizar la cantidad y el costo total
            nueva_cantidad = cantidades[i][1] + cantidad
            nuevo_costo = nueva_cantidad * precio_unitario
            cantidades[i] = (platillo, nueva_cantidad, nuevo_costo)
            return
    nuevo_costo = cantidad * precio_unitario
    cantidades.append((platillo, cantidad, nuevo_costo))


# Ejecución
if __name__ == "__main__":
    comandas = {
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
            "estado": "no pagada"
        },
        2: {
            "mesa": 4,
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

    consultar_platillos_mas_vendidos(comandas, platillos)
