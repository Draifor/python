'''Hacer un algoritmo en Python para un contador que permita almacenar, modificar 
y consultar el patrimonio de un cliente. El patrimonio se debe llevar dentro de 
una lista. Utilizar los métodos de las liustas vistos hasta ahora.'''

#Inicio Programa
print("CONTADOR PATRIMONIO")

#Variables
continuar = True
patrimonio = []
opc = 0
registro = ""
indice = 0

#Ingreso de datos
while continuar:
    print("*************************")
    print("MENÚ".center(23))
    print("*************************")
    print("1. Ingresar nuevo registro")
    print("2. Ubicar nuevo registro")
    print("3. Modificar registro")
    print("4. Contar registros")
    print("5. Buscar registro")
    print("6. Imprimir patrimonio")
    print("7. Salir")
    print("*************************")
    opc = int(input("¿Qué desea realizar?: "))

    if opc == 1: 
        registro = input("Ingrese el nuevo registro: ")
        registro = registro.title()
        patrimonio.append(registro)
        print(patrimonio)

    elif opc == 2:
        registro = input("Ingrese el nuevo registro: ")
        registro = registro.title()
        indice = int(input("Ingrese la pocisión donde desea ubicarlo: "))
        patrimonio.insert(indice - 1, registro)
        print(patrimonio)

    elif opc == 3:
        indice = int(input("Ingrese la pocisión del registro a modificar: "))
        registro = input("Ingrese el nuevo valor del registro: ")
        registro = registro.title()
        patrimonio[indice - 1] = registro
        print(patrimonio)

    elif opc == 4:
        registro = input("Ingrese el registro a contar: ")
        registro = registro.title()
        print("El registro '{}' está {} veces en la lista".format(registro, patrimonio.count(registro)))
        
    elif opc == 5:
        registro = input("Ingrese el registro a buscar: ")
        registro = registro.title()
        print("El registro '{}' está en la posición {}".format(registro, patrimonio.index(registro) + 1))
    
    elif opc == 6:
        print(patrimonio)
    
    elif opc == 7:
        continuar = False 
    
    else:
        print("Opción inválida")
    
    #Fin del Programa