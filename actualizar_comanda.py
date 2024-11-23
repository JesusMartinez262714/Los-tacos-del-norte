"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo: Actualización de productos en una comanda en el sistema.
"""
import utilerias as u

# Función para verificar si existe una comanda abierta para la mesa proporcionada
def verificar_comanda(comandas: dict, platillos: tuple):
    """
    Verifica si una comanda está abierta para la mesa especificada.

    Parámetros:
    - comandas (dict): Diccionario con las comandas abiertas.
    - platillos (tuple): Tupla que contiene los platillos disponibles.

    Llama a la función para mostrar las comandas abiertas y luego solicita el número de la mesa donde se desea hacer la actualización.
    Si la mesa tiene una comanda abierta y no ha sido pagada, muestra el resumen de la comanda y el menú de actualizaciones.
    """
    u.comandas_abiertas(comandas)  # Llama a la función para verificar las comandas abiertas
    verificar = u.validar_numerico("Ingrese el número de la mesa donde se desea hacer la actualización: ")  # Solicita el número de mesa
    for datos in comandas.values():  # Itera sobre las comandas abiertas
        if verificar == datos['mesa'] and datos['estado'] == "No pagada":  # Verifica que la mesa esté abierta y no pagada
            u.mostrar_resumen(comandas, verificar)  # Muestra el resumen de la comanda
            menu_actualizaciones(platillos, verificar, comandas)  # Muestra el menú de actualizaciones
            break
    else:
        print("No hay ninguna comanda abierta para esta mesa. Intente de nuevo.")  # Si no se encuentra la mesa
        return 

# Función para validar el platillo y la cantidad a agregar
def platillo_valido():
    """
    Solicita al usuario la selección de un platillo y su cantidad.

    Retorna:
    - platillo (int): ID del platillo seleccionado.
    - cantidad (int): Cantidad del platillo seleccionada.
    """
    while True:
        platillo = u.validar_numerico("Ingrese el producto que desea agregar: ")  # Solicita el ID del platillo
        platillo_valido = False
        for posicion in platillos:  # Itera sobre las tuplas de platillos
            if platillo == posicion[0]:  # Si el ID del platillo coincide
                platillo_valido = True
                break
        
        if not platillo_valido:  # Si el platillo no es válido
            print("Opción no válida. Seleccione un platillo del menú.")
            continue  # Vuelve a solicitar la selección

        while True:
            cantidad = u.validar_numerico("Ingrese la cantidad que desea agregar: ")  # Solicita la cantidad de platillos

            if cantidad > 0:  # Si la cantidad es válida
                break
            else:
                print("La cantidad debe ser mayor a 0. Intente de nuevo.")  # Si la cantidad no es válida

        return platillo, cantidad  # Devuelve el ID del platillo y la cantidad
    



# Función para agregar un producto a la comanda
def agregar_producto(platillos, verificar, comandas):
    """
    Agrega un producto a una comanda existente.

    Parámetros:
    - platillos (tuple): Tupla con los platillos disponibles.
    - verificar (int): Número de la mesa de la comanda a actualizar.
    - comandas (dict): Diccionario con las comandas abiertas.

    Realiza la actualización en la comanda, ya sea agregando un producto nuevo o actualizando la cantidad de un platillo existente.
    """
    print("Agregar producto")
    u.imprimirPlatillos()  # Imprime el menú de platillos
    
    platillo, cantidad = platillo_valido()  # Obtiene el platillo y la cantidad seleccionada

    for datos in comandas.values():  # Itera sobre las comandas abiertas
        if verificar == datos['mesa']:  # Verifica si la comanda existe
            platillo_encontrado = False
            # Busca si el platillo ya está en la comanda
            for i in range(len(datos["platillos"])):
                # Cálculo del subtotal basado en el platillo seleccionado
                subtotal = cantidad * platillos[0][2] if platillo == 1 else cantidad * platillos[1][2] if platillo == 2 else cantidad * platillos[2][2] if platillo == 3 else cantidad* platillos[3][2] if platillo == 4 else cantidad * platillos[4][2] if platillo == 5 else cantidad * platillos[5][2] if platillo == 6 else cantidad * platillos[6][2] if platillo == 7 else cantidad * platillos[7][2] if platillo == 8 else cantidad * platillos[8][2] if platillo == 9 else cantidad * platillos[9][2] if platillo == 10 else 0
                
                platillo = u.validar_mismo_platillo(platillo)  # Valida si el platillo existe en el sistema

                if platillo == datos["platillos"][i][0]:  # Si se encuentra el platillo
                    # Si el platillo ya existe, se actualiza su cantidad y subtotal
                    datos["platillos"][i] = (datos["platillos"][i][0], datos["platillos"][i][1] + cantidad, datos["platillos"][i][2] + subtotal)
                    for buscar in comandas[folio]['platillos']:
                        if buscar == platillo:
                            comandas[folio]['platillos'][buscar] = datos["platillos"][i]  # Actualiza el platillo en la comanda
                    u.calcular_total(folio, comandas)  # Recalcula el total de la comanda
                    u.mostrar_resumen(comandas, folio)  # Muestra el resumen actualizado de la comanda
                    print("Producto agregado exitosamente.")
                    platillo_encontrado = True
                    break  # Sale del ciclo si se actualizó el platillo

            if not platillo_encontrado:  # Si el platillo no fue encontrado
                # Si el platillo no existe, se agrega como un nuevo producto
                for posicion in platillos:
                    if platillo == posicion[0]:  # Busca el platillo en el menú
                        datos["platillos"].append((posicion[1], cantidad, posicion[2]))  # Agrega el platillo nuevo
                        print("Nuevo producto agregado exitosamente.")
                        verificar = u.obtener_folio_por_mesa(comandas, verificar)  # Obtiene el folio actualizado
                        u.mostrar_resumen(comandas, verificar)  # Muestra el resumen actualizado
                        break
            break  # Sale del ciclo de las comandas

        return  # Finaliza la función de agregar producto


def eliminar_producto():
    """
    Función para eliminar un producto de la comanda.

    
    """
    print("Eliminar producto")


def aumentar_cantidad():
    """
    Función placeholder para aumentar la cantidad de un producto en la comanda.

   
    """
    print("Aumentar cantidad de producto")

# Función que muestra el menú de actualizaciones
def menu_actualizaciones(platillos, verificar, comandas):
    """
    Muestra el menú con las opciones para actualizar la comanda.

    Parámetros:
    - platillos (tuple): Tupla con los platillos disponibles.
    - verificar (int): Número de la mesa de la comanda a actualizar.
    - comandas (dict): Diccionario con las comandas abiertas.

    Permite al usuario elegir entre agregar un producto, eliminar uno o aumentar la cantidad de un producto.
    """
    print("¿Qué actualización desea realizar? ")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Aumentar cantidad de producto")
    print("4.- Regresar al menú principal")
    opcion = u.validar_numerico('Ingrese una opción: ')  # Solicita la opción de actualización
    
    if opcion == 4:  # Si la opción es 4, regresa al menú principal
        return
    elif opcion == 1:  # Si la opción es 1, agrega un producto
        agregar_producto(platillos, verificar, comandas)
    elif opcion == 2:  # Si la opción es 2, elimina un producto
        eliminar_producto()
    elif opcion == 3:  # Si la opción es 3, aumenta la cantidad de un producto
        aumentar_cantidad()

# Bloque principal de ejecución
if __name__ == "__main__":
    """
    Ejemplo de inicialización de estructuras
    """
    # Comandas abiertas
    comandas = {
        1: {  # Comanda con ID 1
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
        2: {  # Comanda con ID 2
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
        3: {  # Comanda con ID 3
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

    # Lista de platillos disponibles con su ID, nombre y precio
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
    verificar_comanda(comandas, platillos)
