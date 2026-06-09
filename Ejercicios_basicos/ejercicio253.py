ingreso = True
saldo = 100000
while ingreso:
    print("--Menu--")
    print("--Menu--")
    print("--Menu--")
    print("--Menu--")
    op = int(input("Ingrese su opción"))

    if op == 1:
        print("Pganado..")
        montopagar = int(input("Ingrese monto a pagar: "))
        if montopagar >= 0:
            if montopagar <= saldo:
                saldo = saldo - montopagar
                print("El saldo de la tarjeta es: $", saldo)
    elif op == 2:
        print("Comprando...")
    elif op == 3:
        print("Saliendo")
        #break
        ingreso = False
    else:
        (print("Opción no valida"))

print("Hola")
