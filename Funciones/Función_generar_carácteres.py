'''Definir una función generar_n_caracteres() que tome un entero n, 
un carácter y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''

# Inicio Programa
# Mi Respuesta
def generar_n_caracteres(numero, letra):
    cadena = ""
    for i in range(numero):
        cadena += letra
    return cadena

# Prueba Función
letra = input("Escriba una letra: ")
numero = int(input("¿Cuántas veces quiere que se repita?: "))
print(generar_n_caracteres(numero, letra))


# Respuesta Más Práctica
'''def generar_n_caracteres(numero, letra):
    print(numero * letra)

# Prueba
letra = input("Escriba una letra: ")
numero = int(input("¿Cuántas veces quiere que se repita?: "))
generar_n_caracteres(numero, letra)'''