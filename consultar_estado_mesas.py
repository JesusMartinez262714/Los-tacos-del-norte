def consultar_estado_mesas(mesas):
    """
    Consulta el estado de las mesas, mostrando las mesas disponibles y ocupadas.

    Parámetros:
    - mesas (dict): Diccionario que contiene el estado de cada mesa, donde la clave es el número de mesa
                    y el valor es el estado ("disponible" o "no disponible").
    
    Proceso:
        - La función recorre el diccionario de mesas y clasifica las mesas en dos categorías: disponibles y ocupadas.
        - Muestra la lista de mesas disponibles y ocupadas. Si no hay mesas en alguna de estas categorías, 
          imprime un mensaje indicando que no hay mesas disponibles o no ocupadas.

    Salida:
    - Imprime en pantalla el estado de las mesas, dividiéndolas en "Mesas Disponibles" y "Mesas Ocupadas".
    - Si no hay mesas disponibles o ocupadas, muestra un mensaje informativo.
    - Pregunta al usuario si desea regresar al menú principal o continuar consultando.

    Argumentos:
    - mesas: Un diccionario donde las claves son los números de las mesas y los valores son los estados de las mismas 
      ("disponible" o "no disponible").
    """
    import utilerias as u
    listaDisponibles=[]
    listaNoDisponibles=[]
    disponibles=0
    noDisponible=0
    while True:
        for x,y in mesas.items():
            if y == 'disponible':
                disponibles+=1
                listaDisponibles.append(x)                  
            elif y == 'no disponible':
                noDisponible+=1
                listaNoDisponibles.append(x)

        if disponibles<=0:
            print("No hay mesas disponibles en este momento")
        elif noDisponible<=0:
            print("No hay mesas ocupadas en este momento")
        else:
            print(f"{"Estado de las Mesas":-^25}")
            print("Mesas Disponibles: ")
            vueltasForDisponible=0
            for mesa in listaDisponibles:
                vueltasForDisponible+=1
                if vueltasForDisponible < len(listaDisponibles):

                    print(f"{mesa}", end=", ")
                else:
                    print(f"{mesa}")
            print("Mesas Ocupadas: ")
            vueltasForNoDisponible=0
            for mesaNo in listaNoDisponibles:
                vueltasForNoDisponible+=1
                if vueltasForNoDisponible < len(listaNoDisponibles):
                    print(f"{mesaNo}", end=", ")
                else:
                    print(f"{mesaNo}")
            print(f"Total de mesas ocupadas: {noDisponible}")
            print(f"Total de mesas ocupadas: {disponibles}")
                
        
        continuar=u.validar_s_n("Desea regresar al menu principal? (s/n)")
        if continuar=='s':
            return
        elif continuar=='n':
            continue














if __name__ == "__main__":
 mesas = {
        1: "disponible",
        2: "disponible",
        3: "no disponible",
        4: "disponible",
        5: "disponible",
        6: "disponible",
        7: "disponible",
        8: "disponible",
        9: "disponible",
        10: "disponible",
        11: "disponible",
        12: "disponible",
        13: "disponible",
        14: "disponible",
        15: "disponible"

}
 consultar_estado_mesas(mesas)