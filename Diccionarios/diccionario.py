dic = {"libro": "Las aventuras del titin", "categoría": "Drama", "Autor": "Pepe", "fecha": "año 2000"}
print(f"El libro {dic['libro']}, cuyo autor es {dic['Autor']} se escribió en el {dic['fecha']} ")

dic["Precio"] = 5000 
print(dic)

del dic["fecha"]

print(dic)
