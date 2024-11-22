"""
Desarrolladores:Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:

"""

import utilerias as u
def verificar_comanda(comandas:dict,platillos:tuple):
    u.comandas_abiertas(comandas)
    verificar = u.validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
    for datos in comandas.values():
        if verificar == datos['mesa'] and datos['estado']=="No pagada":
            u.mostrar_resumen(comandas,verificar)
            menu_actualizaciones(platillos,verificar)
            break
    else:
        print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
        return 
    
def agregar_producto(platillos, verificar):
    print("Agregar producto")
    u.imprimirPlatillos()
    
    while True:
        platillo = u.validar_numerico("Ingrese el producto que desea agregar: ")
        
        # Verificar que el platillo sea válido
        platillo_valido = False
        for p in platillos:
            if platillo == p[0]:  # Comparar con el ID del platillo
                platillo_valido = True
                break
        
        if not platillo_valido:
            print("Opción no válida. Seleccione un platillo del menú.")
            continue  # Sigue con la siguiente iteración del bucle principal
        
        while True:
            cantidad = u.validar_numerico("Ingrese la cantidad que desea agregar: ")
            
            # Verificar que la cantidad sea válida
            if cantidad > 0:
                break  # Si la cantidad es válida, salimos del bucle de cantidad
            else:
                print("La cantidad debe ser mayor a 0. Intente de nuevo.")
    
        for datos in comandas.values():
            if verificar == datos['mesa']:
                # Buscar el platillo en la lista de platillos de la comanda
                platillo_encontrado = False
                for i in range(len(datos["platillos"])):
                    if platillo == datos["platillos"][i][0]:  # Si el nombre del platillo coincide
                        # Crear una nueva tupla con la cantidad actualizada
                        datos["platillos"][i] = (datos["platillos"][i][0], datos["platillos"][i][1] + cantidad, datos["platillos"][i][2])
                        print("Producto agregado exitosamente")
                        platillo_encontrado = True
                        break  # Terminar el bucle si se actualizó la cantidad
                
                if not platillo_encontrado:
                    # Si no se encontró el platillo, lo agregamos como nuevo
                    for p in platillos:
                        if platillo == p[0]:  # Encontrar el platillo en el menú
                            datos["platillos"].append((p[1], cantidad, p[2]))  # Agregarlo a la lista
                            print("Nuevo producto agregado exitosamente")
                            break
                break  # Terminar el bucle si se ha actualizado o agregado el platillo

        u.mostrar_resumen(comandas,verificar)
        return

                
      


def eliminar_producto():
    print("Eliminar producto")

def aumentar_cantidad():
    print("Aumentar cantidad de producto")

def menu_actualizaciones(platillos,verificar):
    print("Que actualizacion desea realizar: ")
    print("1.-Agregar producto")
    print("2.-Eliminar producto")
    print("3.-Aumentar cantidad de producto")
    print("4.-Regresar al menu principal")
    opcion=u.validar_numerico('Ingrese una opcion: ')
    if opcion==4:
        return
    elif opcion==1:
        agregar_producto(platillos,verificar)

    elif opcion==2:
        eliminar_producto()

    elif opcion==3:
        aumentar_cantidad()


       

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
    },
    2:{
        "mesa": 2,
        "cliente": "Juan Pérezza",
        "empleado": "María López",
        "platillos": [
            ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
            ("Refresco", 2, 30.00)
        ],
        "total": 90.00,
        "propina":0,
        "estado" : "No pagada" #Pueden ser pagadas o no pagadas
    },
    3:{
        "mesa": 1,
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

    agregar_producto(comandas,platillos)