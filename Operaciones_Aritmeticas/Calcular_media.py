'''Calcular la media de tres números pedidos por teclado.'''
	# Inicio Programa
print("CALCULAR LA MEDIA")
	
    # Definición de variables
n1 = 0 
n2 = 0
n3 = 0
med = 0

    # Ingreso de datos
n1 = int(input("Escribe un número: "))
n2 = int(input("Escribe otro número: "))
n3 = int(input("Escribe otro número: "))

    #Ejecución de los cálculos
med = (n1 + n2 + n3) / 3

	#Mostrar resultados en pantalla
print("La media de los tres números es: ", med)
