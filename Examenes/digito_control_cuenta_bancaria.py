'''Escriba un programa que calcule el primer dígito de control 
de una cuenta bancaria, el que corresponde al código de entidad 
y oficina.

Las cuatro cifras del código de entidad se multiplican, de izquierda 
a derecha, por 4, 8, 5 y 10, respectivamente.
Las cuatro cifras del número de oficina se multiplican, de izquierda 
a derecha por 9, 7, 3 y 6, respectivamente.
Se suman los resultados de las multiplicaciones anteriores.
Se divide por 11 y se toma el resto.
El dígito de control es la diferencia entre 11 y el resto anterior. 
Si el resultado es 10, el dígito de control es 1. Si el resultado es 11, 
el dígito de control es 0
Dígitos de control de ejemplo: 0375 1281 => 3; 0038 3676 => 1; 
9517 5646 => 0; 8194 7118 => 7

# Prueba 1
DÍGITO DE CONTROL CUENTA CORRIENTE

Escriba el primer dígito de la entidad: 2
Escriba el segundo dígito de la entidad: 0
Escriba el tercer dígito de la entidad: 3
Escriba el cuarto dígito de la entidad: 8

Escriba el primer dígito de la oficina: 6
Escriba el segundo dígito de la oficina: 4
Escriba el tercer dígito de la oficina: 3
Escriba el cuarto dígito de la oficina: 3

El dígito de control es 8.

Programa terminado

#Prueba 2
DÍGITO DE CONTROL CUENTA CORRIENTE

Escriba el primer dígito de la entidad: -2
Escriba el segundo dígito de la entidad: 0
Escriba el tercer dígito de la entidad: 3
Escriba el cuarto dígito de la entidad: 88

Escriba el primer dígito de la oficina: 6
Escriba el segundo dígito de la oficina: 4
Escriba el tercer dígito de la oficina: 3
Escriba el cuarto dígito de la oficina: 3

Lo siento. No ha escrito correctamente los dígitos.

Programa terminado'''

# Inicio programa
print("DÍGITO DE CONTROL CUENTA CORRIENTE")
print()
c_ent_1 = int(input("Escriba el primer dígito de la entidad: "))
c_ent_2 = int(input("Escriba el segundo dígito de la entidad: "))
c_ent_3 = int(input("Escriba el tercer dígito de la entidad: "))
c_ent_4 = int(input("Escriba el cuarto dígito de la entidad: "))
print()
c_ofi_1 = int(input("Escriba el primer dígito de la oficina: "))
c_ofi_2 = int(input("Escriba el segundo dígito de la oficina: "))
c_ofi_3 = int(input("Escriba el tercer dígito de la oficina: "))
c_ofi_4 = int(input("Escriba el cuarto dígito de la oficina: "))
print()

if (0 > c_ent_1 or c_ent_1 > 9) or (0 > c_ent_2 or c_ent_2 > 9) or \
   (0 > c_ent_3 or c_ent_3 > 9) or (0 > c_ent_4 or c_ent_4 > 9) or \
   (0 > c_ofi_1 or c_ofi_1 > 9) or (0 > c_ofi_2 or c_ofi_2 > 9) or \
   (0 > c_ofi_3 or c_ofi_3 > 9) or (0 > c_ofi_4 or c_ofi_4 > 9):

    print("Lo siento. No ha escrito correctamente los dígitos.")

else: 

    ent = c_ent_1*4 + c_ent_2*8 + c_ent_3*5 + c_ent_4*10
    ofi = c_ofi_1*9 + c_ofi_2*7 + c_ofi_3*3 + c_ofi_4*6

    resto = (ent + ofi) % 11
    dig_cont = 11 - resto

    if dig_cont == 10:
        dig_cont = 1
    elif dig_cont == 11:
        dig_cont = 0
    

    print(f"El dígito de control es {dig_cont}.")
print()
print("Programa terminado")
