'''Las estructuras repetitivas nos facilitan la ejecución reiterada de un mismo bloque de
código; en el caso de las incondicionales, la cantidad de veces que se repite el bloque
será un número fijo. En Python, la instrucción for nos permite crear este tipo de
estructuras. Su sintaxis es la siguiente:

for [variable de iteración] in [elementos a repetir]:
[código a repetir]

En donde:
● for es una palabra reservada que utilizamos para indicar que vamos a repetir un
bloque de código.
● La variable de iteración tomará el valor actual de los elementos a repetir en
cada iteración del bucle.
● Los elementos a repetir son el conjunto de valores sobre el que haremos la
repeticiones.
● El código a repetir es el bloque de instrucciones que se ejecutará en cada
iteración del bucle.
Por ejemplo, para mostrar en pantalla los primeros 100 números enteros positivos,
comenzando desde 0, podríamos escribir:'''

for n in range(101):
    print(n)

for letra in "Hola":
    print(letra)

for nro in [1,2,3]:
    print(nro)

# Range(Stop)
#Range(start, stop, step) Tercero opcional

for nro in range(3): #se imprime hasta 2 aunque tenga un 3 (uno menos siempre)
    print(nro)

for nro in range(3,6): #inicia en el mismo que ponemos de primer parametro y termina uno antes del que ponemos de segundo.
    print(nro)

for nro in range(3,12,3): #saltea de 3 pasos, por eso: 3,6,9 ¿porque no 12? porque siempre es uno menos del "stop", entonces no entra en esa "condicion"
    print(nro)