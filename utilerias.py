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
        entrada = input(mensaje)
        if entrada.isdigit():  # Validamos que sea un número
            return int(entrada)  # Retorna el valor numérico como entero
        else:
            print("Entrada no válida. Ingrese un número.")