import utilerias as u
def consultar_ventas(comandas,empleados):
      #formateo y hacer que se muestre al registrar una comanda
    contador=0
    totalT=0
    print("Comandas cerradas:")
    print(f"{"":-^65}")
    print(f"{"folio":<9}{"Mesa":<9}{"Cliente":<16}{"Empleado":<17}Total ($)")
    print(f"{"":-^65}")
    for folio,datos in comandas.items():
        if datos["estado"] == "pagada":
            #agrega la fecha con el daytime
            print(f"{folio }{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
            contador+=1
            totalT+=int(datos['total'])
            print(totalT)


            filtro=u.validar_numerico("Desea filtrar por mesa (1) o empleado (2)? (-1 para salir)")
            if filtro == -1:
                return
            elif filtro==1:
                mesa=u.validar_numerico("Ingrese el numero de la msea")
                if mesa == datos['mesa']:
                    print(f"{folio }{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
                else:
                    print(f"No hay ventas registradas para la mesa {mesa}")  
            elif filtro==2:
                Empleado=u.validar_empleado(empleados)
                if Empleado == datos['empleado']:
                    print(f"{folio }{datos['mesa']:<9}{datos['cliente']:<16}{datos['empleado']:<17}{datos['total']}")
                else:
                    print(f"No hay ventas registradas para el empleado {Empleado}")
        else:
            print("no hay ventas del dia")
    return


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
        "estado" : "pagada" #Pueden ser pagadas o no pagadas
}

}
    empleados = {
    101: {
        "nombre": "María López",
        "telefono": "6441234567",
        "estado": "activo"
    },
    102: {
        "nombre": "Pedro Martínez",
        "telefono": "6449876543",
        "estado": "inactivo"
    }
}
    consultar_ventas(comandas,empleados)