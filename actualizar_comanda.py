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
    
def agregar_producto(platillos,verificar):
    print("Agregar producto")
    u.imprimirPlatillos()
    platillo=0
    cantidad=0
    while True:
        platillo = u.validar_numerico("Ingrese el producto que desea agregar: ")
        
        # Verificar que el platillo sea válido
        if platillo not in platillos:
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
                for comidas in datos["platillos"]:
                    if platillo == comidas[0]:  # Si el nombre del platillo coincide
                        comidas = (comidas[0], comidas[1] + cantidad, comidas[2])  # Sumar la cantidad existente
                        print("producto agregado exitosamente")
                        break  # Terminar el bucle si se actualizó la cantidad

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
    verificar_comanda(comandas)