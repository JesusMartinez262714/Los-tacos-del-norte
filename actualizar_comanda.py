"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo: Actualización de productos en una comanda en el sistema.
"""
import utilerias as u
import imprimir_platillos as ip

def folioGlobal(folio):
    return folio
folioNuevo=0
# Función para verificar si existe una comanda abierta para la mesa proporcionada



# Función para agregar un producto a la comanda
def agregar_producto(platillos, comandas:dict,folio):
    """
    Agrega un producto a una comanda existente.

    Datos de entrada:
        platillos (tuple): Tupla con los platillos disponibles, donde cada platillo es una tupla con su ID, nombre y precio.
        comandas (dict): Diccionario con las comandas abiertas, donde cada clave es el folio de la comanda y cada valor es un diccionario con los datos de la comanda.
        folio (int): El folio de la comanda en la que se desea agregar el producto.

    Proceso:
        - Muestra un menú para seleccionar un platillo disponible.
        - Valida si el platillo existe y si la cantidad es válida.
        - Si el platillo ya está en la comanda, actualiza su cantidad y subtotal.
        - Si el platillo no está en la comanda, lo agrega como un nuevo producto.
        - Recalcula el total de la comanda después de agregar el producto.

    Salida:
        None

    Argumentos:
        platillos: Tupla que contiene los platillos disponibles en el sistema, cada uno representado como una tupla con ID, nombre y precio.
        comandas: Diccionario de comandas activas, donde las claves son los folios de las comandas y los valores son diccionarios con los datos de la comanda.
        folio: El número de folio de la comanda en la que se desea agregar o actualizar el producto.

    """
    print("Agregar producto")
    imprimir="actualizar"
    ip.imprimirPlatillos(es_menu=False)
    
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

        # Cálculo del subtotal basado en el platillo seleccionado
        subtotal=cantidad*platillos[platillo-1][2]
        for comanda in comandas.values():  # Itera sobre las comandas abiertas
            
            comanda = comandas.get(folio)  # Obtiene la comanda por folio
            datos=comanda
            if comanda:  # Verifica si la comanda existe
                platillo_encontrado = False
                # Busca si el platillo ya está en la comanda
                for i in range(len(datos['platillos'])): #Itera sobre la cantidad de platillos
                    platillo = u.validar_mismo_platillo(platillo)  # Valida si el platillo existe en el sistema
                    if platillo == datos['platillos'][i][0]:  # Si se encuentra el platillo
                        # Si el platillo ya existe, se actualiza su cantidad y subtotal
                        datos['platillos'][i] = (datos['platillos'][i][0], datos['platillos'][i][1] + cantidad, datos['platillos'][i][2] + subtotal)
                        for buscar in comandas[folio]['platillos']:
                            if buscar == platillo:
                                comandas[folio]['platillos'][buscar] = datos['platillos'][i]  # Actualiza el platillo en la comanda
                        u.calcular_total(folio, comandas)  # Recalcula el total de la comanda
                        u.mostrar_resumen(comandas,folio,imprimir="actualizar")  # Muestra el resumen actualizado de la comanda
                        print("Producto agregado exitosamente.")
                        platillo_encontrado = True
                        break  # Sale del ciclo si se actualizó el platillo

                if not platillo_encontrado:  # Si el platillo no fue encontrado
                        # Si el platillo no existe, se agrega como un nuevo producto
                        for posicion in platillos:
                            if platillo == posicion[1]:  # Busca el platillo en el menú
                                datos['platillos'].append((posicion[1], cantidad, cantidad*posicion[2]))  # Agrega el platillo nuevo
                                print("Nuevo producto agregado exitosamente.")
                                  # Obtiene el folio actualizado
                                u.mostrar_resumen(comandas,folio,imprimir)  # Muestra el resumen actualizado
                                break
                break  # Sale del ciclo de las comandas
        return  # Finaliza la función de agregar producto




# Función para eliminar un producto de la comanda
def eliminar_producto(platillos:tuple,comandas,folio):
    """
    Elimina un producto de la comanda seleccionada.

    Datos de entrada:
        platillos (Tuple[Tuple[int, str, float], ...]): Tupla con los platillos disponibles, donde cada platillo es una tupla con su ID, nombre y precio.
        comandas (dict): Diccionario de comandas activas, donde cada clave es el folio de la comanda y el valor es un diccionario con los detalles de la comanda.
        folio (int): El folio de la comanda de la cual se desea eliminar un producto.

    Proceso:
        - Muestra los productos de la comanda seleccionada y permite al usuario elegir cuál desea eliminar.
        - Si el producto existe, se pide la cantidad a eliminar.
        - Si se desea eliminar todo el producto, este es eliminado completamente de la comanda.
        - Si se desea eliminar una cantidad parcial, se actualiza la cantidad del producto en la comanda.
        - Recalcula el total de la comanda después de la eliminación.

    Salida:
        None

    Argumentos:
        platillos: Tupla con los platillos disponibles en el sistema, cada uno representado como una tupla con ID, nombre y precio.
        comandas: Diccionario de comandas activas donde se realiza la modificación.
        folio: El número de folio de la comanda de la cual se desea eliminar el producto.

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
                id_producto=u.id_por_nombre_platillo(platillos,nombre_producto)

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
                        continuar = u.validar_s_n(f"¿Está seguro de que desea eliminar {cantidad} de {nombre_producto}? (s/n): ")
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
                u.mostrar_resumen(comandas, folio,imprimir="actualizar")
                return
            else:
                print("Opción no válida. Seleccione un producto de la lista.")
   
def aumentar_producto(platillos,comandas,folio):
    """
    Aumenta la cantidad de un producto en una comanda existente.

    Datos de entrada:
        platillos Tuple: Tupla con los platillos disponibles, donde cada platillo es una tupla con su ID, nombre y precio.
        comandas (dict): Diccionario que contiene las comandas activas, donde cada clave es el folio de la comanda y el valor es un diccionario con los detalles de la comanda.
        folio (int): Número de folio de la comanda a actualizar.

    Proceso:
        - Muestra los productos en la comanda seleccionada y permite al usuario elegir cuál desea aumentar en cantidad.
        - El usuario puede ingresar la cantidad adicional que desea agregar.
        - Si la cantidad es válida, se incrementa la cantidad del producto en la comanda.
        - Recalcula el total de la comanda después de la actualización.

    Salida:
        None

    Argumentos:
        platillos: Tupla con los platillos disponibles, cada uno representado por su ID, nombre y precio.
        comandas: Diccionario con las comandas activas en el sistema.
        folio: El número de folio de la comanda que se desea actualizar.

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
                id_producto=u.id_por_nombre_platillo(platillos,nombre_producto)

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
                                print(f"{cantidad} de {nombre_producto} ha sido eliminado.")
                            else:
                                del comandas[folio]['platillos'][producto - 1]
                                print(f"{nombre_producto} ha sido completamente eliminado.")
                else:
                    print("Entrada no válida. Ingrese un número.")
                
                u.calcular_total(folio, comandas)
                u.mostrar_resumen(comandas, folio,imprimir="actualizar")
                return
            else:
                print("Opción no válida. Seleccione un producto de la lista.")
# Función que muestra el menú de actualizaciones
def menu_actualizaciones(comandas,platillos,es_menu) -> None:
    """
    Muestra el menú con las opciones para actualizar la comanda.

    Datos de entrada:
        comandas (dict): Diccionario con las comandas abiertas, donde cada clave es el folio de la comanda y el valor es un diccionario con los detalles de la comanda.
        platillos (tuple): Tupla con los platillos disponibles, donde cada platillo está representado por su ID, nombre y precio.
        es_menu (str): Indicador de si el menú debe ser mostrado inicialmente ("si" o "no").

    Proceso:
        - Si el parámetro 'es_menu' es "si", solicita un nuevo folio de comanda a través de la función 'verificar_comanda'.
        - Si el parámetro 'es_menu' es "no", utiliza el folio previamente seleccionado.
        - Muestra un menú con opciones para agregar, eliminar o aumentar la cantidad de un producto en la comanda seleccionada.
        - Llama a la función correspondiente según la opción seleccionada: 'agregar_producto', 'eliminar_producto' o 'aumentar_producto'.
        - Permite regresar al menú principal seleccionando la opción 4.

    Salida:
        None

    Argumentos:
        comandas: Diccionario que contiene las comandas activas, donde se realiza la actualización.
        platillos: Tupla que contiene los platillos disponibles con su ID, nombre y precio.
        es_menu: Un valor que indica si se debe mostrar el menú de opciones inicialmente. Si es "si", se solicita un nuevo folio; si es "no", se utiliza el folio previamente seleccionado.
    """
    global folioNuevo
    if es_menu == "si":
        folio=u.verificar_comanda(comandas)
        if not folio:
            return
        folioNuevo=folioGlobal(folio)
    elif es_menu == "no":
        folio=folioNuevo
        

    while True:
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
            "estado": "pagada"  # Pueden ser pagadas o no pagadas
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
            "estado": "pagada"  # Pueden ser pagadas o no pagadas
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
            "estado": "pagada"  # Pueden ser pagadas o no pagadas
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
    menu_actualizaciones(comandas,platillos,es_menu="si")
