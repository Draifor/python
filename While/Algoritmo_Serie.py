#SEGUNDO ENUNCIADO:
'''Hacer un algoritmo que imprima los primeros 20 términos de
la siguiente serie:
1, 3, 6, 10, 15, 21, 28,……..'''

#Inicio Programa
print("ALGORITMO SECUENCIAL")

#Variables
count = 1
secuencia = 0

#Fórmula
while count < 20:
    secuencia = secuencia + count
    count += 1
    print(secuencia)
