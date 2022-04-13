'''Hacer un Algoritmo en Python que solicite al usuario las 
calificaciones de un estudiante para cada asignatura en los 4 
periodos cursados en el año (Puede ver hasta 7 Asignaturas en 
el año).'''

# Inicio Programa
print("PLANILLA CALIFICACIONES")

# Variables
subject = 0
qualif = 0
listPeriod = []


def addSubject(listPeriod):
    listSubject = []
    subject = input("Asignatura (-x para salir): ")
    while True:
        if subject.lower() == "x" or len(listSubject) > 6:
            break
        else:   
            qualif = int(input("Calificación: "))
            listSubject.append((subject, qualif)) 
            subject = input("Asignatura (-x para salir): ")

    return listPeriod.append(listSubject)

# Ingreso de datos
print("INGRESO DE CALIFICACIONES POR ASIGNATURA")

for i in range(4):
    print(i + 1, "Periodo")
    addSubject(listPeriod)

# Mostrar al usuario el boletín final

print("***********************")
print ("    BOLETÍN FINAL")
print("***********************")
for i in range(4):
    print(i+1, "Periodo")
    print(listPeriod[i])
    print("***************")

print("FIN DEL PROGRAMA")
