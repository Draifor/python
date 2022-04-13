'''Debe pedir al usuario una nota (entre 1 y 7). Luego se debe comprobar
 que el número efectivamente esté en ese rango, si no lo está imprima un 
 mensaje de error. Si lo está, imprima reprobado si la nota es inferior 
 a 4, regular si está entre 4 y 5, ok si está entre 5 y 6, y por último, 
 bien si está entre 6 y 7.'''

#Inicio Programa
print("ESTADO DE LA CALIFICACIÓN")

#Variables
nota = 0

#Ingreso de datos
nota = float(input("Escriba la nota (entre 1 y 7): "))

#Validación de datos
if nota >= 1 and nota < 4:
    print("Reprobado!")
elif nota >= 4 and nota < 5:
    print("Regular!")
elif nota >= 5 and nota < 6:
    print("Ok!")
elif nota >= 6 and nota <= 7:
    print("¡Bien!")
else:
    print("Nota inválida!")