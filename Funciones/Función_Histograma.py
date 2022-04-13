'''Definir un histograma procedimiento() que tome una lista de números enteros 
e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) 
debería imprimir lo siguiente: 
****
*********
*******        '''
# Inicio Programa
def procedimiento(lista_numeros):
    for i in range(len(lista_numeros)):
        print(lista_numeros[i] * "*")

# Prueba Función
lista = [1, 2, 3, 2, 1]
procedimiento(lista)