#ariables inicializadas
cupos_gim = 75
cupos_reservar = 0
historial_reservas = 0

#bienvenida
print("¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!")

while True:

    print("*** MENU PRINCIPAL ***")
    print("1.- Cupos disponibles.")
    print("2.- Realizar reserva.")
    print("3.- Cancelar reserva.")
    print("4.- Historial de reservas.")
    print("5.- Salir")
    
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion < 0 or opcion > 5:
            print("Ingrese una opcion valida entre 1 y 5.")
            continue
    except ValueError:
        print("Ingrese un número valido.")
        continue


#Opción 1 mostrar cupos disponibles del gim y atualizarse  
    if opcion == 1:
        print(f"La cantidad de cupos disponibles en el gimnasio es: {cupos_gim}")


#Opcion 2 realizar matriculas

    if opcion == 2:

        while True:
            try:
                cupos_ocupar = int(input("Ingrese la cantidad de cupos a reservar en el gimnasio: "))
                if cupos_ocupar <= 0: #Si la cantidad es negativa.
                    print("Ingrese una cantidad válida, debe ser número mayor a 0.")
                    continue

                if cupos_ocupar > cupos_gim: #Si sobrepasa los cupos que hay, osea que quede en -1
                    print(f"No puede ser mayor a los cupos disponibles del gimnasio (hay {cupos_gim} cupos), intente nuevamenrte")
                    continue
            except ValueError: #VERIFICA SI ES UN NUMERO
                print("Ingrese un numero valido.")
                continue

            cupos_gim = cupos_gim - cupos_ocupar #AQUI dejo UN ESPACIO ENTRE EL CONTINUE PARA SACARLO DEL TRY:  y Actualizas los datos de cupos_gim
            historial_reservas = historial_reservas + cupos_ocupar    #El historial suma los cupos que has usado.
            break 

#Opción 3 para cancelar reservas
    if opcion == 3:
        while True:
            try:
                cupos_liberar = int(input("Ingrese cantidad a cancelar: "))
                if cupos_liberar <= 0:
                    print("Ingrese una cantidad valida, debe ser número mayor a 0.")
                    continue

                if cupos_liberar > historial_reservas:
                    print(f"no puede ser mayor a la cantidad maxima del gym (75), Quedan disponibles {historial_reservas} intente nuevamente.") 
                    continue
            except ValueError: #solo si es un texto dara error.
                print("Ingrese un valor valido.")
                continue
            historial_reservas = historial_reservas - cupos_liberar 
            cupos_gim = cupos_gim + cupos_liberar

            break
    

    if opcion == 4:
        print(f"La cantidad de reservas realizas son {historial_reservas} ")

    if opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

