'''Definir una función inversa() que calcule la inversión de una cadena. Por 
ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''

# Inicio Programa
def funcion_inversa(cadena):

    cadena_inv = ""
    for i in range(len(cadena)-1, -1, -1):
        cadena_inv += cadena[i] 
        
    return cadena_inv

# Prueba función
cadena = input("Escriba una frase: ")
print(funcion_inversa(cadena))
