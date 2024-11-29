import utilerias as u
def cerrar_comanda(comandas:dict,platillos,mesas,propinas_empleados,empleados):
    """
    Cierra una comanda registrada, permitiendo al usuario ingresar una propina, generar el ticket y actualizar el estado de la comanda.

    Datos de entrada:
        comandas (dict): Diccionario con las comandas registradas, donde las claves son los folios y los valores son los detalles de cada comanda.
        platillos (tuple): Tupla con los platillos disponibles, que no se utilizan directamente en esta función, pero pueden ser parte de la estructura del sistema.
        mesas (dict): Diccionario con la información sobre las mesas, utilizado para actualizar el estado de las mesas relacionadas con las comandas.

    Proceso:
        - Solicita al usuario la verificación de una comanda existente.
        - Pregunta si desea cerrar la comanda seleccionada.
        - Si el usuario confirma, pide la propina que desea dejar, valida que no sea negativa y luego genera el ticket correspondiente.
        - Actualiza el estado de la comanda y las mesas asociadas.
        - Permite continuar con el cierre de otra comanda o finalizar el proceso.

    Salida:
        None

    Argumentos:
        comandas: Diccionario que contiene las comandas registradas, se usa para identificar la comanda a cerrar y actualizar su estado.
        platillos: Tupla con los platillos disponibles, aunque no se utiliza en esta función, es parte de la estructura general del sistema.
        mesas: Diccionario que contiene la información de las mesas, se utiliza para actualizar su estado una vez que la comanda se cierra.
    """
    while True:
        folio=u.verificar_comanda(comandas)
        cerrar=u.validar_s_n("Desea cerrar esta comanda? (s/n)")
        if cerrar == 'n':
            print('Cierre de comanda cancelado')
            return
        elif cerrar == 's':
            while True:
                propina=u.validar_numerico("Ingrese la propina que desea dejar: ")
                if propina >= 0:
                    generar_ticket(folio,comandas,propina)
                    actualizar_estado_comanda(folio,comandas,mesas,propina)
                    break
                else:
                    print("La propina no puede ser negativa,intente nuevamente")
                    continue
                
                id_empleado=buscar_id_por_nombre(comandas[folio]['empleado'],empleados)
                propinas_empleados[id_empleado]=propinas_empleados[id_empleado]+propina
                print(propinas_empleados)



            continuar=u.validar_s_n("Desea cerrar otra comamda y generar su cuente? (s/n)")
            if continuar=='s':
                continue
            if continuar == 'n':
                return

def generar_ticket(folio,comandas,propina):
    """
    Genera un ticket con los detalles de la comanda, incluyendo la lista de platillos, subtotales, propina y total.

    Datos de entrada:
        folio (int): El número de folio que identifica la comanda a generar el ticket.
        comandas (dict): Diccionario con las comandas registradas. Cada clave es un folio, y su valor es un diccionario con los detalles de la comanda.
        propina (float): La cantidad de propina que el cliente deja en la comanda.

    Proceso:
        - Busca la comanda asociada al folio.
        - Muestra los detalles de la comanda, incluyendo el cliente, el empleado, los platillos, cantidades, subtotales, propina y total.
        - Genera el ticket con una presentación formateada y centrada.
    
    Salida:
        None

    Argumentos:
        folio: El número de folio de la comanda que se desea generar en el ticket.
        comandas: Un diccionario que contiene la información de todas las comandas, incluyendo platillos, mesa, cliente, empleado y más.
        propina: La cantidad de propina que el cliente ha dejado en la comanda, que será sumada al total final.
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
        print(f"{"Subtotal":<39}{acumulador}")
        print(f"{"Propina":<39}{propina}")
        print(f"{"":-^45}")
        print(f"{"Total":<39}{acumulador+propina}")
        print(f"{"":=^45}")
        print(f"{"¡Gracias por su preferencia!":^45}")
        print(f"{"":=^45}")

def actualizar_estado_comanda(folio,comandas,mesas,propina):
    """
    Actualiza el estado de una comanda a "pagada" y asigna una propina a la misma. 

    Parámetros:
    - folio (int): El número de folio que identifica la comanda a actualizar.
    - comandas (dict): Diccionario que contiene las comandas registradas. Cada clave es un folio, y su valor es un diccionario con los detalles de la comanda.
    - mesas (dict): Diccionario que contiene las mesas disponibles en el restaurante.
    - propina (float): La cantidad de propina que el cliente deja en la comanda.

    Proceso:
        - Si la comanda existe, se actualiza su estado a "pagada" y se asigna la propina proporcionada.
        - Luego se llama a la función `disponibilidad_mesas` para liberar la mesa asociada a la comanda.

    Salida:
    - None: La función no retorna un valor, pero realiza las actualizaciones en el diccionario de las comandas y mesas.

    Argumentos:
    - folio: El número de folio de la comanda que se desea actualizar.
    - comandas: Un diccionario con todas las comandas registradas.
    - mesas: Un diccionario con las mesas disponibles, que se actualizará según la comanda pagada.
    - propina: La cantidad de propina que se asigna a la comanda.
    """
    comanda = comandas.get(folio)  # Obtiene la comanda por folio
    if comanda:
        comanda['estado']="pagada"
        comanda['propina']=propina
        disponibilidad_mesas(comandas,mesas,folio)
     
def buscar_id_por_nombre(nombre_buscado,empleados):
    for id_empleado, detalles in empleados.items():
        if detalles["nombre"] == nombre_buscado:
            return id_empleado
    return None



def disponibilidad_mesas(comandas, mesas, folio):
    """
    Actualiza la disponibilidad de una mesa en función del estado de la comanda asociada.

    Parámetros:
    - comandas (dict): Diccionario que contiene las comandas registradas, identificadas por su folio.
    - mesas (dict): Diccionario que contiene el estado de las mesas, donde la clave es el número de la mesa y el valor es su estado ("disponible" o "no disponible").
    - folio (int): El número de folio de la comanda que se desea verificar.

    Proceso:
        - Si la comanda está pagada, la mesa asociada se marca como "disponible".
        - Si la comanda no está pagada, la mesa se marca como "no disponible".

    Salida:
    - None: La función no retorna un valor, pero actualiza el estado de la mesa en el diccionario `mesas`.

    Argumentos:
    - comandas: Diccionario con todas las comandas registradas, identificadas por su folio.
    - mesas: Diccionario que almacena el estado de cada mesa en el restaurante.
    - folio: El número de folio que identifica la comanda asociada a la mesa.
    """
    comanda = comandas.get(folio)
    if comanda:
        num_mesa = comanda['mesa']  # Obtén el número de la mesa
        if comanda['estado'] == "pagada":
            mesas[num_mesa] = "disponible"  # Cambia a "disponible" si la comanda está pagada
        else:
            mesas[num_mesa] = "no disponible"  # De lo contrario, marca como "no disponible"



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