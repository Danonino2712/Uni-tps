numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    
maximo = max(numeros)
posicionMax = numeros.index(maximo) + 1

minimo = min(numeros)
posicionMin = numeros.index(minimo) + 1

print(f"El mayor número ingresado es {maximo}, y lo ingresaste en la posición {posicionMax}")
print(f"El menor número ingresado es {minimo}, y lo ingresaste en la posición {posicionMin}")
