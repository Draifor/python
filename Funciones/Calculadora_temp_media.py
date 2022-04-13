'''Crear una función que calcule la temperatura media de un día a partir de la 
temperatura máxima y mínima. Crear un programa principal, que utilizando una 
función, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando
la media. El programa pedirá el número de días que se van a introducir.'''

def calTemMed (temMax, temMin):
  temMedia = (temMax + temMin)/2
  return temMedia

#Inicio Programa
print("CALCULAR TEMPERATURA MEDIA")

#Variables
numDias = 0
temMax = 0
temMin = 0
temMed = 0
acumTem = 0
temMedTotal = 0

#Ingreso de datos
numDias = int(input("¿Cuántos días va a registrar?: "))

if not numDias:
  print("¡Debe ingresar al menos 1 día!")

elif numDias < 0:
  print("¡Los días no son negativos!")

else:
  for i  in range(1, numDias + 1):
    temMax = int(input("Escriba la temperatura máxima: "))
    temMin = int(input("Escriba la temperatura mínima: "))
    temMed = calTemMed(temMax, temMin)
    acumTem += temMed
    print(f"El día {i}, la temperatura media es: {temMed}")

temMedTotal = acumTem / numDias

print(f"La temperatura media de los {numDias} días es: {temMedTotal}")
