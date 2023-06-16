palabras = []
palabra = input("Ingresa una palabra: ")

while palabra != "parar":
    palabras.append(palabra)
    palabra = input("Ingresa otra palabra (o escribe 'parar' para detener el programa): ")

print("Estas son las palabras que ingresaste:")
for palabra in palabras:
    print(palabra)

print("--- TERMINADO ---")