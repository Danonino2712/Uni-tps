notas = []
nota = int(input("Ingrese una nota de parcial (-1 para terminar): "))
while nota != -1:
    notas.append(nota)
    nota = int(input("Ingrese otra nota de parcial (-1 para terminar): "))

if len(notas) == 0:
    print("No se ingresaron notas.")
else:
    promedio = sum(notas) / len(notas) 
    print(f"El promedio de las notas ingresadas es: {promedio}")