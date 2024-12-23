"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
Implementar diversas funciones para la gestión de comandas en un sistema de restaurante. 
Incluye funcionalidades como la obtención de la fecha actual, la validación de platillos, el cálculo de totales, 
y la verificación de comandas abiertas.

Descripción general:
Este conjunto de funciones permite gestionar las comandas en un sistema de restaurante. 
La función 'fecha()' obtiene la fecha actual. 'id_por_nombre_platillo()' busca el ID de un platillo por su nombre,
mientras que 'validar_numerico()' asegura que la entrada del usuario sea un número entero. La función 'mostrar_resumen()' 
genera un resumen de los platillos en una comanda específica, mientras que 'obtener_folio_por_mesa()' obtiene el folio de 
una comanda basado en el número de mesa. Además, 'validar_mismo_platillo()' valida el nombre de un platillo a partir de su número, y 
'calcular_total()' actualiza el total de una comanda según los platillos seleccionados. 'verificar_comanda()' permite verificar si una 
comanda está abierta para una mesa específica, y 'validar_empleado()' valida si un empleado está registrado en el sistema. Finalmente, 
'validar_s_n()' gestiona la entrada de respuestas sí/no.
"""

import comandas_abiertas as ca

def fecha():
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Obtiene la fecha actual del día en formato 'YYYY-MM-DD'.

    La función utiliza el módulo 'datetime' para obtener la fecha actual y formatearla en el estándar (año-mes-día).

    Retorno:
    - str: La fecha actual en formato 'YYYY-MM-DD'.

    """
    from datetime import datetime #Usando el modulo datetime
    fechaActual = datetime.now()
    fechaFormateada = fechaActual.strftime("%Y-%m-%d")#.strftime nos permite el escribir la fecha en el formato que se desee
    return fechaFormateada#Regresamos como valor el mensaje formateado
fechaHoy=fecha()#Se obetiene el valor del mensaje para la variable local


def id_por_nombre_platillo(platillos,nombre_producto):
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Busca el ID de un platillo basado en su nombre.

    Parámetros:
    - platillos (list/tuple): Lista o tupla de platillos, donde cada elemento es una tupla (ID, nombre, precio).
    - nombre_producto (str): Nombre del producto cuyo ID se desea obtener.

    Retorna:
    - int: El ID del platillo si se encuentra.
    - None: Si no se encuentra un platillo con el nombre proporcionado.

    """
    id_producto = None  # Inicializamos el ID como None
    for platillo in platillos:
        if platillo[1] == nombre_producto:  # Compara el nombre del platillo
            id_producto = platillo[0]  # Guarda el ID del platillo
            return id_producto

def validar_numerico(mensaje: str) -> int:
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Solicita al usuario un valor numérico y valida que sea un número entero.

    Parámetros:
    - mensaje (str): Mensaje a mostrar al usuario al pedir el dato.

    Retorna:
    - int: Valor numérico validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.lstrip("-").isdigit():  # Validamos que sea un número
            return int(entrada)  # Retorna el valor numérico como entero
        else:
            print("Entrada no válida. Ingrese un número.")






def mostrar_resumen(comandas,folio,imprimir):
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Muestra el resumen de una comanda específica, incluyendo mesa, cliente, empleado, platillos y total.

    Parámetros:
    - comandas (dict): Diccionario que almacena las comandas registradas.
    - folio (int): Número único que identifica la comanda.
    - imprimir (str): Indica el tipo de mensaje que se mostrará:
        - "actualizar" para mostrar que la comanda fue actualizada.
        - "inicio" para mostrar el inicio de un resumen de comanda.
        - Otros valores mostrarán solo el resumen sin encabezado adicional.
    """
    if folio in comandas:
        print (f"Comanda {folio} Actualizada:") if imprimir=="actualizar" else print(f"Resumen de la comanda {folio}:") if imprimir == "inicio" else print ("")
        print(f"Mesa {comandas[folio]['mesa']}" )
        print(f"Cliente: {comandas[folio]['cliente']}")
        print(f"Empleado: {comandas[folio]['empleado']}")
        print(f"{"":-^45}")
        print(f"{"Platillo":<20}{"Cant.":<9}{"P.Unit":<10}Total")
        print(f"{"":-^45}")
        contador = 1  # Inicializamos el contador manualmente
        acumulador=0
        for platillo in comandas[folio]['platillos']:
            nombre = platillo[0]
            cantidad = platillo[1]
            subtotal = platillo[2]
            print(f"{nombre:<20}{cantidad:<9}{subtotal/cantidad:<10}{subtotal}")
            contador += 1  # Incrementamos el contador en cada iteración
            acumulador+=subtotal
        print(f"{"":-^45}")
        print(f"{"Total":<39}{acumulador}")
        print(f"{"":-^45}")

def obtener_folio_por_mesa(comandas:dict, numero_mesa:int):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Obtiene el folio de una comanda asociada a un número de mesa.

    Parámetros:
    - comandas (dict): Diccionario que almacena las comandas registradas.
    - numero_mesa (int): Número de la mesa para la cual se busca el folio.

    Retorna:
    - int: Folio de la comanda asociada a la mesa, si existe.
    - None: Si no se encuentra ninguna comanda para la mesa especificada.

    """
    for folio, datos in comandas.items():
        if datos['mesa'] == numero_mesa:
            return folio  # Si encuentra la mesa, retorna el folio
    return None

def validar_mismo_platillo(platillo):
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Valida y asigna el nombre correspondiente a un número de platillo.

    Parámetros:
    - platillo (int): Número del platillo seleccionado.

    Retorna:
    - str: Nombre del platillo correspondiente.
    """
    if platillo==1:
        platillo='Tacos de Asada'
    if platillo==2:
        platillo='Tacos de Pastor'
    if platillo==3:
        platillo='Quesadilla'
    if platillo==4:
        platillo='Refresco'
    if platillo==5:
        platillo='Burrito de Asada'
    if platillo==6:
        platillo='Burrito de Pastor'
    if platillo==7:
        platillo='Torta de Asada'
    if platillo==8:
        platillo='Torta de Pastor'
    if platillo==9:
        platillo='Agua Fresca (1L)'
    if platillo==10:
        platillo='Flautas (3 piezas)'
    return platillo

def calcular_total(folio, comandas):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Calcula y actualiza el total de una comanda basada en los platillos seleccionados.

    Parámetros:
    - folio (int): Folio de la comanda a calcular.
    - comandas (dict): Diccionario que contiene las comandas registradas.
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

def verificar_comanda(comandas:dict,debe_mostrar):
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Verifica si una comanda está abierta para la mesa especificada.

    Parámetros:
    - comandas dict: Diccionario con las comandas abiertas.
    - platillos Tuple: Tupla que contiene los platillos disponibles.

    Retorna:
     El folio de la comanda si se encuentra, o None si no existe una comanda abierta para la mesa.
    """
    valor=ca.comandas_abiertas(comandas,nombre_empleado="")

    if not valor:
        return valor
    while True:
        verificar = validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
        if verificar<0:
            folio=None
            return folio
        folio = obtener_folio_por_mesa(comandas, verificar)
        bandera=False
        for datos in comandas.values():
            if verificar == datos['mesa'] and datos['estado'] == "no pagada":
                if debe_mostrar:
                    mostrar_resumen(comandas,folio,imprimir="inicio")
                bandera=True
                break
        if not bandera:
            print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
            folio=None
            return folio
        return folio

def validar_empleado(empleados):
    """
    Desarrollado por: Contreras Avila Ramses Norberto 262720

    Valida si un empleado se encuentra registrado en el sistema.

    Parámetros:
    - empleados (dict): Diccionario con los IDs de los empleados.

    Retorna:
    - int: ID del empleado válido.
    """
    while True:
        empleado = validar_numerico("Ingrese el id del empleado: ")
        if empleado == 0:
            return False,False
        if empleado in empleados:
            return empleados[empleado]["nombre"],empleado
            
        else:
            print("El empleado no esta registrado. Proporcione un empleado valido.")

def validar_s_n(mensaje):
    while True:
        entrada = input(mensaje).strip().lower()  # Obtener la entrada y convertirla a minúsculas
        if entrada == 's' or entrada == 'n':  # Verificar si la entrada es 's' o 'n'
            return entrada  # Retorna 's' o 'n' como respuesta válida
        else:
            print("Entrada no válida. Por favor ingrese 's' o 'n'.")  # Mensaje si la entrada es incorrecta

def Calculos_Comandas(platillo, cantidad_platillo,platillos,cantidadPlatilloTotal):
    """
    Desarrollado por: Jesus Manuel Martinez Cortez 262714

    Calcula el costo y subtotal de un platillo seleccionado.

    Parámetros:
    - platillo (int): Número del platillo seleccionado.
    - cantidad_platillo (int): Cantidad de ese platillo.

    Retorna:
    - tuple: Costo por platillo y subtotal calculado.
    """
    #Esta variable se usa para calcular lo que se debe sumar al total a cumulado en el platilloo tambien si es que quiero agregar un nuevo platillo
    costo = cantidad_platillo * platillos[0][2] if platillo == 1 else cantidad_platillo * platillos[1][2] if platillo == 2 else cantidad_platillo * platillos[2][2] if platillo == 3 else cantidad_platillo * platillos[3][2] if platillo == 4 else cantidad_platillo * platillos[4][2] if platillo == 5 else cantidad_platillo * platillos[5][2] if platillo == 6 else cantidad_platillo * platillos[6][2] if platillo == 7 else cantidad_platillo * platillos[7][2] if platillo == 8 else cantidad_platillo * platillos[8][2] if platillo == 9 else cantidad_platillo * platillos[9][2] if platillo == 10 else 0
    #se usa la variable nueva de los parametros, para guardar el total de lo que se lleva acumulado en cantidad de platillo
    costoTotal=cantidadPlatilloTotal * platillos[0][2] if platillo == 1 else cantidadPlatilloTotal * platillos[1][2] if platillo == 2 else cantidadPlatilloTotal * platillos[2][2] if platillo == 3 else cantidadPlatilloTotal * platillos[3][2] if platillo == 4 else cantidadPlatilloTotal * platillos[4][2] if platillo == 5 else cantidadPlatilloTotal * platillos[5][2] if platillo == 6 else cantidadPlatilloTotal * platillos[6][2] if platillo == 7 else cantidadPlatilloTotal * platillos[7][2] if platillo == 8 else cantidadPlatilloTotal * platillos[8][2] if platillo == 9 else cantidadPlatilloTotal * platillos[9][2] if platillo == 10 else 0
    subtotal = 0
    subtotal += costo
    return costoTotal, subtotal

