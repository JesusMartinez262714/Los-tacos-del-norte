cantidades=[]

def consultar_platillos_mas_vendidos(comandas,platillos):
    cantTacosAsada = 0
    cantTacosPastor = 0
    cantQuesadillas = 0
    cantRefrescos = 0
    cantBurritoAsada = 0
    cantBurritoPastor = 0
    cantTortaAsada = 0
    cantTortaPastor = 0
    cantAguaFresca = 0
    cantFlautas = 0

    for folio,datos in comandas.items():
        if datos["estado"] == "pagada":
            for platillo in datos['platillos']:
                if platillo[0] == "Tacos de Asada":
                    cantTacosAsada += platillo[1]
                    agregar_o_actualizar(platillo[0],cantTacosAsada,platillos)
                if platillo[0] == "Tacos de Pastor":
                    cantTacosPastor += platillo[1]
                    agregar_o_actualizar(platillo[0],cantTacosPastor,platillos)
                if platillo[0] == "Quesadillas":
                    cantQuesadillas += platillo[1]
                    agregar_o_actualizar(platillo[0],cantQuesadillas,platillos)
                if platillo[0] == "Refresco":
                    cantRefrescos += platillo[1]
                    agregar_o_actualizar(platillo[0],cantRefrescos,platillos)
                if platillo[0] == "Burrito de Asada":
                    cantBurritoAsada += platillo[1]
                    agregar_o_actualizar(platillo[0],cantBurritoAsada,platillos)
                if platillo[0] == "Burrito de Pastor":
                    cantBurritoPastor += platillo[1]
                    agregar_o_actualizar(platillo[0],cantBurritoPastor,platillos)
                if platillo[0] == "Torta de Asada":
                    cantTortaAsada += platillo[1]
                    agregar_o_actualizar(platillo[0],cantTortaAsada,platillos)
                if platillo[0] == "Torta de Pastor":
                    cantTortaPastor += platillo[1]
                    agregar_o_actualizar(platillo[0],cantTortaPastor,platillos)
                if platillo[0] == "Agua Fresca (1L)":
                    cantAguaFresca += platillo[1]
                    agregar_o_actualizar(platillo[0],cantAguaFresca,platillos)
                if platillo[0] == "Flautas (3 piezas)":
                    cantFlautas += platillo[1]
                    agregar_o_actualizar(platillo[0],cantFlautas,platillos)
        else:
            print("No se han registrado venta de platillos")
            return
    top=sorted(cantidades,key=lambda x:x[1],reverse=True)[:3]
    print(top)
    totalIngresos=0
    for x in top:
        totalIngresos+=x[2]
    print(totalIngresos)

def agregar_o_actualizar(platillo, cantidad,platillos):
    # Buscar si el platillo ya existe en la lista
    for i in range(len(cantidades)):
        if cantidades[i][0] == platillo:
            # Si existe, actualizar la cantidad
            cant=cantidades[i][1] + cantidad
            for x in platillos:
                cantidades[i] = (platillo,cant,cant*x[2])
            return
    # Si no existe, agregar el platillo como una nueva tupla
    for i in platillos:
        if platillo == i[1]:
            cantidades.append((platillo, cantidad,cantidad*i[2]))






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
        "estado" : "pagada" #Pueden ser pagadas o no pagadas
    },
    2:{     
            "mesa": 4,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00) 
            ],
            "total": 90.00,
            "propina":0,
            "estado" : "pagada" #Pueden ser pagadas o no pagadas
    },
     3:{
        "mesa": 5,
        "cliente": "Juan Pérez",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00) 
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "pagada" #Pueden ser pagadas o no pagadas
}

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


    empleados = {
    101: {
        "nombre": "María López",
        "telefono": "6441234567",
        "estado": "activo"
    },
    102: {
        "nombre": "Pedro Martínez",
        "telefono": "6449876543",
        "estado": "inactivo"
    }
}
    consultar_platillos_mas_vendidos(comandas,platillos)