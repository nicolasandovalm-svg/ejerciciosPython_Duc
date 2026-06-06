
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
    
    while True:  
        try:
            cantidad = int(input("Ingrese cantidad de notas: "))
            break
        except ValueError:
            print("Debe ser un valor vañido y entero, intente nuevamnete")

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

def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    for nombre in alumnos:
        print(nombre, ":",alumnos[nombre])

def ver_promedios(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        print(f"{nombre} tiene un promedio de: {round(promedio,2)}")


def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    mayor = 0
    mejorAlumno = ""
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])

        if promedio > mayor:
            mayor = promedio
            mejorAlumno = nombre
    print(f"Mejor alumno: {mejorAlumno}, con promedio: {round(mayor,2)}")

aprobados = 0

def cantidad_aprobados(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])

        if promedio >= 4.0:
            aprobados = aprobados + 1
    print(f"la cantidad de aprobados es: {aprobados}")