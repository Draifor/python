'''Escriba un programa que pregunte cuántos números se van a introducir, 
pida esos números, y muestre un mensaje cada vez que un número no sea 
distinto al anterior.'''

cant = int(input("¿Cuántos números quiere ingresar?: "))
if cant < 0:
    print("¡Imposible!")
elif cant == 0:
    print("Debe ingresar al menos un número") 
else: 
    n1 = int(input("Escriba un número: "))
    for i in range(cant - 1):
        n2 = int(input(f"Escriba un número diferente de {n1}: "))
        if n2 == n1:
            print(n2, "no es diferente de", n1)
        n1 = n2

print("Gracias por su colaboración.")
