# Uni-tps
Solo es una forma de guardar mis trabajos practicos. Aun estoy aprendiendo python y subo los avances

# 1) 
# Escribi un programa en python que permita realizar la carga en una lista y 
# el procesamiento posterior de 1000 encuestas a presidente de un pais imaginario, Argiropolis.
# las posibles respuestas estan codificadas en la encuesta por numeros enteros y son: "Partido Hacker" (0),
# "Partido Gamer" (1),"Partido de los programadores" (2),"Otro Partido" (3),"No va a ir a votar"(4),
# "Indeciso"(5). En resumen, el programa debera contener funciones que permitan procesar lo siguiente,
# ASI COMO LAS LLAMADAS NECESARIAS PARA SU EJECUCION EN EL PROGRAMA PRINCIPAL:

# # A)
# Escribir una funcion que permita al usuario cargas las encuestas en una lista, validando que los valores
# ingresados se encuentran entre 0 y 5 (no se ingresaran valores no numericos) y retorne la lista cargada.

def cargar_encuestas():
     encuestas = []
     for i in range (0,5):
             valor = int(input("Ingrese el valor de la encuesta (0-5): "))
             while valor<0 or valor>5:
                    valor = int(input("Su valor esta fuera de rango, vuelva a ingresar: "))
             encuestas.append(valor)
     return encuestas
#cargar_encuestas()

#---------------------------------------------------------------------#

# def punto_a():
#     votos=[]
#     for i in range(15):
#         ingreso=int(input("Ingresa tu voto entre [0-5]: "))
#         if ingreso in range(0,6):
#             votos.append(ingreso)
#         else:
#             while ingreso<0 or ingreso>5:
#                 print("Fuera de rango")
#                 ingreso=int(input("Ingresa tu voto entre [0-5]: "))
#             votos.append(ingreso)
#     return votos
# votos=punto_a()

# B)
# Escribir una funcion que reciba la lista cargada en el punto (A) y muestre en pantalla el nombre del partido 
# ganador y su cantidad de votos. si hubiese dos o mas partidos ganadores, debera mostrar en pantalla el mensaje
# el mensaje "empate". si no hubiese ningun ganador, ya que nadie quiere ir a votar, o todos son indecisos, la 
# funcion debera retornar -1.

def partidos (cargar_encuestas):
    mayor = -1
    mayor_2= 0
    partidos= [0,0,0,0,0,0]
    for votos in range(len(cargar_encuestas)):
        if cargar_encuestas[votos] == 0:
            partidos[0]+=1
        elif cargar_encuestas[votos] == 1:
            partidos[1]+=1
        elif cargar_encuestas[votos] == 2:
            partidos[2]+=1
        elif cargar_encuestas[votos] == 3:
            partidos[3]+=1
        elif cargar_encuestas[votos] == 4:
            partidos[4]+=1
        elif cargar_encuestas[votos] == 5:
            partidos[5]+=1
    if partidos[0] > partidos[1] and partidos[0] > partidos[2] and partidos[0] > partidos[3] and partidos[0] > partidos[4] and partidos[0] > partidos[5]:
        mayor=("Partido hacker es el ganador!")
    elif partidos[1] > partidos[0] and partidos[1] > partidos[2] and partidos[1] > partidos[3] and partidos[1] > partidos[4] and partidos[1] > partidos[5]:
        mayor=("Partido gamer es el ganador!")
    elif partidos[2] > partidos[0] and partidos[2] > partidos[1] and partidos[2] > partidos[3] and partidos[2] > partidos[4] and partidos[2] > partidos[5]:
        mayor=("Partido programadores es el ganador")
    elif partidos[3] > partidos[0] and partidos[3] > partidos[1] and partidos[3] > partidos[2] and partidos[3] > partidos[4] and partidos[3] > partidos[5]:
        mayor=("Otro partido!")
    elif partidos[4] > partidos[0] and partidos[4] > partidos[1] and partidos[4] > partidos[2] and partidos[4] > partidos[3] and partidos[4] > partidos[5]:
        mayor=("No fue a votar!")
        mayor_2= -1
    elif partidos[5] > partidos[0] and partidos[5] > partidos[1] and partidos[5] > partidos[2] and partidos[5] > partidos[3] and partidos[5] > partidos[4]:
        mayor=("indeciso!")
        mayor_2:-1
    else:
        mayor =("Empate!")
    print(mayor)
    return mayor_2
carga_va= cargar_encuestas()
partidos(carga_va)

#------------------------------------------------------------#

# def punto_b(votos):
#     a=0
#     b=0
#     c=0
#     d=0
#     e=0
#     f=0
#     for i in range(len(votos)):
#         if votos[i]==0:
#             a+=1
#         elif votos[i]==1:
#             b+=1
#         elif votos[i]==2:
#             c+=1
#         elif votos[i]==3:
#             d+=1
#         elif votos[i]==4:
#             e+=1
#         elif votos[i]==5:
#             f+=1
#     votos_cantidad=[a,b,c,d,e,f]
#     mayor=-1
#     for i in range(len(votos_cantidad)):
#         if votos_cantidad[i]>=mayor:
#             if votos_cantidad[i]==mayor:
#                 ganador="Empate"
#             elif votos_cantidad[i]>mayor:
#                 mayor=votos_cantidad[i]
#                 indice_ganador=i
#                 if indice_ganador==0:
#                     indice_ganador="Partido hackers"
#                 elif indice_ganador==1:
#                     indice_ganador="Partido gamers"
#                 elif indice_ganador==2:
#                     indice_ganador="Partido de los programadores"
#                 elif indice_ganador==3:
#                     indice_ganador="Otro partido"
#                 ganador=f"El ganador es '{indice_ganador}' con '{mayor}' votos"
#                 if indice_ganador==4 or indice_ganador==5:
#                         ganador=-1               
#     return ganador
# print(punto_b(votos))

# 2)
# Escriba una funcion que reciba un numero entero N (mayor que M), y una lista Z de enteros como parametros, y 
# retorne la sumatoria de los numeros de la lista Z que sean mayores que M, y menores o iguales que N.
# Por ejemplo M=2, N=5, Z=[6,2,-4,5,4] Retornara 9.

def sumatoria_entre_m_y_n(m, n, z):
    suma = 0
    for num in range (len(z)):
        if m < z[num] and z[num] <= n:
            suma += z[num]
    return suma
num=sumatoria_entre_m_y_n(2,5,[6,2,-4,5,4])
print(num)

# 3) 
# desarrolla la funcion de test para la consigna 2. esta funcion debera contar con 3 casos de prueba. explicar
#porque considera que esos casos de prueba que eligio son relevantes para probar la funcion.add()

def test_sumatoria():
    assert sumatoria_entre_m_y_n(2,5,[6,2,-4,5,4]) == 9
    assert sumatoria_entre_m_y_n(2,5,[6,2,-4,5,3]) == 8
    assert sumatoria_entre_m_y_n(2,5,[6,2,-4,5,2]) == 5
    print("paso!")
test_sumatoria()

