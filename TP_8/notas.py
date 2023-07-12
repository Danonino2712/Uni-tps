'''notas = []
nota = int(input("Ingrese una nota de parcial (-1 para terminar): "))
while nota != -1:
    notas.append(nota)
    nota = int(input("Ingrese otra nota de parcial (-1 para terminar): "))

if len(notas) == 0:
    print("No se ingresaron notas.")
else:
    promedio = sum(notas) / len(notas) 
    print(f"El promedio de las notas ingresadas es: {promedio}")'''

suma_notas = 0
cantidad_notas = 0

nota = int(input("Ingrese una nota de parcial (-1 para terminar): "))

while nota != -1:
    suma_notas += nota
    cantidad_notas += 1
    nota = int(input("Ingrese otra nota de parcial (-1 para terminar): "))

if cantidad_notas > 0:
    promedio = suma_notas / cantidad_notas
    print("El promedio de las notas ingresadas es:", promedio)
else:
    print("No se ingresaron notas.")