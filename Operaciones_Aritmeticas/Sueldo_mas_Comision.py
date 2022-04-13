'''Un vendedor recibe un sueldo base mas un 10% extra por 
comisión de sus ventas, el vendedor desea saber cuanto dinero 
obtendrá por concepto de comisiones por las tres ventas que 
realiza en el mes y el total que recibirá en el mes tomando 
en cuenta su sueldo base y comisiones'''
	
	#Inicio Programa
print("CALCULADORA DE SALARIO")
	
	#Definir Variables
salBase = 0 
venta = 0
comision = 0 
salTotal = 0
	
	#Ingreso de datos
salBase = int(input("Ingrese el sueldo base del vendedor"))
venta = int(input("¿Cuánto vendió este mes?"))
	
comision = venta * 0.1
salTotal = salBase + comision
	
print( "************************" )
print( "Sueldo Base: ", salBase )
print( "************************" )
print( "Comisión: ", comision )
print( "************************" )
print( "Sueldo Total: ", salTotal )
print( "************************" )
print( "MUCHAS GRACIAS" )
print( "************************" )
	
	#Fin Programa	




