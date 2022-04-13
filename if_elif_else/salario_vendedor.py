#PRIMER ENUCIADO: 
'''Desarrollar un algoritmo que calcule el salario neto que debe recibir
un vendedor de un almacén. Se debe tener en cuenta si tiene derecho o no al auxilio de
transporte. Para el desarrollo del ejercicio tenga en cuenta las siguientes formulas:
Sueldo devengado = salario básico * días laborados / 30.
Días laborados = debe ser entre 1 y 30.
Auxilio de Transporte: Lo reciben los empleados cuyo salario básico sea menor o igual
a 2 salarios mínimos legales vigentes.
Salario Mínimo Legal Vigente(2017): 737.717
Auxilio de Transporte = 83.140 * días laborados / 30 (año 2017 en Colombia).
Comisión de Ventas: En la empresa se tiene estipulado dar una comisión de ventas del
2% sobre las ventas del mes de cada vendedor.
Total devengado = sueldo devengado + comisión de ventas.
Total deducciones = descuentos por prestamos.
Salario Neto = Total devengado – Total deducciones
Como resultado del ejercicio se debe imprimir en pantalla lo siguiente:
Cedula empleado: XXXXXX
Nombre Empleado: XXXXXXX
Salario Básico: XXXXXX
Auxilio de Transporte: XXXXXX
Comisión de Ventas: XXXXXX
Préstamos: XXXXXX
Salario Neto a Recibir: XXXXX'''

#Inicio Programa
print("CALCULAR SALARIO NETO DEL VENDEDOR")

#Variables
nomEmpleado = ""
ceduEmpleado = 0
salBasico = 0
diasLaborados = 0
auxTransporte = 0
ventas = 0
comision = 0
suelDevengado = 0
totalDevengado = 0
prestamos = 0
salNeto = 0

#Constantes
salMinLegVigente = 737717

#Ingreso de datos
ceduEmpleado = int(input("Ingrese el número de cédula del vendedor: "))
nomEmpleado = input("Ingrese el nombre: ")
salBasico = int(input("Ingrese el salario básico: "))
ventas = int(input("Ventas del mes: "))
prestamos = int(input("Prestamos solicitados: "))
diasLaborados = int(input("Días laborados: "))

#No se como llamar las condiciones
if diasLaborados <= 0 or diasLaborados > 30:
    print("Los días laborales son mínimo 1, máximo 30.")

else: 
    if salBasico <= salMinLegVigente * 2:
          auxTransporte = 83140 * diasLaborados / 30

    #Fórmulas
    suelDevengado = salBasico * diasLaborados / 30
    comision = ventas * 0.02
    totalDevengado = suelDevengado + comision + auxTransporte
    salNeto = totalDevengado - prestamos

    print("---------------------------")
    print(f"Cédula Empleado: {ceduEmpleado}")
    print(f"Nombre Empleado: {nomEmpleado}")
    print(f"Salario Básico: {salBasico}")
    print(f"Auxilio de Transporte: {auxTransporte}")
    print(f"Comisión de ventas: {comision}")
    print(f"Préstamos: {prestamos}")
    print(f"Salario Neto a Recibir: {salNeto}")

