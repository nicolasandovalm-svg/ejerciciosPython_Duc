usuarios = {}


def ingresar_usuario(usuarios):
    
    nombre = input("Ingrese el nombre del usuario: ").strip()


    if nombre == "":
        print("El nombre no puede estar vacio")
        return
    
    if nombre in usuarios:
        print("El alumno ya existe")
        return

    if nombre.isdigit():
        print("El nombre debe ser con letras!")
        return

    sexo = input("Ingrese sexo del usuario (F/M): ").upper()

    if sexo == "F" or sexo == "M":
        print("agregando correctamente...")
    else:
        print("Ingrese una opción Válida F o M")
        return
        
    num = False
    while True:
        contraseña = input("Ingrese una contraseña: ").strip()
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")
            continue
        for i in contraseña:
            if  i.isdigit(): 
                num = True 
            else:
                print("Contraseña debe contener almenos un digito numerico")
                continue
            if i in abcedario:
                print("Bien contraseña contiene almenos una letra ")
                print("Contraseña válida")   
            else:
                print("Contraseña invalida debe contener almenos 1 letra")
                break
            
            
        

    









#bucle ppal

while True:
    print("---MENU---")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

    try:
        op = int(input("seleccione una opción: "))
        if (op < 1) or (op > 4):
            print("Ingrese una opción entre 1 a 4!")
            continue
    except ValueError:
        print("Ingrese una opción Válida!")
        continue

    if op == 1:
        ingresar_usuario(usuarios)

    elif op == 4:
        print("SALIENDO...")
        break
