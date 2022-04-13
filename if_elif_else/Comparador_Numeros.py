# if ... elif ... else ... 
# EJERCICIO 3
'''Escriba un programa que pida dos números y que conteste 
cuál es el menor y cuál el mayor o que escriba que son iguales.'''

print("Programa para comparar 2 números")
n1 = float(input("Digite un número: "))
n2 = float(input("Digite otro número: "))

if n1 > n2:
  Mensaje = str(n1) + " es mayor que " + str(n2)

elif n1 < n2:
  Mensaje = str(n1) + " es menor que " + str(n2)

else:
  Mensaje = str(n1) + " es igual que " + str(n2)

print(Mensaje)