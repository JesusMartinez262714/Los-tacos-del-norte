"""
Desarrolladores:Jesus Manuel Martinez Cortez 262714, Contreras Avila Ramses Norberto 262720
Objetivo:

"""
folio=0
mesas={
        1:"Disponible",
        2:"Disponible",
        3:"Disponible",
        4:"Disponible",
        5:"Disponible",
        6:"Disponible",
        7:"Disponible",
        8:"Disponible",
        9:"Disponible",
        10:"Disponible",
        11:"Disponible",
        12:"Disponible",
        13:"Disponible",
        14:"Disponible",
        15:"Disponible"

}

Comandas={}




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

empleados={
    1:"juan",
    2:"ramses",
    3:"Paola",
    4:"Fabian"

}
lista_Temporal_Comandas_Abiertas=[]
#Estructuras de almacenamiento
import registrar_comanda as rc
while True:
    print("Menu de opciones Tacos del norte ")
    print("1.-Registrar nueva comanda")
    print("2.-Actualizar una comanda existente")
    print("3.-")
    print("4.-")
    print("5.-")
    print("6.-")
    print("7.-")
    print("8.-")
    print("9.-")
    print("10.-Salir")
    opcion=int(input("Ingrese la opcion : "))
    
    if opcion==10:
        break
    elif opcion==1:
        rc.crear_comanda(mesas,platillos,empleados,Comandas,folio,lista_Temporal_Comandas_Abiertas)
    elif opcion==2:
        print("Opcion 2")
    elif opcion==3:
        print("opcion 3")
    elif opcion==4:
        print("opcion 4")
   



    

