'''Definir una función max_de_tres(), que tome tres números 
como argumentos y devuelva el mayor de ellos.'''
# Inicio Programa
def max_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

# Prueba
num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro número: "))
num3 = int(input("EScriba otro número: "))

print(max_de_tres(num1, num2, num3))
