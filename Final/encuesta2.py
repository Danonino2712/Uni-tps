def nuevalista(l):
    listanueva=[]
    for i in l:
        if i>0 and i<5:
            listanueva.append(i)
def mayor_opcion(l):
    lista_votos=[]
    malo=0
    regular=0
    bueno=0
    muy_bueno=0
    excelente=0
    indeciso=0
    for i in l:
        if i==0:
            malo+=1
        if i==1:
            regular+=1
        if i ==2:
            bueno+=1
        if i ==3:
            muy_bueno+=1
        if i ==4:
            excelente+=1
        if i==5:
            indeciso+=1
    if malo>regular and malo>bueno and malo>muy_bueno and malo>excelente and malo>indeciso:
        b=f"el juego es MALO, con {malo} votos"
    if regular>malo and regular>bueno and regular>muy_bueno and regular>excelente and regular>indeciso:
        b=f"el juego es REGULAR, con {regular} votos"
    if bueno>malo and bueno>regular and bueno>muy_bueno and bueno>excelente and bueno>indeciso:
        b=f"el juego es BUENO, con {bueno} votos"
    if muy_bueno>malo and muy_bueno>regular and muy_bueno>bueno and muy_bueno>excelente and muy_bueno>indeciso:
        b=f"el juego es MUY BUENO, con {muy_bueno} votos"
    if indeciso>malo and indeciso>regular and indeciso>bueno and indeciso>excelente and indeciso>muy_bueno:
        b=f"el resultado fue INDECISO, con {indeciso} votos"
    lista_votos.append(malo)
    lista_votos.append(regular)
    lista_votos.append(bueno)
    lista_votos.append(muy_bueno)
    lista_votos.append(excelente)
    lista_votos.append(indeciso)
    return b,lista_votos 
def porcentajes(l):
    lista_porcentajes=[]
    for i in l:
        a=(i*100)/8
        lista_porcentajes.append(a)
    print(lista_porcentajes)
def main():
    l=[1,4,5,2,0,3,10,3]
    l2=nuevalista(l)
    b,listavotos=mayor_opcion(l2)
    porcentajes(listavotos)
main()