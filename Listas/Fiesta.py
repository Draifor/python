# TERCER ENUNCIADO:
'''Desarrollar un algoritmo que permita calcular los siguientes datos de 
una fiesta:
- ¿Cuántas personas asistieron a la fiesta?
- ¿Cuántos hombres y cuantas mujeres?
- Promedio de edades por sexo.
- La edad de la persona más joven que asistió.
Consideraciones:
• No se permiten menores de edad en la fiesta.
• Ingresar datos hasta que se ingrese una edad igual a cero.'''

# Inicio Programa
print("ASISTENTES A LA FARRA")

# Variables
age = 1              # Edad
sex = ""             # Sexo
ageSex = [0, ""]     # Lista con la edad y sexo de cada persona
people = []          # Lista que almacena las listas ageSex
ageMales = 0         # Acumulador de edades de los hombres
ageFemales = 0       # Acumuludador de edades de las mujeres
cantMales = 0        # Contador de hombres
cantFemales = 0      # Contador de mujeres
promMales = 0        # Promedio de hombres
promFemales = 0      # Promedio de mujeres
ageMinor = 0         # Edad menor

# Ingreso de datos
while age:
    age = int(input("¿Cuántos años tiene?: "))

# Asignación de cada edad y sexo a la lista ageSex y posteriormente a la lista people
    if age >= 18:
        ageSex[0] = age

        sex = input("Hombre: M \nMujer: F\n:")
        sex = sex.upper()

        if sex == "M":
            ageSex[1] = "M"
            people.append(ageSex[:])

        elif sex == "F":
            ageSex[1] = "F"
            people.append(ageSex[:])

        else:
            print("El dato no es válido")

    elif age < 18 and age > 0:
        print("¡No se permiten menores de edad en la farra!")

    elif not age:
        break

    else:
        print("El dato no es válido")

# Asignación de la edad de la primera persona
ageMinor = people[0][0]

# Recorrer la lista para contar los hombres y las mujeres
# con las respectivas edades
for i in people:

    if i[1] == "M":
        ageMales += i[0]
        cantMales += 1

    else:
        ageFemales += i[0]
        cantFemales += 1

    if ageMinor > i[0]:
        ageMinor = i[0]


promMales = ageMales // cantMales
promFemales = ageFemales // cantFemales


print("Asistieron {} personas a la farra.".format(len(people)))
print(cantMales, " hombres.")
print(cantFemales, " mujeres.")
print(f"La edad promedio de los hombres es {promMales} años")
print(f"La edad promedio de las mujeres es {promFemales} años")
print("La persona más joven que asistió tiene: ", ageMinor, " años")

# Fin del programa
print("FIN DEL PROGRAMA")
