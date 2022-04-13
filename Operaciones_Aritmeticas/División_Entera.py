'''Hacer un programa de python, que me permita 
calcular la siguiente expresión aritmetica de 
2 números solicitados al usuario y me indique 
si el numero es positivo o no:
X = n1 - (n1*n2)
Nota: debe indicar true si es positivo o False 
si es Negativo'''

# Inicio Programa
print("Este programa resuelve la ecuación x=n1-(n1*n2) ")
n1 = int(input("Escriba el valor de n1: "))
n2 = int(input("Escriba el valor de n2: "))

x = n1 - (n1 * n2)

print("x es igual a: ", x)
print(x > 0)
