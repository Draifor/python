# if ... elif ... else ...
# EJERCICIO 4.1 - Diferencia de un año

'''Mejore el programa anterior haciendo que cuando la diferencia sea 
exactamente un año, escriba la frase en singular:'''
# Mi Respuesta

print("Calculadora de años")
AñoActual = int(input("¿En qué año estamos? "))
OtroAño = int(input("Escriba otro año: "))

if AñoActual < OtroAño:
  if OtroAño - AñoActual ==1:
   Mensaje = "Falta 1 año para que llegue el " + str(OtroAño) 
  else:
     Mensaje = "Faltan " + str(OtroAño - AñoActual) + " años para que llegue el " + str(OtroAño)

elif AñoActual > OtroAño:
  if AñoActual - OtroAño ==1:
    Mensaje = "Ha pasado 1 año desde el " + str(OtroAño)
  else:
    Mensaje = "Han pasado " + str(AñoActual - OtroAño) + " años desde el " + str(OtroAño)

else:
  Mensaje = "¡Estamos en ese mismo año"

print(Mensaje)