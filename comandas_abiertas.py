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

    print("https://prod.liveshare.vsengsaas.visualstudio.com/join?1CF4344DE9B55A6E601BC5ACF3813FA16833")