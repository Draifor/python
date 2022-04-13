'''Definir una función superposicion() que tome dos listas y devuelva True 
si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.'''

# Inicio Programa
def superposicion(lista1, lista2):

    for i in lista1:
        for ii in lista2:
            if i == ii:
                return True
    return False

# Prueba Función
centenario = list(range(1921, 2021))
añosNacimiento = []

año = int(input("En que año naciste?: "))
añosNacimiento.append(año)

print(superposicion(añosNacimiento, centenario))