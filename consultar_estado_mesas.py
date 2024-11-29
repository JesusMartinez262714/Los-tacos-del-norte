def consultar_estado_mesas(mesas: dict) -> None:
    """"""
    """
    Consulta y muestra el estado actual de las mesas, indicando cuáles están disponibles y cuáles están ocupadas.

    Datos de entrada:
    - mesas (dict): Diccionario donde las claves son los números de mesa y los valores indican su estado ('Disponible' o 'No disponible').

    Proceso:
    1. Iterar por el diccionario `mesas` para clasificar las mesas como disponibles u ocupadas.
    2. Contar el total de mesas disponibles y no disponibles.
    3. Mostrar los números de mesas disponibles y ocupadas, así como sus totales.
    4. Permitir al usuario regresar al menú principal o repetir la consulta.

    Salida:
    - Imprime el estado actual de las mesas (disponibles y ocupadas) y sus totales.

    Argumentos:
    - mesas: Diccionario con la información del estado de cada mesa.

    Retorno:
    - None
    """
    while True:
        listaDisponibles = []  # Lista para mesas disponibles
        listaNoDisponibles = []  # Lista para mesas no disponibles
        disponibles = 0  # Contador de mesas disponibles
        noDisponible = 0  # Contador de mesas no disponibles

        # Clasificar las mesas según su estado
        for x, y in mesas.items():
            if y == 'Disponible':
                disponibles += 1
                listaDisponibles.append(x)
            elif y == 'No disponible':
                noDisponible += 1
                listaNoDisponibles.append(x)

        # Mostrar el estado de las mesas según los contadores
        if disponibles <= 0:
            print("No hay mesas disponibles en este momento.")
        elif noDisponible <= 0:
            print("No hay mesas ocupadas en este momento.")
        else:
            print(f"{'Estado de las Mesas':-^25}")
            print("Mesas Disponibles: ", end="")
            print(", ".join(map(str, listaDisponibles)))  # Mostrar mesas disponibles separadas por comas
            print("Mesas Ocupadas: ", end="")
            print(", ".join(map(str, listaNoDisponibles)))  # Mostrar mesas ocupadas separadas por comas
            print(f"Total de mesas ocupadas: {noDisponible}")
            print(f"Total de mesas disponibles: {disponibles}")

        # Preguntar al usuario si desea continuar o regresar al menú principal
        continuar = input("¿Desea regresar al menú principal? (s/n): ").lower().strip()
        if continuar == 's':
            return
        elif continuar == 'n':
            continue

if __name__ == "__main__":
 mesas = {
        1: "disponible",
        2: "disponible",
        3: "no disponible",
        4: "disponible",
        5: "disponible",
        6: "disponible",
        7: "disponible",
        8: "disponible",
        9: "disponible",
        10: "disponible",
        11: "disponible",
        12: "disponible",
        13: "disponible",
        14: "disponible",
        15: "disponible"

}
 consultar_estado_mesas(mesas)