"""
Desarrolladores: Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:Mostrar las comandas abiertas

Descripción general:
Este código gestiona la visualización de las comandas abiertas (no pagadas) en el sistema. Permite mostrar información relevante 
como el número de mesa, cliente, empleado y el total de cada comanda, filtrando las comandas abiertas por empleado si es necesario.
"""

def comandas_abiertas(comandas:dict,nombre_empleado:str):
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
    comandas_abiertas = True  # Variable para saber si hay comandas abiertas
    
    # Creamos un diccionario donde se ordena por mesas de menor a mayor
    ordenado_por_mesa = (
        dict(sorted(comandas.items(), key=lambda x: x[1]['mesa']))
        if comandas else {}
    )
    for folio, datos in ordenado_por_mesa.items():
        if datos["estado"] == "no pagada" and nombre_empleado == "" or datos['empleado'] == nombre_empleado:  # Solo mostramos las que no han sido pagadas
            if contador == 0:
                print("Comandas Abiertas:")
                print(f"{'':-^65}")
                print(f"{'Mesa':<9}{'Cliente':<16}{'Empleado':<17}Total ($)")
                print(f"{'':-^65}")
                comandas_abiertas=False
            print(f"{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
            contador += 1

    
    # Si no hay comandas abiertas, mostramos solo el mensaje sin ningún formato adicional
    if comandas_abiertas:
        print("No hay comandas abiertas")
        return comandas_abiertas
    else:
        print(f"{'':-^65}")
        print(f"Total de Comandas Abiertas: {contador}")
        return not comandas_abiertas

    
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
            4:{
                "mesa": 1,
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
            5:{
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
            },
            2:{
                "mesa": 2,
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
            }

        }
            comandas_abiertas(comandas,nombre_empleado=None)