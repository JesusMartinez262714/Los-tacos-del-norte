import utilerias as u
"""
"""
def imprimirPlatillos(es_menu: bool) -> None:
    """
    Muestra el menú de platillos disponibles, incluyendo sus precios.

    Datos de entrada:
        - es_menu (bool): Indica si se está llamando a esta función desde el módulo de menú.

    Proceso:
        1. Se imprime una lista de platillos junto con sus precios de forma formateada.
        2. Si `es_menu` es True, se pregunta al usuario si desea volver al menú principal, validando la respuesta.

    Salida:
        - Impresión del menú de platillos.
        - Si `es_menu` es True, permite al usuario regresar al menú principal o continuar.

    Argumentos:
        - es_menu (bool): Define si se muestra la opción de regresar al menú principal o no.
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
    # Si se está llamando desde el módulo 'menu', hacer la pregunta adicional
    if es_menu:
      while True:  
        respuesta=u.validar_s_n("¿Desea volver al menú principal? (s/n):")
        if respuesta=='s':
            return
        elif respuesta=='n':
            continue


if __name__ == "__main__":
    imprimirPlatillos(es_menu=True)