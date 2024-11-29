import comandas_abiertas as ca
"""
"""
def fecha() -> str:
    """
    Se obtiene la fecha del día.

    Datos de entrada:
    - Ninguno.

    Proceso:
    - Se obtiene la fecha actual utilizando el módulo `datetime`.
    - Se formatea la fecha en el formato "YYYY-MM-DD".

    Salida:
    - str: La fecha formateada como cadena de texto.

    Argumentos:
    - Ninguno.
    """
    from datetime import datetime  # Usando el modulo datetime
    fechaActual = datetime.now()
    fechaFormateada = fechaActual.strftime("%Y-%m-%d")  # .strftime nos permite escribir la fecha en el formato deseado
    return fechaFormateada  # Regresa como valor el mensaje formateado

fechaHoy = fecha()  # Se obtiene el valor del mensaje para la variable local


def id_por_nombre_platillo(platillos: tuple, nombre_producto: str) -> int:
    """
    Obtiene el ID de un platillo a partir de su nombre.

    Datos de entrada:
    - platillos (tuple): Tupla con los platillos disponibles, donde cada platillo es una tupla con ID, nombre y precio.
    - nombre_producto (str): Nombre del platillo a buscar.

    Proceso:
    - Compara el nombre del platillo con los disponibles en la tupla de `platillos`.
    - Si encuentra el platillo, regresa su ID.

    Salida:
    - int: El ID del platillo encontrado, o `None` si no se encuentra.

    Argumentos:
    - platillos: Tupla de tuplas con los platillos disponibles.
    - nombre_producto: Cadena de texto que representa el nombre del platillo.
    """
    id_producto = None  # Inicializamos el ID como None
    for platillo in platillos:
        if platillo[1] == nombre_producto:  # Compara el nombre del platillo
            id_producto = platillo[0]  # Guarda el ID del platillo
            return id_producto


def validar_numerico(mensaje: str) -> int:
    """
    Solicita al usuario un valor numérico y valida que sea un número entero.

    Datos de entrada:
    - mensaje (str): Mensaje a mostrar al usuario al pedir el dato.

    Proceso:
    - Solicita al usuario un valor numérico, valida si es un número entero.

    Salida:
    - int: Valor numérico validado.

    Argumentos:
    - mensaje: Mensaje que se muestra al usuario para solicitar un valor numérico.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.lstrip("-").isdigit():  # Validamos que sea un número
            return int(entrada)  # Retorna el valor numérico como entero
        else:
            print("Entrada no válida. Ingrese un número.")


def mostrar_resumen(comandas: dict, folio: int, imprimir: str) -> None:
    """
    Muestra el resumen o actualización de una comanda específica.

    Datos de entrada:
    - comandas (dict): Diccionario con las comandas registradas.
    - folio (int): Folio de la comanda que se desea mostrar.
    - imprimir (str): Indicador de si se muestra un resumen o actualización.

    Proceso:
    - Dependiendo del valor de `imprimir`, muestra el resumen o la actualización de la comanda.
    - Itera sobre los platillos en la comanda y muestra sus detalles.

    Salida:
    - Ninguna. Imprime el resumen o actualización de la comanda.

    Argumentos:
    - comandas: Diccionario de comandas registradas.
    - folio: El número de folio de la comanda.
    - imprimir: Cadena que indica si se debe mostrar un resumen o una actualización.
    """
    if folio in comandas:
        print(f"Comanda {folio} Actualizada:") if imprimir == "actualizar" else print(f"Resumen de la comanda {folio}:") if imprimir == "inicio" else print("")
        print(f"Mesa {comandas[folio]['mesa']}")
        print(f"Cliente: {comandas[folio]['cliente']}")
        print(f"Empleado: {comandas[folio]['empleado']}")
        print(f"{'':-^45}")
        print(f"{'Platillo':<20}{'Cant.':<9}{'P.Unit':<10}Total")
        print(f"{'':-^45}")
        contador = 1  # Inicializamos el contador manualmente
        acumulador = 0
        for platillo in comandas[folio]['platillos']:
            nombre = platillo[0]
            cantidad = platillo[1]
            subtotal = platillo[2]
            print(f"{nombre:<20}{cantidad:<9}{subtotal/cantidad:<10}{subtotal}")
            contador += 1  # Incrementamos el contador en cada iteración
            acumulador += subtotal
        print(f"{'':-^45}")
        print(f"{'Total':<39}{acumulador}")
        print(f"{'':-^45}")


def obtener_folio_por_mesa(comandas: dict, numero_mesa: int) -> int:
    """
    Obtiene el folio de la comanda abierta en una mesa específica.

    Datos de entrada:
    - comandas (dict): Diccionario con las comandas registradas.
    - numero_mesa (int): Número de la mesa a verificar.

    Proceso:
    - Busca la mesa en las comandas y retorna el folio asociado.

    Salida:
    - int: El folio de la comanda de la mesa, o `None` si no se encuentra.

    Argumentos:
    - comandas: Diccionario con las comandas registradas.
    - numero_mesa: El número de mesa que se está buscando.
    """
    for folio, datos in comandas.items():
        if datos['mesa'] == numero_mesa:
            return folio  # Si encuentra la mesa, retorna el folio
    return None


def validar_mismo_platillo(platillo: int) -> str:
    """
    Obtiene el nombre del platillo basado en su ID.

    Datos de entrada:
    - platillo (int): ID del platillo.

    Proceso:
    - Se asigna el nombre correspondiente al platillo según su ID.

    Salida:
    - str: Nombre del platillo.

    Argumentos:
    - platillo: ID del platillo que se desea obtener.
    """
    platillo_dict = {
        1: 'Tacos de Asada',
        2: 'Tacos de Pastor',
        3: 'Quesadilla',
        4: 'Refresco',
        5: 'Burrito de Asada',
        6: 'Burrito de Pastor',
        7: 'Torta de Asada',
        8: 'Torta de Pastor',
        9: 'Agua Fresca (1L)',
        10: 'Flautas (3 piezas)'
    }
    return platillo_dict.get(platillo, "")


def calcular_total(folio: int, comandas: dict) -> None:
    """
    Calcula el total de una comanda según los platillos registrados.

    Datos de entrada:
    - folio (int): Folio de la comanda.
    - comandas (dict): Diccionario con las comandas registradas.

    Proceso:
    - Itera sobre los platillos en la comanda y suma los subtotales para obtener el total.

    Salida:
    - Ninguna. Actualiza el total en la comanda.

    Argumentos:
    - folio: Número de folio de la comanda.
    - comandas: Diccionario con las comandas registradas.
    """
    comanda = comandas.get(folio)  # Obtener la comanda por su folio
    if comanda:
        total = 0
        # Iterar sobre los platillos de la comanda
        for platillo in comanda['platillos']:
            subtotal = platillo[2]  # El subtotal está en la posición 2 de la tupla
            if subtotal is None:  # Si el subtotal es None, asignar un valor predeterminado
                subtotal = 0
            total += subtotal  # Sumar el subtotal al total

        # Actualizar el total de la comanda
        comanda['total'] = total
    else:
        print("Comanda no encontrada.")


def verificar_comanda(comandas: dict) -> int:
    """
    Verifica si existe una comanda abierta para una mesa.

    Datos de entrada:
    - comandas (dict): Diccionario con las comandas abiertas.

    Proceso:
    - Solicita al usuario el número de mesa y verifica si hay una comanda abierta.
    - Si hay una comanda abierta, muestra el resumen.

    Salida:
    - int: El folio de la comanda, o `None` si no se encuentra.

    Argumentos:
    - comandas: Diccionario de comandas abiertas.
    """
    ca.comandas_abiertas(comandas)
    verificar = validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
    folio = obtener_folio_por_mesa(comandas, verificar)

    for datos in comandas.values():
        if verificar == datos['mesa'] and datos['estado'] == "No pagada":
            mostrar_resumen(comandas, folio, imprimir="inicio")
            break
        else:
            print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
    return folio


def validar_empleado(empleados: dict) -> tuple:
    """
    Valida si un empleado se encuentra registrado en el sistema.

    Datos de entrada:
    - empleados (dict): Diccionario con los empleados registrados.

    Proceso:
    - Solicita el ID del empleado y valida si existe en el sistema.

    Salida:
    - tuple: Una tupla con el nombre y el ID del empleado.

    Argumentos:
    - empleados: Diccionario con los empleados registrados.
    """
    while True:
        empleado = validar_numerico("Ingrese el id del empleado: ")
        if empleado == -1:
            return
        if empleado in empleados:
            return empleados[empleado]["nombre"], empleado
        else:
            print("El empleado no está registrado, intente de nuevo.")


def validar_s_n(mensaje: str) -> str:
    """
    Solicita al usuario una respuesta de sí o no.

    Datos de entrada:
    - mensaje (str): Mensaje que se muestra al usuario.

    Proceso:
    - Solicita y valida que la respuesta sea 's' o 'n'.

    Salida:
    - str: La respuesta del usuario ('s' o 'n').

    Argumentos:
    - mensaje: Mensaje que se muestra al usuario para obtener una respuesta.
    """
    while True:
        entrada = input(mensaje).strip().lower()  # Obtener la entrada y convertirla a minúsculas
        if entrada == 's' or entrada == 'n':  # Verificar si la entrada es 's' o 'n'
            return entrada  # Retorna 's' o 'n' como respuesta válida
        else:
            print("Entrada no válida. Por favor ingrese 's' o 'n'.")  # Mensaje si la entrada es incorrecta
