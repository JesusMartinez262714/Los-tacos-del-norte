import utilerias as u
def imprimirPlatillos(es_menu):
    """
    Muestra el menú de platillos disponibles, incluyendo sus precios. Si es llamado desde el menú principal, 
    pregunta al usuario si desea regresar o seguir en el menú de platillos.

    Parámetros:
    - es_menu (bool): Indica si la función es llamada desde el menú principal. Si es True, se ofrece la opción
                      de regresar al menú principal después de mostrar el menú de platillos.

    Salida:
    - Imprime el menú de platillos disponibles con sus respectivos precios.
    - Si 'es_menu' es True, después de mostrar el menú de platillos, permite que el usuario decida si quiere regresar
      al menú principal o continuar viendo los platillos.

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