'''Existen varios algoritmos para calcular el día de la semana 
en que cae una fecha cualquiera. El que se utiliza en este ejercicio 
lo cuenta el danés Claus Tøndering en su web The Calendar FAQ.

Escriba un programa que calcule el día de la semana en que cae una 
fecha cualquiera posterior a 1582 (es decir, desde que se utiliza 
el calendario gregoriano) mediante el siguiente algoritmo:

A es el cociente de la división de 14 menos el mes entre 12,
B es el año menos A
C es el mes más doce veces A menos 2
D es el cociente de la división de B entre 4
E es el cociente de la división de B entre 100
F es el cociente de la división de B entre 400
G es el cociente de 31 veces C entre 12
H es el dia más B más D menos E más F más G
I es el resto de la división de H entre 7
Si I es 0, el día cae en Domingo; si I es 1, el día cae en Lunes; si I es 2, el día cae en Martes, etc
El programa no tiene por qué comprobar que se escribe una fecha correcta (más allá de que el año sea posterior a 1582)

CÁLCULO DEL DÍA DE LA SEMANA
Escriba el número de día: 15
Escriba el número de mes: 2
Escriba el número de año (a partir de 1583): 1564
¡Le he pedido un año posterior a 1582!
CÁLCULO DEL DÍA DE LA SEMANA
Escriba el número de día: 1
Escriba el número de mes: 1
Escriba el número de año (a partir de 1583): 1583
El día 1 del mes 1 de 1583 es sábado
CÁLCULO DEL DÍA DE LA SEMANA
Escriba el número de día: 24
Escriba el número de mes: 2
Escriba el número de año (a partir de 1583): 2017
El día 24 del mes 2 de 2017 es viernes
CÁLCULO DEL DÍA DE LA SEMANA
Escriba el número de día: 31
Escriba el número de mes: 7
Escriba el número de año (a partir de 1583): 1990
El día 31 del mes 7 de 1990 es martes
'''

def main():
    print("CÁLCULO DEL DÍA DE LA SEMANA")

    dia = int(input("Escriba el número del día: "))
    mes = int(input("Escriba el número del mes: "))
    año = int(input("Escriba el número del año (a partir de 1583): "))

    if año < 1583:
        print("¡Le he pedido un año posterior a 1582!")
    else:
        A = (14 - mes) // 12
        B = año - A
        C = mes + 12*A - 2
        D = B // 4
        E = B // 100
        F = B // 400
        G = (31 * C) // 12
        H = dia + B + D - E + F + G
        I = H % 7
        if I == 0: 
            dia_semana = "Domingo"
        elif I == 1:
            dia_semana = "Lunes"
        elif I == 2:
            dia_semana = "Martes"
        elif I == 3:
            dia_semana = "Miércoles"
        elif I == 4:
            dia_semana = "Jueves"
        elif I == 5:
            dia_semana = "Viernes"
        elif I == 6:
            dia_semana = "Sábado"
        else:
            dia_semana = "¿Qué pedo?"

        print(f"El día {dia} del mes {mes} del año {año} es {dia_semana}")

if __name__ == "__main__":
    main()
