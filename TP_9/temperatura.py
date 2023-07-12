# Ingreso de temperatura en grados Celsius
temp_celsius = input("Ingrese una temperatura en grados Celsius entre -18 y 50: ")

# Validación del dato ingresado
while not temp_celsius.isdigit() or int(temp_celsius) < -18 or int(temp_celsius) > 50:
    print("El valor ingresado no es válido. Recuerde que debe ser un número entre -18 y 50.")
    temp_celsius = input("Ingrese una temperatura en grados Celsius entre -18 y 50: ")

# Conversión del valor ingresado a número entero
temp_celsius = int(temp_celsius)

# Impresión del resultado
print("La temperatura ingresada en grados Celsius es:", temp_celsius)