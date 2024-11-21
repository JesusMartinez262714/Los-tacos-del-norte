

def disponibilidad_mesas(estado,mesas,num_mesas):
    if estado=="pagado":
        mesas[num_mesas]="Disponible"
    else:
        mesas[num_mesas]="No disponible"
