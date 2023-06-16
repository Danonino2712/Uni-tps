#La estructura alternativa se utiliza para validar datos y 
# evitar errores en ejecuciones de código que pueden tener resultados no esperados.

#Aquí te muestro un ejemplo de cómo utilizar la estructura 
# alternativa para validar que el denominador no sea cero en una 
# función que realiza la división de dos números enteros:

def division(num1, num2):
    if num2 == 0:
        print("¡No se puede dividir por 0!")
    else:
        result = num1 / num2
        print("El resultado de la división es :", result)

#En este caso, la estructura `if` valida si el segundo parámetro (`num2`) es igual a cero. Si es así,
#  entonces se muestra el mensaje "¡No se puede dividir por 0!". De lo contrario, se calcula el resultado de la división 
# y se muestra en pantalla.

def testDivisión():
    print("testeando testDivisión... ", end="")
    assert division(9, 3) == 3
    assert division(25, 5) == 5
    assert division(5, 0) == "¡No se puede dividir por 0!"

    print(testDivisión())