# if ... elif ... else ...
#EJERCICIO 2  
'''Consideremos un programa que pide la edad y en función del valor recibido 
da un mensaje diferente. Podemos distinguir, por ejemplo, tres situaciones:

si el valor es negativo, se trata de un error
si el valor está entre 0 y 17, se trata de un menor de edad
si el valor es superior o igual a 18, se trata de un mayor de edad'''

edad = int(input("Digite su edad: "))
if edad <0:
  print("¡Debe tener más de 0 años!")
elif edad >= 0 and edad <18:
  print("¡Es usted menor de edad!")
else:
  print("¡Es usted mayor de edad!")
