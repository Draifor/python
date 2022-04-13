# if ... elif ... else ...
# EJERCICIO 8
'''Escribir un programa que, dado un número entero, muestre 
su valor absoluto. Nota: para los números positivos su valor 
absoluto es igual al número (el valor absoluto de 52 es 52), 
mientras que, para los negativos, su valor absoluto es el 
número multiplicado por -1 (el valor absoluto de -52 es 52).'''
# MI SOLUCIÓN

print("CALCULAR VALOR ABSOLUTO")
n1 = int(input("Escriba un número entero: "))

if n1 >= 0:
  print(f"El valor absoluto de {n1} es {n1}")
else:
  print(f"El valor absoluto de {n1} es {-1 * n1}")