#   Ejercicio preparativo a examen

#Crear funciones 
def agregar_consola(consolas):
    while True:
        sigla = input("Ingrese sigla de consola agregar -> eje: (PS4, XBOX, PSP...): ").upper()

        if sigla in consolas:
            print("La sigla ya existe, no puede estar repetida, intente nuevamente!")
            return
        else:
            if len(sigla) < 2 or len(sigla) >5:
                print("La sigla debe tener minimo 2 y 5 caracteres maximos!")
                continue
            else:
                if sigla == "":
                    print("La sigla no puede estar vacia!")
                    continue
                else:
                    break
    
    while True:
        nombre = input("Ingrese nombre de la consola: ")
        if nombre == "":
            print("El nombre no puede estar vacio!")
            continue
        else:
            if len(nombre) < 3 or len(nombre) > 40:
                print("La sigla debe tener minimo 3 y 40 caracteres maximos!")
                continue
            else:
                break

    while True:
        fabricante = input("Ingrese el fabricante: ")
        if fabricante == "":
            print("El nombre no puede estar vacio!")
            continue
        else:
            if len(fabricante) < 2 or len(fabricante) > 30:
                print("La sigla debe tener minimo 2 y 30 caracteres maximos!")
                continue
            else:
                break

    while True:
        try:
            año = int(input("Ingrese año de fabricación: "))
            if año < 1972 or año > 2025:
                print("ingrese un año valido (debe estar entre 1972 y 2025)!")
                continue
            else:
                break
        except ValueError:
            print("Ingrese un valor válido!")

    while True:
        try:
            precio = float(input("Ingrese precio : "))
            if precio < 0:
                print("el precio debe ser mayor a 0!")
                continue
            else:
                break
        except ValueError:
            print("Ingrese un valor válido!")
        
    while True:
        try:
            stock = int(input("Ingrese catidad en stock : "))
            if stock <= 0:
                print("el stock no puede ser 0!")
                continue
            else:
                break
        except ValueError:
            print("Ingrese un valor válido!")

    consolas[sigla] = {
        "nombre" : nombre,
        "fabricante" : fabricante,
        "año" : año,
        "precio" : precio,
        "stock" : stock
    }

    print("Consola agregada correctamente!")

def buscar_consola(consolas):
    sigla = input("Ingrese Sigla de la consola que desea buscar: ").upper()
    if sigla in consolas:
        print()
        print("=== Consola Encontrada ===")
        print(f"sigla : {sigla}")
        print(f"nombre : {consolas[sigla]["nombre"]}")
        print(f"fabricante : {consolas[sigla]["fabricante"]}")
        print(f"año : {consolas[sigla]["año"]}")
        print(f"precio : ${consolas[sigla]["precio"]}")
        print(f"stock : {consolas[sigla]["stock"]}")
    else:
        print("La sigla que busca no esta registrada, debe agregarla primero.")
def eliminar_consola(consolas):
    sigla = input("Ingrese consola que desea eliminar: ").upper()
    if sigla in consolas:
        del consolas[sigla]
        print("Consola eliminada correctamente")
        return
    else:
        print("la sigla no existe, debe agregarla primero.")
def mostrar_consolas(consolas):
    if consolas == {}:
        print("No hay consolas registradas..")
        return
    else:
        print("==============================")
        print("LISTADO COMPLETO DE CONSOLAS")
        print("==============================")
        for sigla in consolas:
            print(f"sigla : {sigla} |{consolas[sigla]["nombre"]} |{consolas[sigla]["fabricante"]} | ${consolas[sigla]['precio']}| stock: {consolas[sigla]['stock']}")

        print(f"el total de consolas es {len(consolas)}")



#Crear Diccionarios vacios
consolas = {}
ventas = {}

#Código Principal
while True:
    print()
    print("  ---MENU PRINCIPAL---")
    print("---------------------------------")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("---------------------------------")

    while True:
        try:
            op = int(input("Ingrese una opción: "))
            if op < 1 or op > 5:
                print("la opción debe estar entre 1 y 5, intente nuevamente!")
                continue
            else:
                break
        except ValueError:
            print("Ingrese una opción válida!")
            continue

    if op == 1:
        print("Agregando consola....")
        agregar_consola(consolas)

    elif op == 2:
        print("Buscando consola...")
        buscar_consola(consolas)

    elif op == 3:
        print("vamos eliminar una consola..")
        eliminar_consola(consolas)

    elif op == 4:
        print("Mostrando consolas...")
        mostrar_consolas(consolas)

    elif op == 5:
        print("Saliendo...")
        break



