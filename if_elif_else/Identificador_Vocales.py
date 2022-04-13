# if ... elif ... else ...
# EJERCICIO 11
'''Escribir un programa que solicite al usuario una letra y, 
si es una vocal, muestre el mensaje “es vocal”. Se debe validar 
que el usuario ingrese sólo un carácter. Si ingresa un string 
de más de un carácter, informarle que no se puede procesar 
el dato.'''
# MI SOLUCIÓN

letra = input("Escriba una letra: ")
letra = letra.lower()
if len(letra) > 1:
  print("¡Hay más de una letra! No se puede procesar el dato")

elif letra == "a" or letra == "e" or letra == "i" \
     or letra == "o" or letra == "u":
  print("¡Es una vocal!")



# MEJOR SOLUCIÓN
'''
letra = input("Escriba una letra: ")

if len(letra) != 1:
  print("¡Debe ser solo una letra!")
else:
  if letra in "AaEeIiOoUu":
    print("¡Es una vocal!")'''