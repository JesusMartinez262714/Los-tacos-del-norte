import utilerias as u
def cerrar_comanda(comandas:dict,platillos):
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
                
            else:
                print("La propina no puede ser negativa,intente nuevamente")
                continue

def generar_ticket():
    print('generar ticket')

def disponibilidad_mesas(estado,mesas,num_mesas):
    if estado=="pagado":
        mesas[num_mesas]="Disponible"
    else:
        mesas[num_mesas]="No disponible"
