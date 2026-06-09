usuarios = {} #Inicializo el diccionario


def ingresar_usuario(usuarios): 
    ''' Esta funcion agrega un usuario, validando nombre, validando sexo y contraseña'''
    #Pedimos nombre de usuario a ingresar y con strip eliminamos espacios.
    print("---INGRESAR USUARIO---")
    nombre = input("Ingrese el nombre del usuario: ").strip().upper()

    #Validamos que no ingrese un nombre vacio!
    if nombre == "":
        print("El nombre no puede estar vacio")
        return
    #Validamos si el usuario ya existe!
    if nombre in usuarios:
        print("El usuario ya existe!")
        return
    #Validamos que sea texto y no número
    if nombre.isdigit():
        print("El nombre debe ser con letras!")
        return

    #Pedimos que ingrese el sexo del usuario a registrar
    sexo = input("Ingrese sexo del usuario (F/M): ").lower()

    #Validamos que sea una opcion correcta F | M.
    if sexo == "f" or sexo == "m":
        print("agregando correctamente...")
    else:
        print("Ingrese una opción Válida F o M")
        return
    
    #Bucle para controlar contraseña
    while True:
        contraseña = input("Ingrese una contraseña: ").strip()#pedimos la contraseña al usuario
        
        #Validamos que no tenga menos de 8 caracteres
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")
            continue

        tiene_numero = False #Inicializamos variable
        tiene_letra = False #Inicializamos variable 

        for i in contraseña: #Bucle para ver si hay numeros y letras
            if i.isdigit(): 
                tiene_numero = True 
                
            if i.isalpha():
                tiene_letra = True
     
        if tiene_letra == True and tiene_numero == True:
            print("Contraseña Válida!!")
            usuarios[nombre] = {"sexo": sexo.upper(), "contraseña":contraseña}
            print("Usuario creado con exito")
            break
        else:
            print("Contraseña debe contener al menos un digito numerico y una letra, intentelo nuevamente!")
            continue
             
def buscar_usuario(usuarios):
    '''Esta función busca un usuario por su nombre y muestra sus datos si existe'''
    print("---BUSCAR USUARIO---")
    nombre_buscar = input("Ingrese el nombre del usuario a buscar: ").strip().upper()
    if len(usuarios) == 0:
        print("No hay usuarios registrados")
        return
    
    if nombre_buscar in usuarios:
        datos = usuarios[nombre_buscar] 
        print("¡Usuario encontrado!")
        print(f"Nombre: {nombre_buscar}")
        print(f" Sexo: {datos['sexo']}")
        print(f"Contraseña: {datos['contraseña']}")
    else:
        #  Si no existe, le avisamos al usuario
        print(" El usuario no se encuentra registrado.")

def eliminar_usuario(usuarios):
    '''Esta función busca un usuario por su nombre y lo elimina junto a sus datos si existe'''
    print("--- ELIMINAR USUARIO ---")
    
    # Validamos primero si hay usuarios en el diccionario
    if len(usuarios) == 0:
        print("No hay usuarios registrados para eliminar.")
        return

    # Pedimos el nombre del usuario que se desea borrar
    nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ").strip().upper()

    # Verificamos si el usuario existe en el diccionario
    if nombre_eliminar in usuarios:
        del usuarios[nombre_eliminar]#eliminamos la clave y el valor
        print("Usuario eliminado con exito!")
    else:
        print("No se pudo eliminar usuario!")


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

    elif op == 2:
        buscar_usuario(usuarios)
    
    elif op == 3:
        eliminar_usuario(usuarios)

    elif op == 4:
        print("SALIENDO...")
        break
