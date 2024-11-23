"""
Desarrolladores:Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:

"""
import utilerias as u
def validar_mismo_platillo(platillo):
    if platillo==1:
        platillo="Tacos de Asada"
    if platillo==2:
        platillo="Tacos de Pastor"
    if platillo==3:
        platillo="Quesadilla"
    if platillo==4:
        platillo="Refresco"
    if platillo==5:
        platillo="Burrito de Asada"
    if platillo==6:
        platillo="Burrito de Pastor"
    if platillo==7:
        platillo="Torta de Asada"
    if platillo==8:
        platillo="Torta de Pastor"
    if platillo==9:
        platillo="Agua Fresca (1L)"
    if platillo==10:
        platillo="Flautas (3 piezas)"
    return platillo

def verificar_comanda(comandas: dict, platillos: tuple):
    u.comandas_abiertas(comandas)
    verificar = u.validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")
    for datos in comandas.values():
        if verificar == datos['mesa'] and datos['estado'] == "No pagada":
            u.mostrar_resumen(comandas, verificar)
            
            menu_actualizaciones(platillos, verificar,comandas)
            break
    else:
        print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")
        return 


def agregar_producto(platillos, verificar,comandas):
    print("Agregar producto")
    u.imprimirPlatillos()  # Esto parece ser una función que imprime los platillos disponibles
    while True:
        platillo = u.validar_numerico("Ingrese el producto que desea agregar: ")
        
        # Verificar que el platillo sea válido
        platillo_valido = False
        for posicion in platillos:  # Itera sobre las tuplas en platillos
            if platillo == posicion[0]:  # Comparar con el ID del platillo
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
            if verificar == datos['mesa']:  # Verificamos que la mesa sea la correcta
                platillo_encontrado = False
                # Buscar si el platillo ya existe en la comanda
                for i in range(len(datos["platillos"])):
                    platillo=validar_mismo_platillo(platillo)
                    if platillo == datos["platillos"][i][0]:
                        # Comparar por nombre del platillo
                        # Si el platillo existe, actualizar la cantidad
                        datos["platillos"][i] = (datos["platillos"][i][0], datos["platillos"][i][1] + cantidad, datos["platillos"][i][2])
                        print(datos["platillos"][i])
                        print("Producto agregado exitosamente.")
                        platillo_encontrado = True
                        break  # Salir del ciclo, ya que el platillo fue encontrado y actualizado
                
                if not platillo_encontrado:
                    # Si el platillo no se encontró, lo agregamos como nuevo
                    for posicion in platillos:
                        if platillo == posicion[0]:  # Encontrar el platillo en el menú por ID
                            datos["platillos"].append((posicion[1], cantidad, posicion[2]))  # Agregar el nuevo platillo
                            print("Nuevo producto agregado exitosamente.")
                            verificar=u.obtener_folio_por_mesa(comandas,verificar)
                            u.mostrar_resumen(comandas,verificar)
                            break
                break  # Salir del ciclo de las comandas, ya que se actualizó o agregó el producto
        
        # Mostrar resumen actualizado
        
        return  # Regresar al submenú o continuar con el flujo de la aplicación


def eliminar_producto():
    print("Eliminar producto")

def aumentar_cantidad():
    print("Aumentar cantidad de producto")

def menu_actualizaciones(platillos, verificar,comandas):
    print("¿Qué actualización desea realizar? ")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Aumentar cantidad de producto")
    print("4.- Regresar al menú principal")
    opcion = u.validar_numerico('Ingrese una opción: ')
    
    if opcion == 4:
        return
    elif opcion == 1:
        agregar_producto(platillos, verificar,comandas)
    elif opcion == 2:
        eliminar_producto()
    elif opcion == 3:
        aumentar_cantidad()


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
            "propina": 0,
            "estado": "No pagada"  # Pueden ser pagadas o no pagadas
        },
        2: {
            "mesa": 2,
            "cliente": "Juan Pérezza",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "No pagada"  # Pueden ser pagadas o no pagadas
        },
        3: {
            "mesa": 1,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Tacos de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
                ("Refresco", 2, 30.00)
            ],
            "total": 90.00,
            "propina": 0,
            "estado": "No pagada"  # Pueden ser pagadas o no pagadas
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

    # Simulamos el proceso de actualización de una comanda
    agregar_producto(comandas, platillos)
