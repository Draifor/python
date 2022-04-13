# if ... elif ... else ...
#EJERCICIO 1.2 - División por cero
'''Mejore el programa anterior haciendo que tenga en 
  cuenta que no se puede dividir por cero'''

print("Programa divisor de números.")
n1 = int(input("Digite el dividendo: "))
n2 = int(input("Digite el divisor: "))

if not n2:
  Mensaje = "No se puede dividir por 0"
else:
  Cociente = n1 // n2
  Residuo = n1 % n2
 
  if Residuo:
    Mensaje = "La división no es exacta. El cociente es: " \
    + str(Cociente) + " y el residuo: " + str(Residuo)

  else:
    Mensaje = "La división es exacta. El cociente es: " \
    + str(Cociente)

print(Mensaje)