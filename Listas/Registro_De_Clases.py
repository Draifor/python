# if ... elif ... else ...
# EJERCICIO 14
'''Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, 
procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes 
de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes 
se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, 
los jueves son para práctica hablada y los viernes se dicta inglés para viajeros. Se debe 
comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde 
[día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario 
ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes 
supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse 
que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición 
se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, 
pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas 
habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará 
cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje 
de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia 
sea mayor al 50% o "no asistió la mayoría" si no es así. Si se trata del inglés para viajeros 
y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de 
nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el 
arancel en $ por cada alumno, para luego imprimir el ingreso total en $.'''

#Inicio Programa
print("REGISTRO DE CLASES")

#Variables
fecha = ["", 0, 0]
dia = ""
numDia = 0
numMes = 0
examen = ""
aprob = 0
reprob = 0
porctAsistencia = 0
cantAlumnos = 0
ingAlumno = 0
ingTotal = 0

#Constantes
diasSemana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
finSemana = ["sabado", "domingo"]

#Ingreso de Fecha
fecha = input("Ingrese la fecha (En formato 'Día, DD/MM'): ")
fecha = fecha.lower()

#Asignación del valor de las variables
dia = fecha[0:fecha.find(",")]
numDia = int(fecha[fecha.find(" ") + 1: fecha.find("/")])
numMes = int(fecha[fecha.find("/") + 1:])

#Establecimiento de las condiciones
if dia not in diasSemana:
     if dia in finSemana:
         print("¡El fin de semana no hay clases!")
     else:
         print("¡El día es incorrecto!")

elif numDia > 31 or numMes > 12:
    print("¡La fecha es incorrecta")

else:
    if dia in diasSemana[0:2]:
        examen = input("Hubo exámenes: Si/No \n")
        if examen.lower() == "si":
            aprob = int(input("¿Cuántos alumnos aprobaron?: "))
            reprob = int(input("¿Cuántos alumnos reprobaron?: "))
            print("El {} porciento de alumnos aprobaron el exámen".format(aprob*100 / (aprob+reprob)))

    elif dia == diasSemana[3]:
        porctAsistencia = int(input("¿Cúal es el porcentaje de asistencia?: "))
        if porctAsistencia > 50 and porctAsistencia <= 100:
            print("¡Asistió la mayoría!")
        
        elif porctAsistencia >= 0 and porctAsistencia <= 50:
            print("¡No asistió la mayoría!")

        else:
            print("¡El porcentaje es incorrecto!")
    
    else: 
        if numDia == 1 and (numMes == 1 or numMes == 7):
            print("¡Comienzo del nuevo ciclo!") 
            cantAlumnos = int(input("¿Cuántos alumnos inician el nuevo ciclo?: "))
            ingAlumno = float(input("¿Cuánto es el arancel por alumno?: $"))
            ingTotal = cantAlumnos * ingAlumno
            print(f"¡El ingreso total es de ${ingTotal}!")
