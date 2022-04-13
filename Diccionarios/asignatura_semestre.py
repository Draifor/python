'''Ejercicio en Clase
Hacer un Algoritmo en Python que solicite los datos de un Estudiante
(Código, Nombres, Apellidos, Correo, Teléfono) y las asignaturas que 
actualmente ve en la Universidad. Para cada asignatura se debe guardar 
la nota definitiva del semestre (usar el nombre de la Asignatura como 
clave y la nota como valor). 
USAR UN SOLO DICCIONARIO PARA GUARDAR TODOS LOS DATOS.'''

# Inicio programa
print("\nBOLETÍN SEMESTRE")

# Funciones
def addsubjects(boletin):
    # Añadir materias al diccionario mediante el ciclo for

    quant = int(input("\nCuántas asignaturas quiere agregar?: "))
    for i in range(quant):
        subject = input(f"Asignatura {i+1}: ")
        subject = subject.title()
        boletin[subject] = float(input("Nota definitiva: "))
    return boletin

# Ingreso de datos del estudiante
boletin = {}

print("\nIngrese los datos del estudiante: ")
boletin["cod"] = int(input("Código: "))
boletin["first_name"] = input("Nombre: ")
boletin["last_name"] = input("Apellido: ")
boletin["email"] = input("Correo electrónico: ")
boletin["mobile"] = int(input("Celular: "))

# Ingreso de materias
addsubjects(boletin)

# Menú iterativo que permite añadir, modificar o eliminar asignaturas e imprimir el boletín
while True:
    print("\nQué desea realizar: ")
    print("1. Agregar asignaturas")
    print("2. Modificar asignatura")
    print("3. Eliminar asignatura")
    print("4. Imprimir boletín")
    print("5. Salir")
    opt = int(input("Elija una opción: "))

    if opt == 1: 
        addsubjects(boletin)
        print("Las asignaturas se añadieron correctamente")
    
    elif opt == 2:
        subject = input("Nombre de asignatura a modificar: ")
        subject = subject.title()
        if subject in boletin:
            boletin[subject] = float(input("Nuevo valor de nota definitiva: "))
            print("La asignatura '%s' se modificó correctamente."%subject)
        else:
            print("Asignatura no encontrada.")
    
    elif opt == 3:
        subject = input("Nombre de asignatura a eliminar: ")
        subject = subject.title()
        if subject in boletin:
            del boletin[subject]
            print("La asignatura '%s' se eliminó correctamente."%subject)
        else: 
            print("Asignatura no encontrada.")

    elif opt == 4:
        print("\n**************************")
        print("       BOLETÍN SEMESTRE")
        print("**************************")
        print("Código del estudiante: %s" %boletin["cod"])
        print("Nombre: %s %s" %(boletin["first_name"], boletin["last_name"]))
        print("Correo electrónico: %s" %(boletin["email"]))
        print("Celular: %s" %boletin["mobile"])
        print("**************************")
        print("    NOTAS DEFINITIVAS")
        print("**************************")
        
        materias = list(boletin.items())
        print(materias)
        for i in range(5,len(materias)):
            print(f"{materias[i][0]}: {materias[i][1]}")
    
    elif opt == 5:
        break

    else:
        print("Opción inválida")

print('"Si no te gusta cómo son las cosas, cámbialas" (Jim Rohn)')
print("Fin del Programa")


