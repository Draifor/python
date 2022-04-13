'''Escriba un programa que pida una cantidad y que escriba 
cuántas gruesas, docenas y unidades son.
Se recuerda que una gruesa son doce docenas.

Ayuda
CONVERTIDOR A GRUESAS Y DOCENAS
Escriba una cantidad (entera): 12345
12345 unidades son 85 gruesas, 8 docenas y 9 unidades
'''

def main():
    print("CONVERTIDOR A GRUESAS Y DOCENAS")
    cant = int(input("Escriba una cantidad (entera): "))
    gruesa = cant // 144
    docena = cant // 12 % 12
    unidad = cant % 12

    print(f"{cant} unidades son {gruesa} gruesas, {docena} docenas y {unidad} unidades")

if __name__ == "__main__":
     main()
