'''Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.'''

# Inicio Programa
def es_palindromo(palabra):

    palabra_inv = ""
    for i in range(len(palabra)-1, -1, -1):
        palabra_inv += palabra[i]

    if palabra == palabra_inv:
        return True
    else:
        return False    

# Prueba función
palabra = input("Escriba una palabra: ")
print(es_palindromo(palabra))