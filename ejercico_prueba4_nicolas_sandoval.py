def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def opcionSelecionada():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 0 or opcion > 6:
                print("Error, ingresa una opcion válida entre 1 y 6")
            else:
                return opcion

        except ValueError:
            print("Error, ingresa una opción válida!")

def agregarEstudiante(lista):
    
    nombre = input("Ingrese nombre del estudiante (no puede estar vacio):  ")
    edad = input("Ingrese edad del estudiante (> 0): ")
    nota = float(input("Ingrese nota del estudiante (número decimal entre 1.0 y 7.0): "))
    

    nombreValido = validarNombre(nombre)
    edadValida = validarEdad(edad)
    notaValida = validarNota(nota)

    if nombreValido == True and edadValida == True and notaValida == True:
        alumnos = {
            "nombre" : nombre,
            "edad" : edad,
            "nota" : nota,
            "aprobado" : False
        }

        lista.append(alumnos)
        print("Alumnoagregado correctamente!")
    else:
        print("Estudiante no agregado, alguno de los datos no son válidos")

def validarNombre(nombreValidar):
    if nombreValidar.strip() == "":
        print("El nombre no puede estar vacio!")
        return False
    else:
        return True

def validarEdad(edadValidar):
    
    try:
        edadValidar = int(edadValidar)

        if edadValidar > 0:
            return True
        else:
            False
    except ValueError:
        print("Error ingreso edad NO válida, debe ser mayor que 0")
        return False
    
def validarNota(notaValidar):
    try:
        notaValidar = float(notaValidar)
        if notaValidar < 1.0 or notaValidar > 7.0:
            print("Error, la nota de debe ser estar entre 1.0 y 7.0")
            return False
        else:
            return True
    except ValueError:
        print("Error ingrese un número")

def buscarEstudiante(lista, nombre):

    for i, alumnos in enumerate(lista):
        if alumnos["nombre"] == nombre:
            return i
    return -1

def actualizarEstados(listaEstudiante):
    for alumnos in listaEstudiante:
        if alumnos["nota"] >= 4.8:
            alumnos['aprobado'] = True
        else:
            alumnos['aprobado'] = False
    
    print("se actualizaron correctamente los Estados de los alumnos")
        
def mostrarEstudiantes(lista):
    if len(lista) == 0:
        print("no existen estudiantes")
        return
    
    actualizarEstados(lista)

    print("=== LISTA DE ESTUDIANTES ===")

    for alumnos in lista:
        print(f"nombre: {alumnos['nombre']}")
        print(f"edad: {alumnos['edad']}")
        print(f"nota: {alumnos['nota']}")

    if alumnos['aprobado']:
        print(f"estado? : APROBADO ")
    else:
        print(f"estado? : NO APROBADO")

    print("*********************************************")
    


#CÓDIGO PRINCIPAL
listaEstudiantes = []

while True:
    mostrarMenu()
    op = opcionSelecionada()

    if op == 1:
        print("Agregando estudiante!")
        agregarEstudiante(listaEstudiantes)
    
    elif op == 2:
        nombre = input("Ingrese nombre de alumno a buscar: ")
        pos = buscarEstudiante(listaEstudiantes, nombre)

        if pos != -1:
            print(f"la posicion es {pos}")
            estudiante = listaEstudiantes[pos]
            print("nombre:" ,estudiante["nombre"])
            print("edad:",estudiante["edad"])
            print("nota:",estudiante["nota"])
            print("aprobado",estudiante["aprobado"])
        else:
            print(f"el estudiante {nombre} no se encuentra registrado")

    elif op == 3:
        nombre = input("ingrese nombre a eliminar: ")
        pos = buscarEstudiante(listaEstudiantes, nombre)
        if pos != -1:
            listaEstudiantes.pop(pos)
            print(f"el estudiante {nombre} eliminado correctamente")
        else:
            print(f"el estudiante {nombre} no se encuentra agregado")

    elif op == 4:
        actualizarEstados(listaEstudiantes)
    
    elif op == 5:
        mostrarEstudiantes(listaEstudiantes)
                
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break