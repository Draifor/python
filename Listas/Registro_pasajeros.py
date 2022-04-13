'''Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
con la siguiente forma: (nombre, dni, destino). Ejemplo:
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

#Inicio Programa
print("*************************")
print("REGISTRO DE PASAJEROS".center(25))

#Variables
continue_ = True
noExist = True
count = 0
name = ""
dni = 0
city = ""
country = ""
passenger = ("", 0, "")
listPassenger = [("Luis", 12, "Florencia"), ("Alfredo", 34, "Cali"), ("Andrea", 56, "Bogotá"), ("Nathalia", 78, "Tokio")]
city_country = ("", "")
listCountry = [("Florencia", "Italia"), ("Cali", "Colombia"), ("Bogotá", "Colombia"), ("Tokio", "Japón")]
#Menú
while continue_:
    print("\n\n*************************")
    print("MENÚ".center(23))
    print("*************************")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Consultar ciudad destino mediante DNI")
    print("4. Consultar cantidad de pasajeros por ciudad")
    print("5. Consultar país destino mediante DNI")
    print("6. Consultar cantidad de pasajeros por país")
    print("7. Salir")
    print("*************************")
    opc = int(input("¿Qué desea realizar?: "))

    if opc == 1:
        while True:
            name = input("Ingrese el nombre del pasajero ('x' para salir): ")
            if name == "x":
                break
            dni = int(input("Ingrese el DNI del pasajero: "))
            city = input("Ingrese la ciudad de destino: ")
            passenger = (name, dni, city)
            listPassenger.append(passenger)
    
    elif opc == 2:
        city = input("Ingrese la ciudad: ")
        country = input("País al que pertenece: ")
        city_country = (city, country)
        listCountry.append(city_country)
        print("Ingreso exitoso: ", city_country)
    
    elif opc == 3:
        dni = int(input("Ingrese el DNI a consultar: "))
        for i in listPassenger:
            noExist = True
            if dni == i[1]:
                print(f"El pasajero {i[0]} viaja a {i[2]}")
                noExist = False
                break
        if noExist == True:
            print(f"No hay ningún pasajero con DNI: {dni}")

    elif opc == 4:
        count = 0
        city = input("Ingrese la ciudad: ")
        for i in listPassenger:
            if i[2] == city:
                count += 1
        print(f"{count} pasajeros viajan a {city}")

    elif opc == 5:
        dni = int(input("Ingrese el DNI a consultar: "))
        for i in listPassenger:
            noExist = True
            if i[1] == dni:
                city = i[2]
                noExist = False
                break
        if noExist:
            print("No hay ningún pasajero con DNI: {}".format(dni))
        
        else:
            for i in listCountry:
                noExist = True
                if i[0] == city:
                    print("El pasajero se dirige a {}".format(i[1]))
                    noExist = False
                    break
            if noExist:
                    print(f"La ciudad {city} no se encuentra registrada.")

    elif opc == 6:
        country = input("Ingrese el país a consultar: ")
        count = 0
        noExist = True
        for i in listCountry:
            if i[1] == country:
                for ii in listPassenger:
                    if ii[2] == i[0]:
                        count +=1
                noExist = False
        if not noExist:
            print("{} personas viajan a {}.".format(count, country))
        else:    
            print("El país '{}' no se encuentra registrado.".format(country))
        
    elif opc == 7:
        continue_ = False
            
    else:
        print("Opción inválida")
#Fin del Programa
print("FIN DEL PROGRAMA")