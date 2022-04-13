def main():
    '''Escriba un programa que pida una cantidad de segundos y que escriba 
    cuántas horas, minutos y segundos son.'''

    print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")

    seg_ini = int(input("Escriba una cantidad de segundos: "))
    
    seg_fin = seg_ini % 60
    min = (seg_ini // 60) % 60
    hor = seg_ini // 3600

    print(f"{seg_ini} segundos son {hor} horas, {min} minutos y {seg_fin} segundos")

if __name__ == "__main__":
    main()
