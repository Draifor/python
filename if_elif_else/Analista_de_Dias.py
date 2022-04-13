# if... elif... else... 
# EJERCICIO 7
'''Requerir al usuario que ingrese un día de la semana e imprimir 
un mensaje si es lunes, otro mensaje diferente si es viernes, 
otro mensaje diferente si es sábado o domingo. Si el día ingresado 
no es ninguno de esos, imprimir otro mensaje'''
 
print("ANALISTA DE DIAS") 
dia = ""
mensaje = ""
 
dia = input("¿Que día es hoy? ") 
 
if dia == "lunes":
  mensaje = "¡Está iniciando la semana!"
elif dia == "viernes":
  mensaje = "¡Está acabando la semana!"
elif dia == "sabado" or dia == "domingo":
  mensaje = "!Es fin de semana!"
elif dia == "martes" or dia == "miercoles" or dia == "jueves":
  mensaje = "¡Es mitad semana!"
else:
  mensaje = "Ese no es un día de la semana!"
print(mensaje)