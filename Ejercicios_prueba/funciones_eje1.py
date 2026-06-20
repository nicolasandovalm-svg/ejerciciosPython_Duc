def validar_nombre(nombre):
    if nombre == "":
        return False
    return True

def validar_precio(precio):
    if precio <= 0:
        return False
    return True

def validar_stock(stock):
    if stock < 0:
        return False
    return True

def validar_lista(inventario):
    if len(inventario) == 0:
        return False
    return True

def agregar_producto(inventario):
    
    nombre = input("Nombre del producto: ")
    if validar_nombre(nombre) == False:
        print("Error: El nombre no puede estar vacio.")
        return
    precio = int(input("Precio del producto: "))
    if validar_precio(precio) == False:
        print("Error: El precio no puede ser menor o igual a 0.")
        return
    stock = int(input("Stock disponible: "))
    if validar_stock(stock) == False:
        print("Error: el stock dee ser mayor o igual a 0 ")
        return 

    producto = {
        "nombre" : nombre.strip(),
        "precio" : precio,
        "stock" : stock,
        "disponible" : False
    }

    inventario.append(producto)
    print("Producto agregado con exito")
    return inventario


def buscar_producto(inventario,nombre):
    if validar_lista(inventario) == False:
        print("No hay productos registrados")
        return -1
    for i in range(len(inventario)):
        if inventario[i]["nombre"] == nombre:
            return i
    return -1


def mostrar_datos_producto(producto):
    if producto["disponible"]:
        estado = "Disponible"
    else:
        estado = "Sin stock"
    
    print(f'Nombre : {producto['nombre']}')
    print(f'Precio : {producto['precio']}')
    print(f'Stock : {producto['stock']}')
    print(f'Estado : {estado}')
    print("-------------------------------------------")
    

def actualizar_disponibilidad(inventario):
    if validar_lista(inventario) == False:
        print("No hay productos registrados")
        return
    for producto in inventario:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False
    return inventario