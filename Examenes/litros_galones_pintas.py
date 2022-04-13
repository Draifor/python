'''Ante las posibles consecuencias del referéndum del "Brexit", escriba 
un programa que permita convertir unidades de volumen de líquidos. 
Concretamente, el programa debe permitir convertir litros en galones 
y pintas y viceversa.

Se recuerda que una pinta son 568.26 ml (es decir, 0.56825 litros) 
y que un galón son 8 pintas.

Al dar las respuestas, el programa debe escribir el número de litros 
con dos decimales, el número de galones sin decimales y el número de 
pintas con un decimal.'''

# Inicio Programa
print("GALONES Y PINTAS\n")

print("Este programa permite:")
print("a. Convertir litros en galones y pintas.")
print("b. Convertir galones y pintas en litros.")

opc = input("\nElija una opción: ")
print()
if opc == "a":
    print("Convertir litros en galones y pintas.")

    litro = float(input("Número de litros: "))
    galon = litro // (.56825 * 8)
    pinta = (litro / .56825) % 8

    print(f"{round(litro, 2)} litros son {int(galon)} galones y {round(pinta, 1)} pintas.")

elif opc == "b":
    print("Convertir galones y pintas en litros.")

    galon = int(input("Número de galones: "))
    pinta = float(input("Número de pintas: "))
    litro = (galon * 8 + pinta) * .56825
    
    print(f"{int(galon)} galones y {round(pinta, 1)} pintas son {round(litro, 2)} litros.")
     
else:  
    print("Debe escribir a o b.")

print("\nPrograma terminado")


'''
GALONES Y PINTAS

Este programa permite:
a. Convertir litros en galones y pintas.
b. Convertir galones y pintas en litros.

Elija una opción: 2

Debe escribir a o b.

Programa terminado
GALONES Y PINTAS

Este programa permite:
a. Convertir litros en galones y pintas.
b. Convertir galones y pintas en litros.

Elija una opción: a

Convertir litros en galones y pintas
Número de litros: 5
5.0 litros son 1 galones y 0.8 pintas.

Programa terminado
GALONES Y PINTAS

Este programa permite:
a. Convertir litros en galones y pintas.
b. Convertir galones y pintas en litros.

Elija una opción: b

Convertir galones y pintas en litros
Número de galones: 3
Número de pintas: 7
3 galones y 7.0 pintas son 17.62 litros.

Programa terminado
3.0 litros son 0 galones y 5.3 pintas.
5.5 litros son 1 galones y 1.7 pintas.
10 galones y 3.0 pintas son 47.17 litros.
0 galones y 0.5 pintas son 0.28 litros.
'''
