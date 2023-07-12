edad = input("Ingrese su edad: ")
intentos = 0

while not (edad.isdigit() and 18 <= int(edad) <= 60):
    print("La edad ingresada no es válida.")
    edad = input("Ingrese su edad nuevamente: ")

print("¡La edad ingresada es válida!")