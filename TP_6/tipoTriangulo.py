lado1 = int(input("Ingrese numero del lado1: "))
lado2 = int(input("Ingrese numero del lado2: "))
lado3 = int(input("Ingrese numero del lado3: "))

if lado1 == lado2 == lado3:
    print("Es un triángulo equilatero!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Es un triángulo isósceles!")
else:
    print("ES un triángulo escaleno")