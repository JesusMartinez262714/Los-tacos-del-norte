def comandas_abiertas(comandas:dict):
    """
    Muestra un listado de las comandas abiertas (no pagadas) en el sistema.

    Parámetros:
    - comandas (dict): Diccionario que contiene las comandas registradas, identificadas por su folio.
    
    Proceso:
        - La función recorre todas las comandas en el diccionario y muestra aquellas que están "no pagadas".
        - Muestra información relevante como el número de mesa, cliente, empleado y el total de la comanda.

    Salida:
    - Imprime en pantalla la lista de comandas abiertas con su información.
    - Si no hay comandas abiertas, imprime un mensaje indicando que no hay comandas abiertas.

    Argumentos:
    - comandas: Diccionario que contiene las comandas abiertas y sus respectivos detalles, identificados por el folio.
    """
    
    contador = 0
    comandas_abiertas = False  # Variable para saber si hay comandas abiertas
    
    # Recorremos las comandas para ver si hay alguna abierta
    for folio, datos in comandas.items():
        if datos["estado"] == "no pagada":  # Solo mostramos las que no han sido pagadas
            if contador == 0:
                print("Comandas Abiertas:")
                print(f"{'':-^65}")
                print(f"{'Mesa':<9}{'Cliente':<16}{'Empleado':<17}Total ($)")
                print(f"{'':-^65}")
            print(f"{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
            contador += 1
            comandas_abiertas = True  # Hay al menos una comanda abierta
    
    # Si no hay comandas abiertas, mostramos solo el mensaje sin ningún formato adicional
    if not comandas_abiertas:
        print("No hay comandas abiertas")
    else:
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