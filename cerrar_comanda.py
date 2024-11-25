import utilerias as u
def cerrar_comanda(comandas:dict,platillos):
    folio=u.verificar_comanda(comandas,platillos)

def disponibilidad_mesas(estado,mesas,num_mesas):
    if estado=="pagado":
        mesas[num_mesas]="Disponible"
    else:
        mesas[num_mesas]="No disponible"
