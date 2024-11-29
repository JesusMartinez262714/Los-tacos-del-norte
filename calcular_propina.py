import utilerias as u

def calcular_propina(comandas,empleados):
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
            print(f"{" Calculo de Propinas ":-^27}")
            print("")
            print(f"Empleado: {empleado}")
            print("")
            print(f"Propinas acumuladas: ${propinaAcumulada}")
            print("")
            print(f"Comandas asociadas: {comandaAsociada}")
            print("")
            print(f'La mesa con mayor cantidad de propinas es la {masPropina}.')
            print("")
        else:
            print(f"{" Calculo de Propinas ":-^27}")
            print(f"Empleado: {empleado}")
            print("Propinas acumuladas: $0.00")
            print("Comandas asociadas: 0")
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