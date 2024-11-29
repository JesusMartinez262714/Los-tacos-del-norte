cantidades = []

def consultar_platillos_mas_vendidos(comandas, platillos):
    for folio, datos in comandas.items():
        if datos["estado"] == "pagada":  # Solo procesar comandas pagadas
            for platillo in datos['platillos']:
                agregar_o_actualizar(platillo[0], platillo[1], platillos)  # Sumar directamente
        else:
            print("No se han registrado ventas de platillos en comandas no pagadas.")

    # Ordenar los 3 platillos más vendidos
    top = sorted(cantidades, key=lambda x: x[1], reverse=True)[:3]

    # Imprimir resultados
    print(f"{'':^6}{' Platillos Más Vendidos ':-^42}")
    print(f"{'Platillo':<20}{'Cantidad Vendida':<20}Ingreso Generado")
    print(f"{'':-^56}")

    rango = min(len(top), 3)  # Ajustar rango si hay menos de 3 platillos
    for dentro in range(rango):
        print(f"{top[dentro][0]:<20}{top[dentro][1]:<20}{top[dentro][2]:.2f}")
    print(f"{'':-^56}")

    # Calcular total de ingresos generados
    total_ingresos = sum(x[2] for x in top)
    print(f"{'Total de Ingresos:':<40}{total_ingresos:.2f}")


def agregar_o_actualizar(platillo, cantidad, platillos):
    # Buscar si el platillo ya está en la lista
    for i in range(len(cantidades)):
        if cantidades[i][0] == platillo:
            # Encontrar el precio unitario del platillo
            precio_unitario = 0
            for item in platillos:
                if item[1] == platillo:
                    precio_unitario = item[2]
                    break
            
            # Actualizar la cantidad y el costo total
            nueva_cantidad = cantidades[i][1] + cantidad
            nuevo_costo = nueva_cantidad * precio_unitario
            cantidades[i] = (platillo, nueva_cantidad, nuevo_costo)
            return

    # Si no está en la lista, agregar un nuevo registro
    precio_unitario = 0
    for item in platillos:
        if item[1] == platillo:
            precio_unitario = item[2]
            break

    nuevo_costo = cantidad * precio_unitario
    cantidades.append((platillo, cantidad, nuevo_costo))


# Ejecución
if __name__ == "__main__":
    comandas = {
        1: {
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        2: {
            "mesa": 4,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
        },
        3: {
            "mesa": 5,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "pagada"
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

    consultar_platillos_mas_vendidos(comandas, platillos)
