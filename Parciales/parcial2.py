def trabajadores(x):
    nombres=[]
    edades=[]
    gustavo=0
    pedro="No hay pedro "
    mayor=0
    for i in range(x):
        a=input("Ingrese el nombre:")
        b=int(input("Ingrese la edad:"))
        if a.lower()=="gustavo":
           gustavo+=1
        if a.lower()=="pedro":
           pedro="si hay un pedro" 
        if b>=mayor:
           mayor=b
        nombres.append(a)
        edades.append(b)
    return f"hay {gustavo} personas que se llaman Gustavo. {pedro}. {mayor} es la mayor edad."
print(trabajadores(2))
