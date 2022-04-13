'''Escriba un programa que pida una temperatura en grados Celsius 
y que escriba esa temperatura en grados Fahrenheit.
Se recuerda que la relación entre grados Celsius (C) y grados 
Fahrenheit (F) es la siguiente: F = 1,8 * C + 32'''

# Inicio Programa
print("CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT")

celsius = float(input("Escriba una temperatura en grados Celsius: "))
fahren = 1.8 * celsius + 32

print(f"{celsius} ºC son {fahren} ºF")
