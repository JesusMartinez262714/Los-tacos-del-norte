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
        if entrada.isdigit():  # Validamos que sea un número
            return int(entrada)  # Retorna el valor numérico como entero
        else:
            print("Entrada no válida. Ingrese un número.")


def comandas_abiertas(comandas:dict):
    #formateo y hacer que se muestre al registrar una comanda
    contador=0
    print("Comandas Abiertas:")
    print(f"{"":-^65}")
    print(f"{"Mesa":<9}{"Cliente":<16}{"Empleado":<17}Total ($)")
    print(f"{"":-^65}")
    for folio,datos in comandas.items():
        if datos["estado"] == "No pagada":
            print(f"{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
            contador+=1
    print(f"{"":-^65}")
    print(f"Total de Comandas Abiertas: {contador}")



def mostrar_resumen(comandas,folio):
    if folio in comandas:
        print(f"{"":=^45}")
        print(f"{"Los tacos del norte":^45}")
        print(f"{"":=^45}")
        print(f"Comanda #{folio:<18}Fecha: {fechaHoy}")
        print(f"Mesa: {comandas[folio]['mesa']:<21}Cliente: {comandas[folio]['cliente']}")
        print(f"Empleado: {comandas[folio]['empleado']:<27}")
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
        platillo="Tacos de Asada"
    if platillo==2:
        platillo="Tacos de Pastor"
    if platillo==3:
        platillo="Quesadilla"
    if platillo==4:
        platillo="Refresco"
    if platillo==5:
        platillo="Burrito de Asada"
    if platillo==6:
        platillo="Burrito de Pastor"
    if platillo==7:
        platillo="Torta de Asada"
    if platillo==8:
        platillo="Torta de Pastor"
    if platillo==9:
        platillo="Agua Fresca (1L)"
    if platillo==10:
        platillo="Flautas (3 piezas)"
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
    comandas_abiertas(comandas)
    verificar = validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
    folio = obtener_folio_por_mesa(comandas, verificar)
    for datos in comandas.values():
        if verificar == datos['mesa'] and datos['estado'] == "No pagada":
            mostrar_resumen(comandas, folio)
            break
    else:
        print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
        return
    return folio

