'''usuarios2 = {
    "daniel":{"sexo" : "M",
              "pass" : "1234asdf"
              },
              "Jorge" : {"sexo":"M",
                         "pass":"4567asdf"
                         }
}
'''
#funciones

def ingresar_usuario():
    
    while True:
        nombre = input("Ingrese nombre de usuario")
    
        if nombre in usuarios:
            print("Usuario ya existe, intente con otro!")
        else: 
            break

    while True:
        sexo = input("Ingrese sexo (F/ M)").upper()

        if sexo == "F" or sexo == "M":
            break
        else:
            print("El sexo debe ser M O F, ingrese nuevamente! ")

    while True:
        contraseña = input("Ingrese contraseña: ")

        if validar_contraseña(contraseña):
         print("Contraseña valida")
         break
        else:
            print("Contraseña inválida, debe tener 8 caracteres y un número")

    usuarios[nombre] = {
        "sexo":sexo,
        "contraseña":contraseña
    }  


def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    
    if " " in contraseña:
        return False
    
    num = False
    letra = False
    
    for caracter in contraseña:
        if caracter.isdigit():
            num = True
        if caracter.isalpha():
            letra = True
    return num and letra

def buscar_usuario():
    nombre = input("ingrese nombre a buscar")

    if nombre in usuarios:
        print("sexo", usuarios[nombre]["sexo"])
        print(f" contraseña: {usuarios[nombre["contraseña"]]}")
    else:
        print("nombre no encontrado")

def eliminar_usuario():
    nombre = input("ingrese nomber a eliminar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("usuario eliminado")
    else:
        print("nombre no encontrado")
    




    







#---parte ppal-----
usuarios = {}

while True:
    print("MENU PRINCIPAL")
    print("1 Ingresar usuario")
    print("2 Buscar usuario")
    print("3 Eliminar usuario")
    print("4 Salir")

    while True:
        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Por favor ingrese una opción válida")

    if op == 1:
        ingresar_usuario()
    elif op== 2:
        buscar_usuario()
    elif op == 3:
        eliminar_usuario()
    elif op == 4:
        print("Saliendo...")
        break
    else:
        print("Ingrese un valor entre 1 y 4")