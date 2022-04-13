# if ... elif ... else ...
# EJERCICIO 12
'''Hacer un programa que permita saber si un año es bisiesto. 
Para que un año sea bisiesto debe ser divisible por 4 y no debe 
ser divisible por 100, excepto que también sea divisible por 400.'''

print("CALCULADORA DE AÑOS BISIESTOS")
año = int(input("Escriba un año: "))

if año % 100 != 0 or año % 400 == 0:
  if año % 4 == 0:
    print(f"¡{año} es un año bisiesto!")
  else:
    print(f"¡{año} no es un año bisiesto!")  
else:
  print(f"¡{año} no es un año bisiesto!")