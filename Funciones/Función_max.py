'''Definir una función max() que tome como argumento dos números 
y devuelva el mayor de ellos. (Es cierto que python tiene una 
función max() incorporada, pero hacerla nosotros mismos es un 
muy buen ejercicio.'''

#Definir función
def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else: 
        return "Son iguales."

#Prueba de la función
a = int(input("Escriba un número: "))
b = int(input("Escriba otro número: "))
print(max(a, b))