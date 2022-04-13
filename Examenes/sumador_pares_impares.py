'''Escriba un programa que pida primero cuántos números se van a 
escribir, que pida a continuación esa cantidad de números y al 
final diga tanto la suma de los números pares introducidos como 
la suma de los números impares introducidos. El programa no necesita 
comprobar que los valores introducidos sean positivos.'''

# Inicio programa
print("SUMADOR DE PARES E IMPARES")

pares = 0
impares = 0
cant = int(input("¿Cuántos números quiere ingresar?: "))

if cant > 0:
    for i in range(cant):
        num = int(input("Escriba un número entero: "))
        if num % 2:
            impares += num
        else: 
            pares += num
    print("La suma de los números pares ingresados es:", pares)
    print("La suma de los números impares ingresados es:", impares)
print("Programa terminado")
