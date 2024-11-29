import utilerias as u
from typing import Dict, Tuple

def cerrar_comanda(
    comandas: Dict, 
    platillos: Tuple, 
    mesas: Dict
) -> None:
    """
    Permite cerrar una comanda, registrar la propina, generar un ticket y actualizar el estado de la mesa.

    Datos de entrada:
    - comandas (Dict): Información de las comandas (mesa, cliente, empleado, platillos, total, estado y propina).
    - platillos (Tuple): Lista de platillos disponibles con su precio.
    - mesas (Dict): Estado de disponibilidad de las mesas.

    Proceso:
    1. Verificar el folio de la comanda con la función `verificar_comanda`.
    2. Preguntar al usuario si desea cerrar la comanda.
    3. Registrar la propina ingresada, generar el ticket y actualizar el estado de la comanda y la mesa.
    4. Preguntar si desea cerrar otra comanda y repetir el proceso si es necesario.

    Salida:
    - Imprime el ticket de la comanda cerrada.
    - Actualiza el estado de la comanda y la mesa correspondiente.

    Argumentos:
    - comandas: Diccionario con los datos de las comandas.
    - platillos: Tupla con los platillos disponibles.
    - mesas: Diccionario con el estado de las mesas.

    Retorno:
    - None
    """
    while True:
        folio = u.verificar_comanda(comandas)  # Verificar folio de comanda
        cerrar = input("Desea cerrar esta comanda? (s/n)").lower()
        if cerrar == 'n':
            print('Cierre de comanda cancelado')
            return
        else:
            while True:
                propina = u.validar_numerico("Ingrese la propina que desea dejar: ")
                if propina >= 0:
                    generar_ticket(folio, comandas, propina)
                    actualizar_estado_comanda(folio, comandas, mesas, propina)
                    break
                else:
                    print("La propina no puede ser negativa, intente nuevamente")
                    continue
            continuar = u.validar_s_n("Desea cerrar otra comanda y generar su cuenta? (s/n)").lower()
            if continuar == 's':
                continue
            if continuar == 'n':
                return

def generar_ticket(
    folio: int, 
    comandas: Dict, 
    propina: float
) -> None:
    """
    Genera e imprime el ticket de la comanda cerrada.

    Datos de entrada:
    - folio (int): Folio de la comanda.
    - comandas (Dict): Información de las comandas.
    - propina (float): Porcentaje de propina aplicado.

    Proceso:
    1. Verificar que el folio exista en las comandas.
    2. Calcular el subtotal, propina y total de la cuenta.
    3. Imprimir el ticket con el formato establecido.

    Salida:
    - Imprime el ticket con la información de la comanda.

    Argumentos:
    - folio: ID único de la comanda.
    - comandas: Diccionario con los datos de las comandas.
    - propina: Porcentaje de propina proporcionado.

    Retorno:
    - None
    """
    if folio in comandas:
        print(f"{"":=^45}")
        print(f"{"Los tacos del norte":^45}")
        print(f"{"":=^45}")
        print(f"Comanda #{folio:<18}Fecha: {u.fecha()}")
        print(f"Mesa: {comandas[folio]['mesa']:<21}Cliente: {comandas[folio]['cliente']}")
        print(f"Empleado: {comandas[folio]['empleado']:<27}")
        print(f"{"":-^45}")
        print(f"{"Platillo":<20}{"Cant.":<9}{"P.Unit":<10}Total")
        print(f"{"":-^45}")
        acumulador = 0
        for platillo in comandas[folio]['platillos']:
            nombre = platillo[0]
            cantidad = platillo[1]
            subtotal = platillo[2]
            print(f"{nombre:<20}{cantidad:<9}{subtotal/cantidad:<10}{subtotal}")
            acumulador += subtotal
        print(f"{"":-^45}")
        print(f"{"Subtotal":<39}{acumulador}")
        print(f"{"Propina":<39}{acumulador * (propina / 100)}")
        print(f"{"":-^45}")
        print(f"{"Total":<39}{acumulador + (acumulador * (propina / 100))}")
        print(f"{"":=^45}")
        print(f"{"¡Gracias por su preferencia!":^45}")
        print(f"{"":=^45}")

def actualizar_estado_comanda(
    folio: int, 
    comandas: Dict, 
    mesas: Dict, 
    propina: float
) -> None:
    """
    Actualiza el estado de una comanda a "pagada" y asigna la propina.

    Datos de entrada:
    - folio (int): Folio de la comanda.
    - comandas (Dict): Información de las comandas.
    - mesas (Dict): Estado de disponibilidad de las mesas.
    - propina (float): Porcentaje de propina aplicado.

    Proceso:
    1. Cambiar el estado de la comanda a "pagada".
    2. Registrar la propina ingresada.
    3. Actualizar la disponibilidad de la mesa.

    Salida:
    - Actualiza los valores de la comanda y la mesa.

    Argumentos:
    - folio: ID único de la comanda.
    - comandas: Diccionario con los datos de las comandas.
    - mesas: Diccionario con el estado de las mesas.
    - propina: Porcentaje de propina.

    Retorno:
    - None
    """
    comanda = comandas.get(folio)  # Obtener comanda por folio
    if comanda:
        comanda['estado'] = "pagada"
        comanda['propina'] = propina
        disponibilidad_mesas(comandas, mesas, folio)

def disponibilidad_mesas(
    comandas: Dict, 
    mesas: Dict, 
    folio: int
) -> None:
    """
    Actualiza la disponibilidad de una mesa dependiendo del estado de la comanda.

    Datos de entrada:
    - comandas (Dict): Información de las comandas.
    - mesas (Dict): Estado de las mesas.
    - folio (int): Folio de la comanda.

    Proceso:
    1. Verificar el estado de la comanda.
    2. Cambiar la disponibilidad de la mesa según el estado de la comanda.

    Salida:
    - Actualiza el estado de la mesa en el diccionario.

    Argumentos:
    - comandas: Diccionario con los datos de las comandas.
    - mesas: Diccionario con el estado de las mesas.
    - folio: ID único de la comanda.

    Retorno:
    - None
    """
    comanda = comandas.get(folio)
    num_mesas = comanda['mesa']
    if comanda['estado'] == "pagada":
        mesas[num_mesas] = "Disponible"
    else:
        mesas[num_mesas] = "No disponible"


if __name__ == "__main__":
    comandas = {
    1:{
        "mesa": 3,
        "cliente": "Juan Pérez",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00)
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "No pagada" #Pueden ser pagadas o no pagadas
}

}
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
    cerrar_comanda(comandas,platillos,mesas)