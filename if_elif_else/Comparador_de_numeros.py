 # if... elif... else... 
# EJERCICIO 6
'''Solicitar al usuario que ingrese dos números y mostrar cuál de los 
dos es menor. No considerar el caso en que ambos números son iguales.'''

print("COMPARADOR DE NUMEROS") 
n1 = 0
n2 = 0
rta = ""

n1 = int(input("Ingrese un número: ")) 
n2 = int(input("Ingrese otro número: ")) 

if n1 > n2:  
  rta = "El número menor es el " + str(n2)
else:
  rta = "El número menor es el " + str(n1)
 
print(rta)