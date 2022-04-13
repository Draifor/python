'''Escriba un programa conversor de centímetros a kens y shakus, 
unidades japonesas de longitud.

Se recuerda que un ken son seis shakus y que un shaku equivale a 30,3 cm.

Si se pone un número no positivo, el programa debe dar un aviso de error. 
Escriba el resultado de shakus con dos decimales.

CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS
Escriba la cantidad de centímetros: -5
Por favor, escriba un número positivo.
CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS
Escriba la cantidad de centímetros: 100
100 cm son 3.3 shakus, es decir 0 ken(s) y 3.3 shaku(s).
CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS
Escriba la cantidad de centímetros:  2000
2000 cm son 66.01 shakus, es decir 11 ken(s) y 0.01 shaku(s).
CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS
Escriba la cantidad de centímetros: 9876
9876 cm son 325.94 shakus, es decir 54 ken(s) y 1.94 shaku(s).
'''

# Inicio Programa
print("CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS")

cm = int(input("Escriba la cantidad de centímetros: "))

if cm < 0:
    print("Por favor, escriba un número positivo.")
else:
    shaku = round(cm / 30.3, 2)
    ken = int(shaku // 6)
    shakuResto = round(shaku % 6, 2)
    print(cm, f"cm son {shaku} shakus, es decir {ken} ken(s) y {shakuResto} shaku(s).")
