'''Escribir un programa que permita procesar datos de pasajeros de viaje en una lista 
de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo:
[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), 
("Rosa Ortíz", 15123978, "Glasgow"), ("Luciana Hernandez", 3898174, "Lisboa")]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que 
pertenecen. Ejemplo: 
[("Buenos Aires", "Argentina"), ("Gasglow", "Escocia"), ("Lisboa", "Portugal"), 
("Liverpool", "Inglaterra"), ("Madrid", "España")]

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de países.
- Dado el DNI de un pasajero, ver a que ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.'''

# Inicio Programa
print("*************************")
print("REGISTRO DE PASAJEROS".center(25))

#Funciones
def addPassenger(passengers):
    # Recibe una lista de pasajeros, agrega pasajeros a la lista y la retorna.
    while True:
        name = input("Nombre del pasajero (-x para salir): ")
        if name.lower() == "x":
            break
        dni = int(input("DNI: "))
        city = input("Ciudad de destino: ")
        passengers.append((name, dni, city))
    return passengers   

def addCity(countries):
    # Recibe una lista de países, agrega ciudades a la lista y la retorna.
    while True:
        city = input("Ciudad (-x para salir): ")
        if city.lower() == "x":
            break
        country = input("País: ")
        countries.append((city, country))
    return countries

def searchCity(passengers, dni):
    # Recibe una lista de pasajeros y el DNI de un pasajero, lo busca en la lista 
    # y retorna la ciudad a la que viaja. Si no lo encuentra, retorna el número 1.
    for person in passengers:
        if person[1] == dni:
            return person[2]
    return 1

def quantPassengCity(passengers, city):
    # Recibe una lista de pasajeros y una ciudad, busca la ciudad en la lista, 
    # cuenta las veces que se repite y retorna esa cantidad.
    count = 0
    for person in passengers:
        if person[2] == city:
            count += 1
    return count

def searchCountry(passengers, countries, dni):
    # Recibe una lista de pasajeros, una de países y el DNI de un pasajero. 
    # Retorna el país al que viaja ese pasajero. Si no se encuentra la ciudad 
    # retorna el número 1, si no se encuentra el país retorna el número 2.
    city = searchCity(passengers, dni)
    if city == 1:
        return 1
    else:
        for country in countries:
            if country[0] == city:
                return country[1]
        return 2

def quantPassengCountry(passengers, countries, country):
    # Recibe una lista de pasajeros, una de países y un país. Retorna la cantidad de 
    # pasajeros que viajan a ese país.
    count = 0
    for i in countries:
        if i[1] == country:
            for person in passengers:
                if person[2] == i[0]:
                    count += 1
    return count

# Variables
continue_ = True
opt = 0
name = ""
dni = 0
city = 0
quant = 0
count = 0
country = ""
passengers = []
countries = []
#Listas de prueba
#passengers = [("Luis", 1, "A"), ("Anastasio", 2, "B"), ("Petronio", 3, "C"), ("Jorge", 4, "D"), \
#             ("Andrea", 5, "B"), ("Jacinta", 6, "E")]
#countries = [("A", "Angola"), ("B", "Bielorrusia"), ("C", "Canadá"), ("D", "Dinamarca")]

# Menú
while continue_: 
    print("\n\n*************************")
    print("          MENÚ")
    print("*************************")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Consultar ciudad destino por DNI")
    print("4. Consultar cantidad de pasajeros por ciudad")
    print("5. Consultar país destino por DNI")
    print("6. Consultar cantidad de pasajeros por país")
    print("7. Salir")
    opt = int(input("¿Qué desea realizar?: "))
    
    # Acciones de acuerdo a la opción
    if opt == 1:
        addPassenger(passengers)
        print(passengers)

    elif opt == 2:
        addCity(countries)
        print(countries)

    elif opt == 3:
        dni = int(input("Ingrese el DNI a consultar: "))
        city = searchCity(passengers, dni)
        if city == 1:
           print(f"No se encontró el DNI '{dni}'")
        else:
            print("El pasajero viaja a ", city)
     
    elif opt == 4:
        city = input("Ingrese la ciudad a consultar: ")
        quant = quantPassengCity(passengers, city)
        print(quant, " pasajeros viajan a ", city)

    elif opt == 5:
       dni = int(input("Ingrese el DNI a consultar: "))
       country = searchCountry(passengers, countries, dni)
       if country == 1:
           print(f"No se encontró el DNI '{dni}'")
       elif country == 2:
           print("El país no está registrado")
       else: 
           print("El pasajero viaja a ", country)

    elif opt == 6:
        country = input("Ingrese el país a consultar: ")
        quant = quantPassengCountry(passengers, countries, country)
        print(quant, "pasajeros viajan a ", country)

    elif opt == 7:
        print("Fin del Programa")
        break 

# Fin Programa