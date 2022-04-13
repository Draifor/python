# if ... elif ... else ...
# EJERCICIO 9
'''Solicitar al usuario que ingrese los nombres de dos personas, 
los cuales se almacenarán en dos variables. A continuación, imprimir 
“coincidencia” si los nombres de ambas personas comienzan con la 
misma letra ó si terminan con la misma letra. Si no es así, imprimir 
“no hay coincidencia”.'''

print("COMPARADOR DE NOMBRES")
nombre1 = input("Escriba un nombre: ")
nombre2 = input("Escriba otro nombre: ")
ult_letra_nomb1 = len(nombre1) - 1
ult_letra_nomb2 = len(nombre2) - 1

if nombre1[0] == nombre2[0] or nombre1[ult_letra_nomb1] == nombre2[ult_letra_nomb2]:
  print("¡Coincidencia!")
else:
  print("¡No hay coincidencia!")