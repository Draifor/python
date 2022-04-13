'''Escriba un programa que pida una distancia en pies y pulgadas 
y que escriba esa distancia en centímetros.
Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.'''

# Inicio Programa
print("CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS")

pies = int(input("Escriba una cantidad de pies: "))
pulgadas = int(input("Escriba una cantidad de pulgadas: "))

cm = (pies*12 + pulgadas) * 2.54
print(f"{pies} pies y {pulgadas} pulgadas son {cm} cm")
