'''Escriba un programa que pida una temperatura en grados Fahrenheit y 
que escriba esa temperatura en grados Celsius.
Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) 
es la siguiente: C = (F - 32) / 1,8'''

# Inicio Programa
print("CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS")

fahren = float(input("Escriba una temperatura en grados Fahrenheit: "))
celsius = (fahren - 32) / 1.8

print(fahren, f"ºF son {round(celsius, 1)} ºC")
