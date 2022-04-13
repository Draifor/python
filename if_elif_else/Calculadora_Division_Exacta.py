# if ... elif ... else ...
#EJERCICIO 1 
'''Escriba un programa que pida dos números enteros y que calcule 
su división, escribiendo si la división es exacta o no.'''
#Solución 1
 
print("Este programa calcula una división.")
n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))
 
División = n1 / n2
Residuo = n1 % n2
 
if Residuo == 0: 
  mensaje = "La división es exacta"
 
else:
  mensaje = "La división no es exacta"
 
print("El resultado de la división es: ", División)
print(mensaje)