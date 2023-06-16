for i in range(1, 11):
    num = int(input("Ingrese el número entero #" + str(i) + ": "))
    if num > 0:
        print(num, "es un número positivo.")
    elif num < 0:
        print(num, "es un número negativo.")
    else:
        print("El número es cero.")