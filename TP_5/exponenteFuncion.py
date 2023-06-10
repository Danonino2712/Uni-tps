def potencia(base, exponente): 
    return base**exponente

#print(potencia(5, 4))

#test

def testPotencia(): 
    print('Testeando testPotencia()... ', end='')
    assert potencia(5, 4) == 625
    assert potencia(3, 2) == 9
    assert potencia(5, 2) == 25
    print("pasó!")



print(testPotencia())
