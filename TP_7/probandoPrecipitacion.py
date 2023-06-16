precipitaciones = []

for i in range(5):
    precipitacion = int(input(f"Ingrese: "))
    precipitaciones.append(precipitacion)

    suma = sum(precipitaciones)
    cuanto = len(precipitaciones)

print(suma)
print(cuanto)