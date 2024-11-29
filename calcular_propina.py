import utilerias as u
"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo: Calcular las propinas acumuladas de un empleado, basándose en las comandas pagadas en el sistema.
"""
def calcular_propina(comandas,empleados):
    """
    Calcula las propinas acumuladas de un empleado, basándose en las comandas pagadas.

    Datos de entrada:
        comandas (dict): Diccionario con las comandas registradas, donde cada clave es un folio y cada valor es un diccionario con los detalles de la comanda.
        empleados (dict): Diccionario con los empleados registrados, donde cada clave es el ID del empleado y cada valor es el nombre del empleado.

    Proceso:
        - Solicita al usuario el empleado para calcular las propinas asociadas.
        - Recorre todas las comandas y, si están pagadas, acumula las propinas correspondientes a las comandas del empleado seleccionado.
        - Muestra la cantidad de propina acumulada y el número de comandas asociadas al empleado.
        - Además, muestra la mesa con la mayor cantidad de propinas acumuladas.

    Salida:
        None

    Argumentos:
        comandas: Diccionario que contiene las comandas registradas, donde las claves son los folios de las comandas y los valores son los detalles de cada una.
        empleados: Diccionario con los empleados registrados, que permite validar el empleado a consultar.
    """
    while True:
        propinaAcumulada = 0.0  # Inicializar fuera del bucle
        comandaAsociada = 0
        hay_comandas_pagadas = False  # Variable para saber si hay comandas pagadas
        empleado, id = u.validar_empleado(empleados)
        listaMesasPropina=[]
        propinaMesa=0
        for folio, datos in comandas.items():
            if datos["estado"] == "pagada":  # Validar solo comandas pagadas
                hay_comandas_pagadas = True  # Hay al menos una comanda pagada
                if empleado == datos["empleado"]:
                    comandaAsociada += 1
                    propinaAcumulada += datos["propina"]
                    propinaMesa=datos['propina']
                    for i in listaMesasPropina:
                        if datos['mesa'] == i[0]:
                            propinaMesa+=datos['propina']
                            listaMesasPropina.remove(i)
                    listaMesasPropina.append((datos['mesa'],propinaMesa))


        if not hay_comandas_pagadas:
            print("No hay comandas pagadas registradas en el sistema")
            return  # Sale de la función si no hay comandas pagadas
        mesa=sorted(listaMesasPropina,key=lambda x:x[1],reverse=True)
        masPropina=mesa[0][0]
        
        # Mostrar resultados después de procesar todas las comandas
        if comandaAsociada > 0:
            print(f"Empleado: {empleado}")
            print(f"Propinas acumuladas: {propinaAcumulada}")
            print(f"Comandas asociadas: {comandaAsociada}")
            print(f'La mesa con mayor cantidad de propinas es la {masPropina}')
        else:
            print(f"Empleado: {empleado}")
            print("Nota: Este empleado no tiene comandas pagadas asociadas.")
        continuar=u.validar_s_n("Desea calcular las propinas de otro empleado (s/n)").lower()
        if continuar=='s':
            continue
        elif continuar=='n':
            return
            
            







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
            "propina":10,
            "estado" : "pagada" #Pueden ser pagadas o no pagadas
        },
        2:{     
                "mesa": 3,
                "cliente": "Juan Pérez",
                "empleado": "María López",
                "platillos": [
                    ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                    ("Refresco", 2, 30.00) 
                ],
                "total": 90.00,
                "propina":10,
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
            "propina":10,
            "estado" : "pagada" #Pueden ser pagadas o no pagadas
        }
    }
     
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
    propinas_empleados = {
        101: 50.00,  # María López
        102: 35.00   # Pedro Martínez
    }
    calcular_propina(comandas,empleados,propinas_empleados)