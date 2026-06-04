#Estructura sugerida
# productos = {"Mouse":[10,15000],"Teclado":[5,25000],"Monitor":[3,180000]}

productos = {}

while True:
    print("----MENU----")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")

    try:
        op = int(input("Seleccione una opción: "))
        if op <= 0:
            print("Selecione un opción entre 1 y 5, intente nuevamente! ")
            continue
        if op > 5:
            print("Selecione un opción entre 1 y 5, intente nuevamente! ")
            continue
        
    except ValueError:
        print("Opción inválida intente nuevamente!!")
        continue

    

    def agregar_producto(productos):
        '''Esta función permite agregar productos nuevos a un diccionario'''
        while True:
            nombre = input("Ingrese nombre del producto: ").strip()
            if nombre == "":
                print("El nombre del producto no puede estar vacio!")
                continue

            if nombre in productos:
                print("El producto ya EXISTE, no puede estar repetido!!")
                continue

            try: 
                stock = int(input("Ingrese la cantidad en stock: "))
                if stock <= 0:
                    print("El stock debe ser un numero entero mayor o igual a 0.")
                    continue

            except ValueError:
                print("Opcion no valida")
                continue

            try: 
                precio = int(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("El stock debe ser un numero entero mayor que 0.")
                    continue

            except ValueError:
                print("Opcion no valida")
                continue
            break   

        productos[nombre] = [stock,precio]

    def mostrar_productos(productos):
        '''Esta función permite mostrar los productos que estan en el diccionario'''
        if len(productos) == 0:
            print("No existen productos")
            return

        for nombre in productos:
            print(nombre, "-Stock: ",productos[nombre][0],"-Precio: $",productos[nombre][1])


    def buscar_producto(productos):
        '''Esta funcion permite buscar un productos y saber si existe o no!'''
        while True:
            buscador = input("Ingrese clave del producto que desea buscar: ").strip()

            if buscador in productos:
                print(f"El producto que busca si esta en la lista")
                break
            else:
                print("El producto que desea buscar no existe!")
                break
    
    def producto_mas_caro(productos):
        if len(productos) == 0:
            print("No existen productos")
            return
        mayor = 0
        nombreMayor = ""
        
        for nombre in productos:
            precio = productos[nombre][1]

            if precio > mayor:
                mayor = precio
                nombreMayor = nombre
        print(f"El producto mas caro es {nombreMayor}")
        print(f"Su valor es {mayor}")
        
        

    if op == 1: 
        print("Agregando productos....")
        agregar_producto(productos)
        print("Producto agregado exitosamente!")

    

    elif op == 2:
        print("Mostrando productos!!")
        print()
        mostrar_productos(productos)
        print()
        
    

    elif op == 3:
        print("Buscando Productos...")
        print()
        buscar_producto(productos)


    elif op == 4:
        print("Buscando el Producto más caro...")
        print()
        producto_mas_caro(productos)


    elif op == 5:
        break

