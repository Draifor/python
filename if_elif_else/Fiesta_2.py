#TERCER ENUNCIADO: 
'''Desarrollar un algoritmo que permita calcular los siguientes
datos de una fiesta:
¿Cuántas personas asistieron a la fiesta?
¿Cuántos hombres y cuantas mujeres?
• Promedio de edades por sexo.
• La edad de la persona más joven que asistió.
Consideraciones:
• No se permiten menores de edad a la fiesta.
• Ingresar datos hasta que se ingrese una edad igual a cero.'''

#Inicio Programa
print("ASISTENTES A LA FARRA")

#Variables
age = 1
sex = ""
males = 0
females = 0
ageMales = 0
ageFemales = 0
averageFemales = 0
averageMales = 0
ageMinor = 200

#Inicia la diversión
while age:

    age = int(input("¿Cuántos años tiene?: "))

    if age >= 18:

        if age < ageMinor:
            ageMinor = age
    
        sex = input("Hombre: M \nMujer: F: \n" )

        if sex.upper() == "M":
            males += 1
            ageMales += age

        elif sex.upper() == "F":
            females += 1
            ageFemales += age
        else:
            print("El dato no es válido")
        
    elif age < 18 and age > 0:
        print("¡No se permiten menores de edad en la farra!") 

#Fórmulas
assistants = males + females
averageMales = ageMales / males
averageFemales = ageFemales / females

#Imprimir Resultados
print("Asistieron ", assistants, "personas a la farra." )
print(males, " hombres.")
print(females, " mujeres.")
print("La edad promedio de hombres es ", averageMales)
print("La edad promedio de mujeres es ", averageFemales)
print("La persona más joven que asistió tiene: ", ageMinor)

#Fin Programa
