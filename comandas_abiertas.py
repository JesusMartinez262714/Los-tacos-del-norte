def comandas_abiertas(comandas: dict) -> None:
    """"""
    """
    Muestra en formato tabular las comandas que aún no han sido pagadas.

    Datos de entrada:
    - comandas (dict): Diccionario con la información de las comandas, incluyendo su estado, mesa, cliente, empleado y total.

    Proceso:
    1. Iterar sobre las comandas para identificar aquellas cuyo estado sea "No pagada".
    2. Mostrar las comandas abiertas en formato tabular, incluyendo mesa, cliente, empleado y total.
    3. Contar y mostrar la cantidad total de comandas abiertas.

    Salida:
    - Imprime una tabla con las comandas abiertas y el total de estas.

    Argumentos:
    - comandas: Diccionario que contiene información de cada comanda.

    Retorno:
    - None
    """
    contador = 0  # Contador para las comandas abiertas
    print("Comandas Abiertas:")
    print(f"{'':-^65}")
    print(f"{'Mesa':<9}{'Cliente':<16}{'Empleado':<17}Total ($)")
    print(f"{'':-^65}")
    
    for folio, datos in comandas.items():
        if datos["estado"] == "No pagada":  # Filtrar solo las comandas no pagadas
            print(f"{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
            contador += 1  # Incrementar el contador por cada comanda abierta
    
    print(f"{'':-^65}")
    print(f"Total de Comandas Abiertas: {contador}")

    
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
    comandas_abiertas(comandas)