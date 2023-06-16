'''Consigna 1:
Escriba una función en Python que permita almacenar en listas el título y la cantidad de visualizaciones de N videos de 
YouTube (donde N se recibe como parámetro). Por ejemplo, una entrada válida del programa 
sería “Manejo de Listas” para el título y 2500 para las visualizaciones.
Una vez procesados todos los videos, escribir otra función que permita devolver la siguiente información:
a)	El promedio de visualizaciones de los videos.
b)	Indicar (por sí o por no) si algún vídeo posee como título “Argentina Campeón 2022”.
c)	El título del vídeo con mayor cantidad de visualizaciones. En caso que haya más de un video que comparta 
la mayor cantidad de visualizaciones se solicita el último.
'''
def videos(n):
    vistas=[]
    titulos=[]
    for i in range (n):
        a=int(input("Ingrese la cantidad de visitas: "))
        b=input("Ingrese el titulo: ")
        vistas.append(a)
        titulos.append(b)
    return vistas,titulos
def proc(vistas,titulos):
    suma=0
    mayor=-1
    mayor_titulo=""
    argentina="No hay video de argentina"
    for i in range(len(titulos)):
        suma+= vistas[i]
        prom= suma/len(vistas)
        if titulos [i]=="Argentina campeon":
            argentina="Hay video de argentina"
        if vistas [i] >= mayor:
            mayor=vistas[i]
            mayor_titulo= titulos[i]
    return (f"El promedio de vistas es {prom}. {argentina}. El titulo con mayor vistas es {mayor_titulo}")
def main():
    s= int (input("Ingrese numero: "))
    vistas,titulos=videos(s)
    print(proc(vistas,titulos))
main()

#Consigna 2: ¿Cuál es la diferencia entre la instrucción for y la instrucción while?
# La diferencia es que en el for sabemos cuantas veces va a iterar el usuario en cambio en while no.

#Consigna 3:  ¿Cómo se utiliza y para qué sirve el operador módulo (4 % 3) en Python?
#El operador divide por el entero y me devuelve unicamente el resto de esa división

#Consigna 4 
# Desarrolle una función que dado un N mayor que 100 e informe los números entre 100 y N, que 
# siendo pares además son múltiplos de 5. La función además deberá retornar la cantidad 
# de números que cumplen con ese criterio.

def multiples_de_5_entre_100_y_n(n):
    contador = 0
    for numero in range(100, n+1):
        if numero % 2 == 0 and numero % 5 == 0:
            print(numero)
            contador += 1
    return contador

print(multiples_de_5_entre_100_y_n(10))