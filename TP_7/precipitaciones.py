precipitaciones = []

for i in range(7):
    precipitacion = float(input(f"Ingrese las precipitaciones del día {i+1}: "))
    precipitaciones.append(precipitacion)

# calcular el promedio de precipitaciones (sum: suma todos los elementos)
promedio = sum(precipitaciones) / len(precipitaciones)

mayor_precipitacion = max(precipitaciones)
dia_mayor_precipitacion = precipitaciones.index(mayor_precipitacion) + 1

print(f"El promedio de precipitaciones fue de {promedio} mls. diarios.")
print(f"El día de más precipitaciones fue el día {dia_mayor_precipitacion}.")