import utilerias as u
def imprimirPlatillos(platillos,es_menu):
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
    while True:
      print(f"{" Menú de Platillos Disponibles ":-^45}")
      print(f"{"ID":<6}{"Platillo":<20}Precio ($)")
      print(f"{"":-^45}")
      contador=1
      for i in platillos:
        print(f"{contador:<6}{i[1]:<20}${i[2]}")
        contador+=1
      print(f"{"":-^45}")

      # Si se está llamando desde el módulo 'menu', hacer la pregunta adicional
      if es_menu:
          respuesta=u.validar_s_n("¿Desea volver al menú principal? (s/n):")
          if respuesta=='s':
              return
          elif respuesta=='n':
              continue


if __name__ == "__main__":
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
  imprimirPlatillos(platillos,es_menu=True)