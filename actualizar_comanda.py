"""
Desarrolladores: Jesús Manuel Martínez Cortez 262714, Contreras Ávila Ramsés Norberto 262720
Objetivo: Actualización de productos en una comanda en el sistema.
"""
import utilerias as u
imprimir=""

# Función para verificar si existe una comanda abierta para la mesa proporcionada

    


# Función para agregar un producto a la comanda
def agregar_producto(platillos, verificar, comandas:dict,folio):
    """
    Agrega un producto a una comanda existente.

    Parámetros:
    - platillos (tuple): Tupla con los platillos disponibles.
    - verificar (int): Número de la mesa de la comanda a actualizar.
    - comandas (dict): Diccionario con las comandas abiertas.

    Realiza la actualización en la comanda, ya sea agregando un producto nuevo o actualizando la cantidad de un platillo existente.
    """
    print("Agregar producto")
    imprimir="actualizar"
    u.imprimirPlatillos()
    
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
                        u.mostrar_resumen(comandas,folio,imprimir)  # Muestra el resumen actualizado de la comanda
                        print("Producto agregado exitosamente.")
                        platillo_encontrado = True
                        break  # Sale del ciclo si se actualizó el platillo

                if not platillo_encontrado:  # Si el platillo no fue encontrado
                        # Si el platillo no existe, se agrega como un nuevo producto
                        for posicion in platillos:
                            if platillo == posicion[1]:  # Busca el platillo en el menú
                                datos['platillos'].append((posicion[1], cantidad, cantidad*posicion[2]))  # Agrega el platillo nuevo
                                print("Nuevo producto agregado exitosamente.")
                                verificar = u.obtener_folio_por_mesa(comandas, verificar)  # Obtiene el folio actualizado
                                u.mostrar_resumen(comandas,verificar,imprimir)  # Muestra el resumen actualizado
                                break
                break  # Sale del ciclo de las comandas

        u.verificar_comanda(comandas,platillos)  # Finaliza la función de agregar producto


# Función para eliminar un producto de la comanda
def eliminar_producto(platillos:tuple,verificar,comandas,folio):
    """
    Elimina un producto de la comanda seleccionada.

    Parámetros:
    - platillos (Tuple[Tuple[int, str, float], ...]): Tupla con los platillos disponibles.

    Actualiza el contenido de la comanda eliminando productos o cantidades según las indicaciones del usuario.
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
                u.mostrar_resumen(comandas, folio,imprimir="actualizar")
                return
            else:
                print("Opción no válida. Seleccione un producto de la lista.")
   
def aumentar_producto(platillos,verificar,comandas,folio):
    
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
def menu_actualizaciones(platillos:tuple, verificar: int, comandas:dict) -> None:
    """
    Muestra el menú con las opciones para actualizar la comanda.

    Parámetros:
    - platillos Tuple: Tupla con los platillos disponibles.
    - verificar (int): Número de la mesa de la comanda a actualizar.
    - comandas dict: Diccionario con las comandas abiertas.

    Permite elegir entre agregar, eliminar o aumentar la cantidad de un producto.
    """
    folio=u.verificar_comanda(comandas,platillos)
    print("¿Qué actualización desea realizar? ")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Aumentar cantidad de producto")
    print("4.- Regresar al menú principal")
    opcion = u.validar_numerico('Ingrese una opción: ')
    
    if opcion == 4:
        return
    elif opcion == 1:
        agregar_producto(platillos, verificar, comandas,folio)
    elif opcion == 2:
        eliminar_producto(platillos,verificar,comandas,folio)
    elif opcion == 3:
        aumentar_producto(platillos,verificar,comandas,folio)

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
    u.verificar_comanda(comandas,platillos)
