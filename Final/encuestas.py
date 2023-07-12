# A) escribir una funcion que permita al usuario cargar las encuestas en una lista, validando que los datos
# ingresados se encuentran entre 0 y 5 (no se ingresaran valores no numericos) y retorne la lista cargada.

def carga_encuestas():
    lista=[]
    for i in range (3):
        carga=int(input("ingrese un valor entre 0 y 5: "))
        while carga < 0 or carga >5:
            carga=int(input("ERROR, ingrese un valor entre 0 y 5: "))
        lista.append(carga)
    return lista
#carga_encuestas()

# B) escribir una funcion que reciba una la lista cargada en el punto (A) y retorne la opcion mas elegida 
# y la cantidad de votos que obtuvo.

def opcion_mas_votada(carga_encuestas):
    mayor=-1
    a,b,c,d,e,f= 0,0,0,0,0,0
    for i in range(len(carga_encuestas)):
        if carga_encuestas[i]==0:
            a+=1
        if carga_encuestas[i]==1:
            b+=1
        if carga_encuestas[i]==2:
            c+=1
        if carga_encuestas[i]==3:
            d+=1
        if carga_encuestas[i]==4:
            e+=1
        if carga_encuestas[i]==5:
            f+=1
        votos_cantidad=[a,b,c,d,e,f]
        
    for i in range(len(votos_cantidad)):
        if votos_cantidad[i]>mayor:
            mayor=votos_cantidad[i]
            indice_ganador=i
            if indice_ganador==0:
                indice_ganador="Malo"
            elif indice_ganador==1:
                indice_ganador="Regular"
            elif indice_ganador==2:
                indice_ganador="Bueno"
            elif indice_ganador==3:
                indice_ganador="Muy bueno"
            elif indice_ganador==4:
                indice_ganador="Excelente"
            elif indice_ganador==5:
                indice_ganador="Indeciso"
            ganador=(f"El ganador es '{indice_ganador}' con '{mayor}' votos")
            return ganador
carga=carga_encuestas()
opcion_mas_votada(carga)

# C) escribir una funcion que muestre por pantalla el porcentaje de votos obtenidos por cada opcion.