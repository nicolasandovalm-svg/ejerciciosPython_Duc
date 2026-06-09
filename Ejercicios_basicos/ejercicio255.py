usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

#bucle principal 
while True:
    #menu 1
    print("---Menu---")
    print("1. Iniciar sesión")
    print("2. Registar usuario")
    print("3. salir")
    #primer manejo de error
    while True:
        try:
            opcion = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero")
    #OPCION 1
    if opcion == 1:
        
        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("Debe ingresar un usuario antes de iniciar sesión")
            continue
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")
        if (usuario == usuario1 and contrasena == contrasena1) or (usuario == usuario2 and contrasena == contrasena2) or (usuario == usuario3 and contrasena == contrasena3):
            print("Inicio de sesión exitosa")

            #SUB MENU
            while True:
                print("---MENU DE USUARIO--")
                print("1. Realizar llamada")
                print("2. Enviar correo electrónico")
                print("3. Salir")
                #VALIDACIÓN 2
                try:
                    op = int(input("Seleccione una opción: "))
                except:
                    print("Error, debe ingrear un número")
                    continue

                if op == 1:
                    celular = input("Ingrese un número de 9 digitos, comience con 9")
                    if len(celular) == 9 and celular.startswith("9") and celular.isdigit():
                        print("LLamando al celular: ",celular)
                    else:
                        print("Error, el número no es correcto")
                
                elif op == 2:
                    correo = input("Ingrese su correo: ")
                    valido = False
                    for caracter in correo:
                        if caracter == "@":
                            valido = True
                    
                    if valido:
                        mensaje = input("Ingrese el mensaje del correo: ")
                        print(f"correo enviado a {correo} con mensaje: {mensaje}")
                    
                    else:
                        print("Error correo no válido!")
                
                elif op == 3:
                    print("Cerrar sesión")
                    break
                else:
                    print("Opción no válida!")


    #OPCION 2
    elif opcion == 2:
        print("Registra usuario")
        nuevoUsuario = input("Ingrese un nuevo usuario: ")
        nuevaContrasena = input("Ingrese su clave: ")

        if usuario1 == None:
            usuario1 = nuevoUsuario
            contrasena1 = nuevaContrasena
        elif usuario2 == None:
            usuario2 = nuevoUsuario
            contrasena2 = nuevoUsuario
        elif usuario3 == None:
            usuario3 = nuevoUsuario
            contrasena3 = nuevaContrasena
        else:
            print("Error al ingresar usuario, maximo 3")
    #OPCION 3
    elif opcion == 3:
        print("Saliendo del sistema..")
        break
    else:
        print("Opcion no válida")