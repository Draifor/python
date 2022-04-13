'''Escriba un programa conversor de peniques a coronas, chelines y libras.

Se recuerda a los que no han leído a Guillermo el travieso que antes de la 
conversión al sistema decimal una libra eran 20 chelines, un chelín eran 
12 peniques y una corona eran 5 peniques.

CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES
Escriba la cantidad de peniques: 258
258 peniques son 1 libras, 1 chelines 1 coronas y 1 peniques.
CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES
Escriba la cantidad de peniques: 240
240 peniques son 1 libras, 0 chelines 0 coronas y 0 peniques.
CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES
Escriba la cantidad de peniques: 11
11 peniques son 0 libras, 0 chelines 2 coronas y 1 peniques.
CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES
Escriba la cantidad de peniques: 31
31 peniques son 0 libras, 2 chelines 1 coronas y 2 peniques.
'''

def main():
    
    print("CONVERTIDOR A LIBRAS, CHELINES; CORONAS Y PENIQUES")
    peniques = int(input("Escriba la cantidad de peniques: "))

    libra = peniques // 240
    chelin = (peniques // 12) % 20
    corona = (peniques % 12) // 5
    pequinesRestantes = (peniques % 12) % 5 
    
    print(f"{peniques} peniques son {libra} libras, {chelin} \
chelines {corona} coronas y {pequinesRestantes} peniques. ")

if __name__ == "__main__":
    main()
