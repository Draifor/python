'''Diseñar un Algoritmo que permita Imprimir la siguiente serie
de numeros 1,3,5,7,9,11....,n'''

# Inicio Programa
cant = int(input("Escriba la cantidad de términos: "))
i = 0
termino = 1

while i < cant:
    print(termino)
    i += 1
    termino += 2
