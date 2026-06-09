usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None
usuario = None
contrasena = None

while True:
    print("---BIENVENIDO A MENU---")
    print("1 --> Iniciar sesión")
    print("2 --> Registrar usuario")
    print("3 --> Salir")

    while True:
        try:
            op = int(input(""))
            break
        except ValueError:
            print("Ingresa un valor valido (del 1 al 3)")
    


    #
    if op == 1 and usuario1 == None or usuario2 == None or usuario3 == None:
        print("No existe! Es necesario crear un usuario antes. Intente con la opcion 2")
    elif (op == 1) and (usuario1 == usuario and contrasena1 == contrasena) or (usuario2 == usuario and contrasena2 == contrasena) or (usuario3 == usuario and contrasena3 == contrasena):
        
        while True:
            print("")
            print("Realizar llamada --> 1")
            print("Enviar correo electrónico --> 2")
            print("Cerrar sesión --> 3")
            op_menu2 = int(input("Ingresa una opción"))

            if op_menu2 == 1:
                celular = int(input("Ingrese un numero celular de 9 digitos "))
                if celular.startswith(9):
                    break #and len(celular,9):

            elif op_menu2 == 2:
                correo = input("Ingrese un correo: ")
                
                while True:
                    if "@" in correo:
                        print("correo guardado")
                        mensaje = int("ingrese un mensaje para enviar: ")
                        break
                    else:
                        print("Ingrese un correo valido")
            elif op_menu2 == 3:
                print("Cerrando sesión")
    else:
        print("Intente nuevamente!! ")







        
    
    if op == 2:
        print("Vamos a crear un nuevo usuario")
        usuario = input("ingrese nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")
        continue

       




    if op == 3:
        break


    