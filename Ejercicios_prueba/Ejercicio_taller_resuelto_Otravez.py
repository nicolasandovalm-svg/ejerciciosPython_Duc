def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo") 
    print("4. Actualizar disponibilidad") 
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def opcionMenu():
    while True:
        try:
            opcion = int(input("Ingresa una opción: "))

            if opcion < 0 or opcion > 6:
                print("Error, ingresa un valor entre 1 y 6")
            else:
                return opcion
        except ValueError:
            print("Ingrese una opción válida!")

def validarModelo(modelovalidar):
    if modelovalidar.strip == "":
        return False
    else:
        return True
    
def validarAnio(aniovalidar):
    try:
        aniovalidar = int(aniovalidar)

        if aniovalidar <= 1900:
            return False
        else:
            return True
    except ValueError:
        return False
def validarPrecio(precioValidar):
    try:
        precioValidar = float(precioValidar)
        if precioValidar <= 0:
            return False
        else:
            return True
    except ValueError:
        return False
    
def agregarVehiculo(lista):
    modelo = input("Ingrese modelo del vehiculo: ")
    anio = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValido = validarModelo(modelo)
    anioValido = validarAnio(anio)
    precioValido = validarPrecio(precio)

    if modeloValido == True and anioValido == True and precioValido == True:
        vehiculos = {
            "modelo" : modelo,
            "anio" : int(anio),
            "precio" : float(precio),
            "disponible" : False
        }
        lista.append(vehiculos)

        print("Vehiculos agregado correctamente!")
    else:
        print("Los datos ingresados no cumplen con las validaciones")

def buscarVehiculo(lista, modelo):
    for indice, vehiculos in enumerate(lista):
        if vehiculos["modelo"] == modelo:
            return indice # indice donde se encontro

    return -1 # Si no encuentra devolver -1
def actualizarVehiculos(lista):

    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

    print("Se actualizaron los registros de vehiculos")

def mostrarVehiculos(lista):

    if len(lista) == 0:
        print("No existen vehiculos registrados aún")
        return

    actualizarVehiculos(lista)

    print("=== LISTA DE VEHICULOS ===")
    for vehiculo in lista:
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Año: {vehiculo['anio']}")

        if vehiculo['disponible']:
            print(f"Disponible?: DISPONIBLE")
        else:
            print(f"Disponible?: NO DISPONIBLE")


#CÓDIGO PPAL
ListaVehiculos = [] #VARIABLE GLOBAL
while True:

    mostrarMenu()
    op = opcionMenu()

    if op == 1:
        print("Agregando vehiculo...")
        agregarVehiculo(ListaVehiculos)

    elif op == 2:
        vehiculoBuscar = input("Ingrese vehiculo a buscar: ")

        posicion = buscarVehiculo(ListaVehiculos, vehiculoBuscar)
        vehiculoEncontrado = ListaVehiculos[posicion]
        if posicion != -1:
            print("Vehiculo encontrado con exito! su posicion es: ", posicion)
            print(f"modelo : {vehiculoEncontrado["modelo"]}")
            print(f"año : {vehiculoEncontrado["anio"]}")
            print(f"precio : {vehiculoEncontrado["precio"]}")

            if vehiculoEncontrado["disponible"]:
                print(f"disponible? : DISPONIBLE")
            else:
                print(f"disponible? : NO DISPONIBLE")
        else:
            print(f"Vehiculo '{vehiculoBuscar}' no se encuentra registrado")

    elif op == 3:
        modeloBuscado = input("Ingresa el modelo de vehiculo a buscar: ")

        posicion = buscarVehiculo(ListaVehiculos, modeloBuscado)

        if posicion != -1:
            ListaVehiculos.pop(posicion)

            print(f"Vehiculo con modelo '{modeloBuscado}' eliminado")
        else:
            print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.")
    
    elif op == 4:
        actualizarVehiculos(ListaVehiculos)
    
    elif op == 5:
        mostrarVehiculos(ListaVehiculos)

    elif op == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break


