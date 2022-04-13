'''Realiza un programa que reciba una cantidad de minutos 
y muestre por pantalla a cuantas horas y minutos corresponde. 
Por ejemplo: 1000 minutos son 16 horas y 40 minutos.'''
	
	# Inicio Programa
print("CONVERTIDOR DE MINUTOS A HORAS")
	
	#Declaración de variables
min = 0
hour = 0
min_hour = 0
	
	#Ingreso de datos
min = int(input("Escriba una cantidad de minutos"))

	
hour = min // 60
min_hour = min % 60

print(min, " minutos son ", hour, " horas y ", min_hour, " minutos.")
    #Fin Programa
