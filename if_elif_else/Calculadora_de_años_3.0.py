# if ... elif ... else ...
# EJERCICIO 4.1 - Diferencia de un año
 
'''Mejore el programa anterior haciendo que cuando la diferencia sea 
exactamente un año, escriba la frase en singular:'''
# Mejor respuesta
 
print("Calculadora de años")
AñoActual = int(input("¿En qué año estamos?: "))
OtroAño = int(input("Escriba otro año: "))
Diferencia = AñoActual - OtroAño
 
if Diferencia == 1:
  Mensaje = "Ha pasado un año desde el " + str(OtroAño)
elif Diferencia > 1:
  Mensaje = "Han pasado " + str(AñoActual - OtroAño) + \
  " años desde el " + str(OtroAño)
elif Diferencia == -1:
  Mensaje = "Falta 1 año para el " + str(OtroAño)
elif Diferencia < -1:
  Mensaje = "Faltan " + str(OtroAño - AñoActual) + \
  " años para que llegue el " + str(OtroAño)
else:
  Mensaje = "¡Estamos en el mismo año!"
 
print(Mensaje)