#Ciclo interctivo

'''
def pcn(x):
    if x > 0:
        resultado = "El numero es positivo"
    elif x < 0:
        resultado = "El numero es negativo"
    else: 
        resultado = "El numero es 0"
    return resultado

#hago esto para automatizar a la hora de testear

def muchos_pcn():
    hay_mas_datos = "Si"
    while hay_mas_datos == "Si":
        x = int(input("Ingrese un numero: "))
        print(pcn(x))
        hay_mas_datos = input("¿Quiere seguir? <Si-No>: ")

#muchos_pcn()

def test_pcn():
    assert pcn(3) == "El numero es positivo"
    assert pcn(-10) == "El numero es negativo"
    assert pcn(0) == "El numero es 0"
    print("Se testeó exitosamente, pasó")

test_pcn()
'''

#Ciclo con centinela. Mas recomendado al ser mas automatico.
def pcn(x):
    if x > 0:
        resultado = "El numero es positivo"
    elif x < 0:
        resultado = "El numero es negativo"
    else: 
        resultado = "El numero es 0"
    return resultado

def leer_centinela(): #para evitar las lineas de codigo duplicadas, como pasaba antes en linea 47 y 51 con "centinela"
    return input("ingrese un numero: (ponga * para terminar) ")

def muchos_pcn():
    centinela = leer_centinela()
    while centinela != "*":
        x = int(centinela)
        print(pcn(x))
        centinela = leer_centinela()

muchos_pcn()