'''num = int(input("Ingrese un número entero: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print(f"El factorial de {num} es: {factorial}")'''

#En este script, se le pide al usuario que ingrese un número entero utilizando la función `input`. 
# Luego, se inicializa la variable `factorial` en 1. A continuación, se utiliza un ciclo `for` con la 
# función `range` para multiplicar cada valor desde 1 hasta el número ingresado por el usuario. Finalmente,
#  se imprime el resultado utilizando `print`.

#El factorial es una función matemática que se utiliza para calcular el producto de todos
#los números enteros positivos desde 1 hasta un número entero positivo dado. Por ejemplo, el factorial de 5 
#(escrito como 5!) es igual a 5 x 4 x 3 x 2 x 1, lo que da como resultado 120. 
#El factorial se utiliza en matemáticas para resolver problemas de combinación y permutación, 
#así como en la teoría de probabilidades y en la estadística. También se utiliza en algoritmos y 
#programación para resolver problemas complejos.

#Ejercicio editado

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def testFactorial(): 
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(7) == 5040
    print("pasó!!!")

testFactorial()

