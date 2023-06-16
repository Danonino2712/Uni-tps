parical1 = int(input("Ingrese la nota de su primer parcial: "))
parcial2 = int(input("Ingrese la nota de su segundo parcial: "))

promedio = (parical1 + parcial2) / 2

if parical1 >= 4 and parcial2 >= 4:
    if promedio >= 8:
        print("Situación: Promovido")
    else:
        print("Situación: Regular")
else:
    print("Situación: Libre")