"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo: Actualización de productos en una comanda en el sistema.
"""
import utilerias as u
import imprimir_platillos as ip

# Función para agregar un producto a la comanda
def agregar_producto(platillos: tuple, comandas: dict, folio: int) -> None:
    """
    Agrega un producto a una comanda existente.

    Datos de entrada:
    - platillos (tuple): Tupla con los platillos disponibles (ID, nombre, precio).
    - comandas (dict): Diccionario con las comandas abiertas (clave: folio, valor: información de la comanda).
    - folio (int): ID de la comanda a actualizar.

    Proceso:
    - Se solicita al usuario el producto que desea agregar y su cantidad.
    - Si el producto existe en el menú, se agrega a la comanda o se actualiza la cantidad si ya existe.
    
    Salida:
    - None: Actualiza la comanda y muestra un resumen actualizado.

    Argumentos:
    - platillos: Tupla de platillos disponibles.
    - comandas: Diccionario de comandas abiertas.
    - folio: ID de la comanda a actualizar.
    """
    print("Agregar producto")
    imprimir="actualizar"
    ip.imprimirPlatillos()
    
    while True:
        platillo = u.validar_numerico("Ingrese el producto que desea agregar: ")
        
        platillo_valido = False
        for posicion in platillos:  # Itera sobre las tuplas en platillos
            if platillo == posicion[0]:  # Comparar con el ID del platillo
                platillo_valido = True
                break
        
        if not platillo_valido:
            print("Opción no válida. Seleccione un platillo del menú.")
            continue
        
        while True:
            cantidad = u.validar_numerico("Ingrese la cantidad que desea agregar: ")
            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0. Intente de nuevo.")

        subtotal = cantidad * platillos[platillo-1][2]
        for comanda in comandas.values():
            comanda = comandas.get(folio)
            datos = comanda
            if comanda:
                platillo_encontrado = False
                for i in range(len(datos['platillos'])):
                    platillo = u.validar_mismo_platillo(platillo)
                    if platillo == datos['platillos'][i][0]:
                        datos['platillos'][i] = (datos['platillos'][i][0], datos['platillos'][i][1] + cantidad, datos['platillos'][i][2] + subtotal)
                        for buscar in comandas[folio]['platillos']:
                            if buscar == platillo:
                                comandas[folio]['platillos'][buscar] = datos['platillos'][i]
                        u.calcular_total(folio, comandas)
                        u.mostrar_resumen(comandas, folio, imprimir="actualizar")
                        print("Producto agregado exitosamente.")
                        platillo_encontrado = True
                        break

                if not platillo_encontrado:
                    for posicion in platillos:
                        if platillo == posicion[1]:
                            datos['platillos'].append((posicion[1], cantidad, cantidad * posicion[2]))
                            print("Nuevo producto agregado exitosamente.")
                            u.mostrar_resumen(comandas, folio, imprimir)
                            break
                break
        menu_actualizaciones(comandas, platillos, es_menu="no")

# Función para eliminar un producto de la comanda
def eliminar_producto(platillos: tuple, comandas: dict, folio: int) -> None:
    """
    Elimina un producto de la comanda seleccionada.

    Datos de entrada:
    - platillos (tuple): Tupla con los platillos disponibles.
    - comandas (dict): Diccionario con las comandas abiertas.
    - folio (int): ID de la comanda a actualizar.

    Proceso:
    - Se muestra la lista de productos en la comanda.
    - El usuario selecciona el producto a eliminar y la cantidad que desea eliminar.

    Salida:
    - None: Actualiza la comanda y muestra el resumen actualizado.

    Argumentos:
    - platillos: Tupla de platillos disponibles.
    - comandas: Diccionario de comandas abiertas.
    - folio: ID de la comanda a actualizar.
    """
    if folio in comandas:
        print(f"\n{"productos de la comanda ":->25}{folio}:")
        contador = 1
        for platillo in comandas[folio]['platillos']:
            print(f"{contador}. {platillo[0]} ({platillo[1]})")
            contador += 1
        
        while True:
            producto = u.validar_numerico("Ingrese el número del producto que desea eliminar: ")
            if 1 <= producto <= len(comandas[folio]['platillos']):
                cant_producto = comandas[folio]['platillos'][producto - 1][1]
                nombre_producto = comandas[folio]['platillos'][producto - 1][0]
                id_producto = u.id_por_nombre_platillo(platillos, nombre_producto)

                print(f"Producto: {nombre_producto}")
                print(f"Cantidad disponible: {cant_producto}")

                cantidad = input(f"Ingrese cuántos {nombre_producto} desea eliminar (o 'todo'): ")
                if cantidad == 'todo':
                    del comandas[folio]['platillos'][producto - 1]
                    print(f"{nombre_producto} ha sido completamente eliminado.")
                elif cantidad.isdigit():
                    cantidad = int(cantidad)
                    if cantidad > cant_producto:
                        print(f"Solo existen {cant_producto} de este producto.")
                    else:
                        continuar = input(f"¿Está seguro de que desea eliminar {cantidad} de {nombre_producto}? (s/n): ").lower()
                        if continuar == 's':
                            nuevo_cant = cant_producto - cantidad
                            if nuevo_cant > 0:
                                comandas[folio]['platillos'][producto - 1] = (nombre_producto, nuevo_cant, nuevo_cant * platillos[id_producto - 1][2])
                                print(f"{cantidad} de {nombre_producto} ha sido eliminado.")
                            else:
                                del comandas[folio]['platillos'][producto - 1]
                                print(f"{nombre_producto} ha sido completamente eliminado.")
                else:
                    print("Entrada no válida. Ingrese un número.")
                
                u.calcular_total(folio, comandas)
                u.mostrar_resumen(comandas, folio, imprimir="actualizar")
                menu_actualizaciones(comandas, platillos, es_menu="no")
            else:
                print("Opción no válida. Seleccione un producto de la lista.")

# Función para aumentar la cantidad de un producto en la comanda
def aumentar_producto(platillos: tuple, comandas: dict, folio: int) -> None:
    """
    Aumenta la cantidad de un producto en la comanda seleccionada.

    Datos de entrada:
    - platillos (tuple): Tupla con los platillos disponibles.
    - comandas (dict): Diccionario con las comandas abiertas.
    - folio (int): ID de la comanda a actualizar.

    Proceso:
    - Muestra los productos en la comanda y permite al usuario agregar más cantidad a un producto seleccionado.

    Salida:
    - None: Actualiza la comanda y muestra el resumen actualizado.

    Argumentos:
    - platillos: Tupla de platillos disponibles.
    - comandas: Diccionario de comandas abiertas.
    - folio: ID de la comanda a actualizar.
    """
    if folio in comandas:
        print(f"\n{"productos de la comanda ":->25}{folio}:")
        contador = 1
        for platillo in comandas[folio]['platillos']:
            print(f"{contador}. {platillo[0]} ({platillo[1]})")
            contador += 1
        
        while True:
            producto = u.validar_numerico("Ingrese el número del producto que desea agregar: ")
            if 1 <= producto <= len(comandas[folio]['platillos']):
                cant_producto = comandas[folio]['platillos'][producto - 1][1]
                nombre_producto = comandas[folio]['platillos'][producto - 1][0]
                id_producto = u.id_por_nombre_platillo(platillos, nombre_producto)

                print(f"Producto: {nombre_producto}")
                print(f"Cantidad disponible: {cant_producto}")

                cantidad = input(f"Ingrese cuántos {nombre_producto} desea agregar: ")
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    if cantidad < 0:
                        print(f"La cantidad debe ser mayor a 0. Intente de nuevo.")
                    else:
                        nuevo_cant = cant_producto + cantidad
                        if nuevo_cant > 0:
                            comandas[folio]['platillos'][producto - 1] = (nombre_producto, nuevo_cant, nuevo_cant * platillos[id_producto - 1][2])
                            print(f"{cantidad} de {nombre_producto} ha sido agregado.")
                        else:
                            del comandas[folio]['platillos'][producto - 1]
                            print(f"{nombre_producto} ha sido completamente eliminado.")
                else:
                    print("Entrada no válida. Ingrese un número.")
                
                u.calcular_total(folio, comandas)
                u.mostrar_resumen(comandas, folio, imprimir="actualizar")
                menu_actualizaciones(comandas, platillos, es_menu="no")
            else:
                print("Opción no válida. Seleccione un producto de la lista.")

# Función que muestra el menú de actualizaciones
def menu_actualizaciones(comandas,platillos,es_menu) -> None:
    """
    Muestra el menú con las opciones para actualizar la comanda.

    Parámetros:
    - platillos Tuple: Tupla con los platillos disponibles.
    - verificar (int): Número de la mesa de la comanda a actualizar.
    - comandas dict: Diccionario con las comandas abiertas.

    Permite elegir entre agregar, eliminar o aumentar la cantidad de un producto.
    """

    folio=u.verificar_comanda(comandas)
    
    print("¿Qué actualización desea realizar? ")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Aumentar cantidad de producto")
    print("4.- Regresar al menú principal")
    opcion = u.validar_numerico('Ingrese una opción: ')
    
    if opcion == 4:
        return
    elif opcion == 1:
        agregar_producto(platillos,comandas,folio)
    elif opcion == 2:
        eliminar_producto(platillos,comandas,folio)
    elif opcion == 3:
        aumentar_producto(platillos,comandas,folio)

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
                ("Refresco", 2, 30.00),
                ("Torta de Asada", 4, 180.00)
            ],
            "total": 270.00,
            "propina": 0,
            "estado": "No pagada"  # Pueden ser pagadas o no pagadas
        },
        3: {  # Comanda con ID 3
            "mesa": 1,
            "cliente": "Juan Pérez",
            "empleado": "María López",
            "platillos": [
                ("Torta de Asada", 3, 60.00),  # (Nombre del platillo, Cantidad, Subtotal)
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
    menu_actualizaciones(comandas,platillos)
