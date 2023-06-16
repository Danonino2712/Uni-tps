'''numero = input("Ingrese un numero: ")

def validoOno(numero):
    if numero.isdigit():
        numero = int(numero)
        if numero <= 0 or numero > 100:
            dato = "El numero ingresado está fuera del rango permitido"
        else:
            dato = f"El {numero} es valido. Gracias!"
    else:
        dato = "El dato ingresado no es numerico"
    return dato

validoOno(numero)

num = int(input("Ingrese un numero del 1 al 100: "))
while num < 1 or num > 100:
    num = int(input("El dato es invalido, intente nuevamente: "))
    if num >= 1 and num <= 100:
        print("Dato valido, gracias.")
print("Dato valido. Gracias")
'''

#convertir en funcion...
bandera = True
while bandera:
    num = input("ingrese un numero: ")
    if num.isdigit():
        dato = int(num)
        if dato <= 1 or dato > 100:
            print("Ingrese un numero entre 0 a 100")
        else:
            bandera = False
    else:
        print("No es un valor numero")
        
print(f"Tu numero {dato} es valido")

