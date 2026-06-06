





def agregarAlumnos(alumnos):
    nombre = input("Ingrese el nombre del alumno: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
        return
    
    if nombre in alumnos:
        print("El alumno ya existe")

    if nombre.isdigit():
        print("El nombre debe ser con letras!")
        return
        
    cantidad = int(input("Ingrese cantidad de notas: "))

    notas = []

    for i in range(cantidad):
        print(f"Ingresando nota {i+1}/{cantidad}")
        notaParcial = validaNota()
        notas.append(notaParcial)

    alumnos[nombre] = notas
    print("Alumno agregado correctamente")

def validaNota():
    while True:
        try:
            nota=float(input("Ingrese nota: "))
            if nota >= 1.0 and nota <=7.0:
                return nota
            print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Debe ingresar un valor válido")



alumnos = {}

while True:
    print("--MENU ALUMNOS")
    print("1. Agregar alumnos")
    print("2. Agregar alumnos")
    print("3. Agregar alumnos")
    print("4. Agregar alumnos")
    print("5. Cantidad aprobados")
    print("6. Salir")

    while True: 
        try:
            op = int(input("Ingrese una opción: "))
            break
        except ValueError:
            print("opción no válida")

    if op == 1:
        #AGREGAR_ALUMNOS
        # dato = input("Ingrese datos: ")
        # if dato.isdigit():
        #     print("debe ser letras")
        # else:
        #     print("Correcto! ") se hace con ctrl + }
        agregarAlumnos(alumnos)

    elif op == 2:
        print(alumnos)
    
    elif op == 6:
        break
