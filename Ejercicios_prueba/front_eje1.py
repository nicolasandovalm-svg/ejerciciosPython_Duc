import funciones_eje1 as fn 
inventario = []


while True:
    print("-------- MENU PRINCIPAL --------")
    print("1.- Agregar un producto")
    print("2.- Buscar producto")
    print("3.- Eliminar producto")
    print("4.- Actualizar disponibilidad")
    print("5.- Mostrar productos")
    print("6.- Salir")
    print("-------- ---------- --------")

    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break
        except ValueError:
            print("Error: escriba un numero entero")
    
    if opcion == 1:
        inventario = fn.agregar_producto(inventario)
        print(inventario)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        posicion = fn.buscar_producto(inventario,nombre)
        if posicion != -1:
            print(f'\nProducto encontrado en la posicion {posicion} : ')
            fn.mostrar_datos_producto(inventario[posicion])
        else:
            print(f'El producto {nombre} no se encuentra registrado.')

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a eliminar:")
        posicion = fn.buscar_producto(inventario,nombre)
        if posicion != -1:
            del inventario[posicion]
            print("Producto eliminado correctamente")
        else:
            print(f'El producto {nombre} no se encuentra registrado.')
    
    elif opcion == 4:
        inventario = fn.actualizar_disponibilidad(inventario)
        print("Disponibilidad actualizada para todos los productos.")

    elif opcion == 5:
        for producto in inventario:
            fn.mostrar_datos_producto(producto)
    
    elif opcion == 6:
        print("Saliendo....")
        break
    else:
        print("Ingrese una opcion validad (1-6)")