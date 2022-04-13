# if ... elif ... else ...
# EJERCICIO 14
'''Realiza un programa que pida al usuario dos números a y b. Luego debe pedir un 
tercer número que representa una operación matemática (1 para sumar, 2 para resta, 
3 para multiplicación y 4 para división). Debe imprimir en pantalla el resultado 
de operar a con b mediante el operador que quería usar el usuario.'''

print("OPERADOR DE NÚMEROS")
a = float(input("Escriba un número: "))
b = float(input("Escriba otro número: "))
operacion = int(input("¿Qué operación desea? \
  \n1: Suma \n2: Resta \n3: Multiplicación \n4: División \n"))

if operacion == 1:
  suma = a + b
  mensaje = "Suma: {}".format(suma) 
elif operacion == 2:
  resta = a - b
  mensaje = "Resta: {}".format(resta) 
elif operacion == 3:
  multiplicacion = a * b
  mensaje = "Multiplicación: " + str(multiplicacion) 
elif operacion == 4:
  division = a / b
  mensaje = "División: " + str(division) 
else:
  mensaje = "¡Oppss esa no es una opción válida!"

print(mensaje)