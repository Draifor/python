# Convierte una cantidad cualquiera de pesos a dolares
	
# Inicio Programa
print("Calculadora de dolares")	

# Variables
peso = 0
dolar = 0
total = 0

#Ingreso de datos
peso = int(input("Ingrese la cantidad de pesos: "))
dolar = int(input("Ingrese el valor actual del dolar: "))
	
total = peso / dolar
	
print("$", peso, " de pesos, son $", total, " dolares.")