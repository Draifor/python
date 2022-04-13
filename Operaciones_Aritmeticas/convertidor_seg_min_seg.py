'''Escriba un programa que pida una cantidad de segundos y que escriba 
cuántos minutos y segundos son.'''

# Inicio Programa
print("CONVERTIDOR DE SEGUNDOS A MINUTOS")

seg = int(input("Escriba una cantidad de segundos: "))

min = seg // 60
seg_res = seg % 60

print(seg, f"segundos son {min} minutos y {seg_res} segundos")
