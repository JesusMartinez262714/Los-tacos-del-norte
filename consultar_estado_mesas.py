def consultar_estado_mesas(mesas):
    listaDisponibles=[]
    listaNodisponibles=[]
    disponibles=0
    noDisponible=0
    while True:
        for x,y in mesas.items():
            if y == 'disponible':
                disponibles+=1
                listaDisponibles.append(x)                  
            elif y == 'no disponible':
                noDisponible+=1
                listaNodisponibles.append(x)

        if disponibles<=0:
            print("No hay mesas disponibles en este momento")
        else:
            print(f"hay {disponibles} mesas disponibles que son: {listaDisponibles}")

        if noDisponible<=0:
            print("No hay mesas ocupadas en este momento")
        else:
            print(f"hay {noDisponible} mesas no disponibles que son: {listaNodisponibles}")
        continuar=input("Desea regresar al menu principal? (s/n)").lower().strip()
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