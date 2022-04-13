# if ... elif ... else ...
# EJERCICIO 4
'''Escriba un programa que pida el año actual y un año cualquiera y que escriba
   cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.'''

print("Calculadora de años")
AñoActual = int(input("¿En qué año estamos? "))
OtroAño = int(input("Escriba otro año: "))

if AñoActual < OtroAño:
  Mensaje = "Faltan " + str(OtroAño - AñoActual) + \
  " años para que llegue el " + str(OtroAño)

elif AñoActual > OtroAño:
  Mensaje = "Han pasado " + str(AñoActual - OtroAño) + \
  " años desde el " + str(OtroAño)

else:
  Mensaje = "¡Estamos en ese mismo año"

print(Mensaje)