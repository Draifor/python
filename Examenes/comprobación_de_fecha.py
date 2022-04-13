'''Escriba un programa que pida una fecha y diga si ese día existe.

El programa no tiene por qué comprobar que se escribe una fecha 
posterior al 15 de octubre de 1582, que fue cuando se instauró el 
calendario gregoriano.

Se recuerda que enero, marzo, mayo, julio, agosto, octubre y diciembre 
tienen 31 días, que abril, junio, septiembre y noviembre tienen 30 días 
y febrero tiene 28 días salvo los años bisiestos en que tiene 29.

COMPROBACIÓN DE FECHA
Escriba el número de día: 24
Escriba el número de mes: 2
Escriba el número de año: 2017
El día 24 del mes 2 del año 2017 existe.
COMPROBACIÓN DE FECHA
Escriba el número de día: 40
Escriba el número de mes: 5
Escriba el número de año: 1982
El día 40 del mes 5 del año 1982 no existe.
COMPROBACIÓN DE FECHA
Escriba el número de día: 0
Escriba el número de mes: 13
Escriba el número de año: 1999
El día 0 del mes 13 del año 1999 no existe.
COMPROBACIÓN DE FECHA
Escriba el número de día: 29
Escriba el número de mes: 2
Escriba el número de año: 2016
El día 29 del mes 2 del año 2016 existe.
COMPROBACIÓN DE FECHA
Escriba el número de día: 29
Escriba el número de mes: 2
Escriba el número de año: 1900
El día 29 del mes 2 del año 1900 no existe.
'''

# Inicio Programa
print("COMPROBACIÓN DE FECHA")

dia = int(input("Escriba el número de día: "))
mes = int(input("Escriba el número de mes: "))
año = int(input("Escriba el número de año: "))

fecha = "no existe"

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or \
   mes == 10 or mes == 12:
   if dia > 0 and dia < 31:
       fecha = "existe"

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia < 30:
       fecha = "existe"

elif mes == 2:
    if dia > 0 and dia < 28:
       fecha = "existe" 
    
    elif dia == 29:  
        if año % 100 or not año % 400: 
            if not año % 4:    
                fecha = "existe"
   
print(f"El día {dia} del mes {mes} del año {año} {fecha}.")
