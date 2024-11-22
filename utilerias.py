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
        print(f"\n{"Resumen de la comanda ":->25}{folio}:")
        print(f"Mesa: {comandas[folio]['mesa']}")
        print(f"Cliente: {comandas[folio]['cliente']}")
        print(f"Empleado: {comandas[folio]['empleado']}")
        print(f"Platillos:{comandas[folio]['platillos']}")
        print(f"Total: ${comandas[folio]['total']}")
