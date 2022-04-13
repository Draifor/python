'''Definir una función que calcule la longitud de una lista 
o una cadena dada. (Es cierto que python tiene la función 
len() incorporada, pero escribirla por nosotros mismos resulta 
un muy buen ejercicio.'''

def len_casera(lista):
  #Esta función calcula la longitud de una lista o una cadena 
  #de caracteres dada e imprime el resultado en pantalla

    contador = 0
    for i in lista:
        contador +=1
    print("La lista tiene {} elementos".format(contador))


