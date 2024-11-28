import comandas_abiertas as ca

def fecha():
    """
    Se obtiene a fecha del dia.
    """
    from datetime import datetime #Usando el modulo datetime
    fechaActual = datetime.now()
    fechaFormateada = fechaActual.strftime("%Y-%m-%d")#.strftime nos permite el escribir la fecha en el formato que se desee
    return fechaFormateada#Regresamos como valor el mensaje formateado
fechaHoy=fecha()#Se obetiene el valor del mensaje para la variable local

def imprimirPlatillos():
    """
    Muestra el menú de platillos disponibles, incluyendo sus precios.
    """
    #formateo
    print("Menu platillos: ")
    print(f"{"":-^24}")
    print("1.-Tacos de asada - $20")
    print("2.-Tacos de pastor - $18")
    print("3.-Quesadillas -  $25")
    print("4.-Refresco - $15")
    print("5.-Burrito de Asada - $40")
    print("6.-Burrito de Pastor - $38")
    print("7.-Torta de Asada -  $45")
    print("8.-Torta de Pastor - $43")
    print("9.-Agua Fresca (1L) -  $20")
    print("10.-Flautas (3 piezas) - $30")

def id_por_nombre_platillo(platillos,nombre_producto):
    id_producto = None  # Inicializamos el ID como None
    for platillo in platillos:
        if platillo[1] == nombre_producto:  # Compara el nombre del platillo
            id_producto = platillo[0]  # Guarda el ID del platillo
            return id_producto

def validar_numerico(mensaje: str) -> int:
    """
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
    if folio in comandas:
        print (f"Comanda {folio} Actualizada:" if imprimir=="actualizar" else "Resumen de la comanda {folio}:")
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
    for folio, datos in comandas.items():
        if datos['mesa'] == numero_mesa:
            return folio  # Si encuentra la mesa, retorna el folio
    return None

def validar_mismo_platillo(platillo):
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

def verificar_comanda(comandas:dict, platillos:tuple):
    """
    Verifica si una comanda está abierta para la mesa especificada.

    Parámetros:
    - comandas dict: Diccionario con las comandas abiertas.
    - platillos Tuple: Tupla que contiene los platillos disponibles.

    Retorna:
     El folio de la comanda si se encuentra, o None si no existe una comanda abierta para la mesa.
    """
    ca.comandas_abiertas(comandas)
    verificar = validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
    folio = obtener_folio_por_mesa(comandas, verificar)
    for datos in comandas.values():
        if verificar == datos['mesa'] and datos['estado'] == "No pagada":
            mostrar_resumen(comandas, folio,imprimir="")
            break
        else:
            print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
            return
    return folio

def validar_empleado(empleados):
    """
    Valida si un empleado se encuentra registrado en el sistema.

    Parámetros:
    - empleados (dict): Diccionario con los IDs de los empleados.

    Retorna:
    - int: ID del empleado válido.
    """
    while True:
        empleado = validar_numerico("Ingrese el id del empleado: ")
        if empleado == -1:
            return
        if empleado in empleados:
            return empleados[empleado]["nombre"],empleado
            
        else:
            print("El empleado no esta registrado,Intente de nuevo.")

def validar_s_n(mensaje):
    while True:
        entrada = input(mensaje).strip().lower()  # Obtener la entrada y convertirla a minúsculas
        if entrada == 's' or entrada == 'n':  # Verificar si la entrada es 's' o 'n'
            return entrada  # Retorna 's' o 'n' como respuesta válida
        else:
            print("Entrada no válida. Por favor ingrese 's' o 'n'.")  # Mensaje si la entrada es incorrecta

