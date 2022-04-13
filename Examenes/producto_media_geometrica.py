'''Escriba un programa que pregunte cuantos números se van a introducir, 
pida esos números (que puedan ser decimales y deben ser positivos) y 
calcule su producto y su media geométrica. El programa no necesita 
comprobar que los valores introducidos sean positivos.

Se recuerda que la media geométrica de n valores es la raíz n-ésima 
del producto de esos valores. La media geométrica se redondeará 
con un decimal'''

cant = int(input("¿Cuántos números quiere ingresar?: "))
if cant <= 0: 
    print("¡Imposible!")
else: 
    producto = 1
    for i in range(cant):
        n = float(input(f"Escriba el {i + 1} número: "))
        producto *= n

    medGeometrica = round(producto ** (1/cant), 1)

    print(f"El producto es {producto} y la media gemométrica es {medGeometrica}")
