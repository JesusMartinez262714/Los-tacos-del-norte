"""

"""

def validar_mesa(mesas,num_mesas):

    if mesas[num_mesas]=="Disponible":
        return True
    else:
        return False

def crear_comanda(mesas,platillos,empleados):
    num_mesas=int(input("Ingrese el numero de la mesa "))
    if not validar_mesa(mesas,num_mesas):
        print("La mesa no esta disponible")
    nombre_cliente=input("Ingrese el nombre del cliente: ")
    if nombre_cliente=="":
        nombre_cliente="Cliente anonimo"
    
    empleado=input("Ingrese  el id del empleado: ")
    print("Menu platillos")
    print(platillos)
    lista_platillos=[]
    registrar_platillos(lista_platillos,platillos)
    print(num_mesas,nombre_cliente,empleado,lista_platillos)

def registrar_platillos(lista_platillos,platillos):
    while True:
        platillo=int(input("Platillo: "))
        if platillo -1 in range(len(platillos)):
            cantidad_platillo=int(input("Ingrese la cantidad del platillo: "))
            if cantidad_platillo >= 1:
                lista_platillos.append([platillo,cantidad_platillo])
        continuar=input("desea pedir otro platillo?(s/n): ").lower()
        if continuar=="n":
            break




   













