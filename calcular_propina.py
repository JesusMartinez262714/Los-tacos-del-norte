import utilerias as u
from typing import Dict, Tuple, List

def calcular_propina(comandas: Dict, empleados: Dict, ) -> None:
    """
    Calcula y muestra las propinas acumuladas por un empleado, el número de comandas asociadas
    y la mesa con la mayor cantidad de propinas.

    Datos de entrada:
    - comandas (Dict): Contiene información de las comandas (mesa, cliente, empleado, platillos, total, propina y estado).
    - empleados (Dict): Contiene información de los empleados (nombre, teléfono y estado).
    - propinas_empleados (Dict): Mapeo de IDs de empleados con la cantidad acumulada de propinas.

    Proceso:
    1. Validar al empleado ingresado utilizando la función `validar_empleado`.
    2. Iterar sobre las comandas para identificar aquellas que estén "pagadas" y sean del empleado seleccionado.
    3. Acumular propinas del empleado y calcular la mesa con la mayor cantidad de propinas.
    4. Mostrar el resumen de propinas acumuladas y comandas asociadas.
    5. Permitir calcular propinas para otro empleado si el usuario lo desea.

    Salida:
    - Imprime el resumen de propinas acumuladas y la mesa con mayor cantidad de propinas.
    - En caso de no haber comandas pagadas, informa al usuario.

    Argumentos:
    - comandas: Diccionario con los datos de las comandas.
    - empleados: Diccionario con los datos de los empleados.
    - propinas_empleados: Diccionario con las propinas acumuladas de cada empleado.

    Retorno:
    - None
    """
    while True:
        propinaAcumulada = 0.0  # Inicializar acumulador de propinas
        comandaAsociada = 0
        hay_comandas_pagadas = False  # Indica si hay comandas pagadas
        empleado, id = u.validar_empleado(empleados)  # Validar empleado
        listaMesasPropina = []
        propinaMesa = 0

        for folio, datos in comandas.items():
            if datos["estado"] == "pagada":  # Validar solo comandas pagadas
                hay_comandas_pagadas = True
                if empleado == datos["empleado"]:
                    comandaAsociada += 1
                    propinaAcumulada += datos["propina"]
                    propinaMesa = datos['propina']
                    for i in listaMesasPropina:
                        if datos['mesa'] == i[0]:
                            propinaMesa += datos['propina']
                            listaMesasPropina.remove(i)
                    listaMesasPropina.append((datos['mesa'], propinaMesa))

        if not hay_comandas_pagadas:
            print("No hay comandas pagadas registradas en el sistema")
            return  # Salir si no hay comandas pagadas

        mesa = sorted(listaMesasPropina, key=lambda x: x[1], reverse=True)
        masPropina = mesa[0][0]  # Mesa con mayor propina

        # Mostrar resultados
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
        
        # Preguntar si desea calcular para otro empleado
        continuar = u.validar_s_n("Desea calcular las propinas de otro empleado (s/n)").lower()
        if continuar == 's':
            continue
        elif continuar == 'n':
            return

if __name__ == "__main__":
    comandas = {
        1: {
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 10,
            "estado": "pagada"  # Pueden ser pagadas o no pagadas
        },
        2: {     
            "mesa": 3,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 10,
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
            "propina": 10,
            "estado": "pagada"
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

    calcular_propina(comandas, empleados)
