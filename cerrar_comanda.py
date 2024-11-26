import utilerias as u
def cerrar_comanda(comandas:dict,platillos,mesas):
    folio=u.verificar_comanda(comandas,platillos)
    cerrar=input("Desea cerrar esta comanda? (s/n)").lower()
    if cerrar == 'n':
        print('Cierre de comanda cancelado')
        return
    else:
        while True:
            propina=u.validar_numerico("Ingrese la propina que desea dejar: ")
            if propina >= 0:
                generar_ticket()
                actualizar_estado_comanda(folio,comandas,mesas)

            else:
                print("La propina no puede ser negativa,intente nuevamente")
                continue

def generar_ticket():
    print('generar ticket')

def actualizar_estado_comanda(folio,comandas,mesas):
    comanda = comandas.get(folio)  # Obtiene la comanda por folio
    if comanda:
        comanda['estado']="pagado"
        disponibilidad_mesas(comandas,mesas,folio)
        print(comanda)
     


def disponibilidad_mesas(comandas,mesas,folio):
    comanda = comandas.get(folio)
    num_mesas=comanda['mesa']
    if comanda['estado']=="pagado":
        mesas[num_mesas]="Disponible"
    else:
        mesas[num_mesas]="No disponible"
    print(mesas)

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
}

}
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
    cerrar_comanda(comandas,platillos,mesas)