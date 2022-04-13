'''import time
print("Hola Mundo")
print(time.asctime(time.localtime()))
seconds = time.time()
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days /30
years = days / 365.25
decades = years / 10
print("Seconds : {} \nMinutes: {} \nHours: {} \nDays: {} \
    \nMonths: {} \nYears: {} \nDecades: {}"\
    .format(seconds, minutes, hours, days, months, years, decades))
inicio = time.time()
for i in range(5000):
    print(i, end = "-")
final = time.time()
print(f"\nHe tardado {round(final - inicio, 3)} segundos.")
'''
while True: 
    try:
        num = int(input("Escriba un número entero: "))
        break
    
    except ValueError:
        print("¡Ese no es un número entero!")
print(num)
