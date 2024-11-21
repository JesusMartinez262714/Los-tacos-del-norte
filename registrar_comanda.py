"""
Desarrolladores:Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:
"""

def validar_mesa(mesas,num_mesas):

    if mesas[num_mesas]=="Disponible":
        return True
    else:
        print("La mesa seleccionada ya tiene una comanda abierta. No se puede registrar otra comanda hasta que la actual sea cerrada")
        return False
    
def imprimirPlatillos(platillos):
    #formateo
    print(platillos)

def validar_empleado(empleados):
    while True:
        empleado=int(input("Ingrese  el id del empleado: "))
        if empleado in empleados:
            return empleado
        else:
            print("Empleado no valido,intente nuevamente")
  



def crear_comanda(mesas:dict,platillos:tuple,empleados:dict,Comandas:dict,folio):
    num_mesas=int(input("Ingrese el numero de la mesa "))
    if not validar_mesa(mesas,num_mesas):
        print("La mesa no esta disponible")
    nombre_cliente=input("Ingrese el nombre del cliente: ")
    if nombre_cliente=="":
        nombre_cliente="Cliente anonimo"
    
    empleado=validar_empleado(empleados)
    print("Menu platillos: ")
    print("1.-Tacos de asada - $20")
    print("2.-Tacos de pastor - $18")
    print("3.- Quesadillas -  $25")
    print("4.-Refresco - $15")
    lista_platillos=[]
    registrar_platillos(lista_platillos,platillos)
    mostrarComanda(lista_platillos,nombre_cliente,empleado,num_mesas)


    continuar=input("Desea registrar esta comanda? s/n ").lower()
    
    if continuar=="s":
        estado=input("Ingrese el estado de la comanda (pagado/no pagado)").lower()
        disponibilidad_mesas(estado,mesas,num_mesas)
        folio+=1
        print("Comanda registrada correctamente")
        Comandas[folio]={
            "mesa":num_mesas,
            "empleado":empleado,
            "platillos":lista_platillos,
            "estado":estado
        }
        print(Comandas)
        print(mesas)

def disponibilidad_mesas(estado,mesas,num_mesas):
    if estado=="pagado":
        mesas[num_mesas]="Disponible"
    else:
        mesas[num_mesas]="No disponible"



def registrar_platillos(lista_platillos,platillos):
    while True:
        platillo=int(input("Platillo: "))
        if platillo -1 in range(len(platillos)):
            cantidad_platillo=int(input("Ingrese la cantidad del platillo: "))
            if cantidad_platillo >= 1:
                
                #costo,total=Calculos_Comandas(platillo,cantidad_platillo)
                lista_platillos.append([platillo,cantidad_platillo])
        else:
            print("Ese platillo no existe")
        continuar=input("desea pedir otro platillo?(s/n): ").lower()
        if continuar=="n":
            break


def mostrarComanda(lista_platillos,nombre_cliente,empleado,num_mesas):
    #formateo
    print("")

"""
def Calculos_Comandas(platillo,cantidad_platillo):
    costo=cantidad_platillo*20 if platillo==1 else cantidad_platillo*18 if platillo==2 else cantidad_platillo*25 if platillo==3 else cantidad_platillo*15 if platillo==4 else 0
    subtotal=0
    subtotal+=costo
    agregarPropina=input("Desea agregar propina?")
"""








if __name__ == "__main__":
    listaPlatillos=[]
    platillos=(
        (
            "tacos de asada",20   
        ),

        (
            "tacos de pastor",18
        ),

        (
            "quesadillas",25
        ),

        (
            "Refresco",15
        )
        )

    registrar_platillos(listaPlatillos,platillos)
   













