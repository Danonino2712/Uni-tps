numero1 = int(input("Coloque primer numero: "))
numero2 = int(input("Coloque segundo numero: "))

if numero1 > numero2:
    print(f"El numero {numero1} es mayor que el numero {numero2}")
elif numero1 < numero2:
    print(f"El numero {numero1} es menor que el numero {numero2}")
else:
    print("Los numeros son iguales!")