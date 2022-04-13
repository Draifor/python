'''Escriba un programa que pida la anchura y altura de un rectángulo 
y que escriba su área, su perímetro y la longitud de su diagonal.

Nota: Se recuerda que, por el teorema de Pitágoras, la relación entre 
diagonal y lados de un rectángulo es diagonal2 = anchura2 + altura2. 
Se recuerda que la raíz cuadrada de un número es el número elevado a 0,5.

CÁLCULO DE DATOS DE UN RECTÁNGULO
Escriba la anchura del rectángulo: -4
Escriba la altura del rectángulo: 3
Por favor, escriba valores mayores que cero.
CÁLCULO DE DATOS DE UN RECTÁNGULO
Escriba la anchura del rectángulo: 4.0
Escriba la altura del rectángulo: 3
La superficie del rectángulo es 12.0
El perímetro del rectángulo es 14.0
La diagonal del rectángulo mide 5.0
CÁLCULO DE DATOS DE UN RECTÁNGULO
Escriba la anchura del rectángulo: 35
Escriba la altura del rectángulo: 43
La superficie del rectángulo es 1505.0
El perímetro del rectángulo es 156.0
La diagonal del rectángulo mide 55.4
'''
# Inicio Programa
print("CÁLCULO DE DATOS DE UN RECTÁNGULO")

anchura = float(input("Escriba la anchura del rectángulo: "))
altura = float(input("Escriba la altura del rectángulo: "))

if anchura <= 0 or altura <= 0:
    print("Por favor, escriba valores mayores que cero.")
else:
    area = anchura * altura
    perimetro = 2*anchura + 2*altura
    diagonal = (anchura**2 + altura**2)**0.5 
    print("La superficie del rectángulo es:", area)
    print("El perímetro del rectángulo es:", perimetro)
    print("La diagonal del rectángulo es:", round(diagonal, 1))
