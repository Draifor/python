'''Calcular la comisión de un vendedor de acuerdo con el
porcentaje de cumplimiento en cada una de las categorías,
como se muestra en la tabla correspondiente.'''

# Inicio Programa
print("CALCULAR COMISIÓN")




while True:
    # Variables
    lecheEsp = 0
    nutricionIndulg = 0
    cremasEsparc = 0
    lecheEnt = 0
    jugos = 0
    comLecheEsp = 0
    comNutricionIndulg = 0
    comCremasEsparc = 0
    comLecheEnt = 0
    comJugos = 0
    comTotal = 0

    # Ingreso de datos
    print("Ingrese los porcentajes de cumplimiento:")

    # Leche Especializada
    lecheEsp = int(input("Leche Especializada: "))
    if lecheEsp in range(0, 93):
        print("¡Gracias por venir a trabajar!")
    elif lecheEsp == 93:
        comLecheEsp = 171825
    elif lecheEsp == 94:
        comLecheEsp = 178350
    elif lecheEsp == 95:
        comLecheEsp = 184875
    elif lecheEsp == 96:
        comLecheEsp = 191400
    elif lecheEsp == 97:
        comLecheEsp = 197925
    elif lecheEsp == 98:
        comLecheEsp = 204450
    elif lecheEsp == 99:
        comLecheEsp = 210975
    elif lecheEsp == 100:
        comLecheEsp = 217500
    elif lecheEsp == 101:
        comLecheEsp = 228375
    elif lecheEsp == 102:
        comLecheEsp = 239250
    elif lecheEsp == 103:
        comLecheEsp = 250125
    elif lecheEsp == 104:
        comLecheEsp = 261000
    elif lecheEsp == 105:
        comLecheEsp = 271875
    elif lecheEsp == 106:
        comLecheEsp = 282750
    elif lecheEsp == 107:
        comLecheEsp = 293625
    elif lecheEsp == 108:
        comLecheEsp = 304500
    elif lecheEsp == 109:
        comLecheEsp = 315375
    elif lecheEsp in range(110, 121):
        comLecheEsp = 326250
    elif lecheEsp > 120:
        print("Tan convencido, siga soñando!")
        comLecheEsp = 326250
    else:
        print("¡Los porcentajes no pueden ser negativos!")

    # Nutrición Indulgente
    nutricionIndulg = int(input("Nutrición Indulgente: "))
    if nutricionIndulg in range(0, 90):
        print("¡Gracias por venir a trabajar!")
    elif nutricionIndulg == 90:
        comNutricionIndulg = 116000
    elif nutricionIndulg == 91:
        comNutricionIndulg = 118900
    elif nutricionIndulg == 92:
        comNutricionIndulg = 121800
    elif nutricionIndulg == 93:
        comNutricionIndulg = 124700
    elif nutricionIndulg == 94:
        comNutricionIndulg = 127600
    elif nutricionIndulg == 95:
        comNutricionIndulg = 130500
    elif nutricionIndulg == 96:
        comNutricionIndulg = 133400
    elif nutricionIndulg == 97:
        comNutricionIndulg = 136300
    elif nutricionIndulg == 98:
        comNutricionIndulg = 139200
    elif nutricionIndulg == 99:
        comNutricionIndulg =142100
    elif nutricionIndulg == 100:
        comNutricionIndulg = 145000
    elif nutricionIndulg == 101:
        comNutricionIndulg = 159500
    elif nutricionIndulg == 102:
        comNutricionIndulg = 174000
    elif nutricionIndulg == 103:
        comNutricionIndulg = 188500
    elif nutricionIndulg == 104:
        comNutricionIndulg = 203000
    elif nutricionIndulg == 105:
        comNutricionIndulg = 217500
    elif nutricionIndulg == 106:
        comNutricionIndulg= 232000
    elif nutricionIndulg == 107:
        comNutricionIndulg = 246500
    elif nutricionIndulg == 108:
        comNutricionIndulg = 261000
    elif nutricionIndulg == 109:
        comNutricionIndulg = 275500
    elif nutricionIndulg in range(110, 121):
        comNutricionIndulg = 290000
    elif nutricionIndulg > 120:
        print("Tan convencido, siga soñando!")
        comNutricionIndulg = 290000
    else:
        print("¡Los porcentajes no pueden ser negativos!")

    # Cremas - Esparcibles
    cremasEsparc = int(input("Cremas - Esparcibles: "))
    if cremasEsparc in range(0, 90):
        print("¡Gracias por venir a trabajar!")
    elif cremasEsparc == 90:
        comCremasEsparc = 145000
    elif cremasEsparc == 91:
        comCremasEsparc = 148625
    elif cremasEsparc == 92:
        comCremasEsparc = 152250
    elif cremasEsparc == 93:
        comCremasEsparc = 155875
    elif cremasEsparc == 94:
        comCremasEsparc = 159500
    elif cremasEsparc == 95:
        comCremasEsparc = 163125
    elif cremasEsparc == 96:
        comCremasEsparc = 166750
    elif cremasEsparc == 97:
        comCremasEsparc = 170375
    elif cremasEsparc == 98:
        comCremasEsparc = 174000
    elif cremasEsparc == 99:
        comCremasEsparc =177625
    elif cremasEsparc == 100:
        comCremasEsparc = 181250
    elif cremasEsparc == 101:
        comCremasEsparc = 190313
    elif cremasEsparc == 102:
        comCremasEsparc = 199375
    elif cremasEsparc == 103:
        comCremasEsparc = 208438
    elif cremasEsparc == 104:
        comCremasEsparc = 217500
    elif cremasEsparc == 105:
        comCremasEsparc = 226563
    elif cremasEsparc == 106:
        comCremasEsparc= 235625
    elif cremasEsparc == 107:
        comCremasEsparc = 244688
    elif cremasEsparc == 108:
        comCremasEsparc = 253750
    elif cremasEsparc == 109:
        comCremasEsparc = 262813
    elif cremasEsparc in range(110, 121):
        comCremasEsparc = 271875
    elif cremasEsparc > 120:
        print("Tan convencido, siga soñando!")
        comCremasEsparc = 271875
    else:
        print("¡Los porcentajes no pueden ser negativos!")

     # Leche Entera
    lecheEnt = int(input("Leche Entera: "))
    if lecheEnt in range(0, 93):
        print("¡Gracias por venir a trabajar!")
    elif lecheEnt == 93:
        comLecheEnt = 114550
    elif lecheEnt == 94:
        comLecheEnt = 118900
    elif lecheEnt == 95:
        comLecheEnt = 123250
    elif lecheEnt == 96:
        comLecheEnt = 127600
    elif lecheEnt == 97:
        comLecheEnt = 131950
    elif lecheEnt == 98:
        comLecheEnt = 136300
    elif lecheEnt == 99:
        comLecheEnt = 140650
    elif lecheEnt == 100:
        comLecheEnt = 145000
    elif lecheEnt == 101:
        comLecheEnt = 152250
    elif lecheEnt == 102:
        comLecheEnt = 159500
    elif lecheEnt == 103:
        comLecheEnt = 166750
    elif lecheEnt == 104:
        comLecheEnt = 174000
    elif lecheEnt == 105:
        comLecheEnt = 181250
    elif lecheEnt == 106:
        comLecheEnt = 188500
    elif lecheEnt == 107:
        comLecheEnt = 195750
    elif lecheEnt == 108:
        comLecheEnt = 203000
    elif lecheEnt == 109:
        comLecheEnt = 210250
    elif lecheEnt in range(110, 121):
        comLecheEnt = 217500
    elif lecheEnt > 120:
        print("Tan convencido, siga soñando!")
        comLecheEnt = 217500
    else:
        print("¡Los porcentajes no pueden ser negativos!")

    # Jugos
    jugos = int(input("Jugos: "))
    if jugos in range(0, 90):
        print("¡Gracias por venir a trabajar!")
    elif jugos == 90:
        comJugos = 29000
    elif jugos == 91:
        comJugos = 29725
    elif jugos == 92:
        comJugos = 30450
    elif jugos == 93:
        comJugos = 31175
    elif jugos == 94:
        comJugos = 31900
    elif jugos == 95:
        comJugos = 32625
    elif jugos == 96:
        comJugos = 33350
    elif jugos == 97:
        comJugos = 34075
    elif jugos == 98:
        comJugos = 34800
    elif jugos == 99:
        comJugos = 35525
    elif jugos == 100:
        comJugos = 36250
    elif jugos == 101:
        comJugos = 39875
    elif jugos == 102:
        comJugos = 43500
    elif jugos == 103:
        comJugos = 47125
    elif jugos == 104:
        comJugos = 50750
    elif jugos == 105:
        comJugos = 54375
    elif jugos == 106:
        comJugos = 58000
    elif jugos == 107:
        comJugos = 61625
    elif jugos == 108:
        comJugos = 65250
    elif jugos == 109:
        comJugos = 68875
    elif jugos in range(110, 121):
        comJugos = 72500
    elif jugos > 120:
        print("Tan convencido, siga soñando!")
        comJugos = 72500
    else:
        print("¡Los porcentajes no pueden ser negativos!")

    comTotal = comLecheEsp + comNutricionIndulg + comCremasEsparc + \
               comLecheEnt + comJugos
    print( "************************" )
    print( "       COMISIONES" )
    print( "************************" )
    print( "Leche Especializada: {:,}".format(comLecheEsp).replace(",", "."))
    print( "************************" )
    print( "Nutrición Indulgente: {:,}".format(comNutricionIndulg).replace(",", "."))
    print( "************************" )
    print( "Cremas - Esparcibles: {:,}".format(comCremasEsparc).replace(",", "."))
    print( "************************" )
    print( "Leche Entera: {:,}".format(comLecheEnt).replace(",", "."))
    print( "************************" )
    print( "Jugos: {:,}".format(comJugos).replace(",", "."))
    print( "************************" )
    print( "COMISIÓN TOTAL: {:,}".format(comTotal).replace(",", "."))
    print( "************************" )
    print( "MUCHAS GRACIAS" )
    print( "************************" )
