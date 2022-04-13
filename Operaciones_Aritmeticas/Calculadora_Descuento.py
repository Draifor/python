'''En una tienda se ofrece un descuento del 15% sobre el total 
de la compra y un cliente desea saber cuánto deberá pagar 
finalmente por su compra.'''
	# Inicio Programa
print("CALCULADORA DE DESCUENTOS")
	
    # Definición de variables
valCompra = 0 
desCompra = 0
totCompra = 0

    # Ingreso de datos
valCompra = int(input("Ingrese el valor de la compra: $"))

    #Ejecución de los cálculos
desCompra = valCompra * 0.15
totCompra = valCompra - desCompra

	#Mostrar resultados en pantalla
print("Valor de la compra: $", valCompra)
print("Descuento: $", desCompra)
print("El total a pagar a es: $", totCompra)