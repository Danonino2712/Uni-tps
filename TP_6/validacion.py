'''cadena = "Agus"
if cadena.isdigit():
    print("La cadena solo contiene dígitos numéricos")
elif cadena.isalpha():
    print("La cadena contiene caracteres alfabeticos")
else:
    print("Es alfanumerico")
'''

def validar_tipo(valor):
    if valor.isdigit():
        print("El valor es numérico.")
    elif valor.isalpha():
        print("El valor es una palabra.")
    else:
        print("El valor es alfanumérico.")

validar = "123"
print(validar_tipo(validar))
validar = "Agus"
print(validar_tipo(validar))
validar = "123Hola"
print(validar_tipo(validar))

'''def testValidar_tipo(): 
    print('Testeando testValidar()... ', end='')
    assert validar_tipo("3") == "El valor es numérico."
    assert validar_tipo("hola") == "El valor es una palabra."
    assert validar_tipo("hola123") == "El valor es alfanumérico."
    print("pasó!")

    print(testValidar_tipo())'''


    #aun no está correcto

#Con esta función simplemente puedes llamar a `validar_tipo()` y pasarle un parámetro. 
#La función determinará si el parámetro es numérico, una palabra o alfanumérico y devolverá un mensaje correspondiente.

#Por ejemplo, si pasas como parámetro `"123"`, la función devuelve `"El valor es numérico."`.
#  Si pasas `"hola"`, la función devuelve `"El valor es una palabra."`. Y si pasas `"hola123"`, 
# la función devuelve `"El valor es alfanumérico."`.

#valor.isdigit()
# Retorna True si todos los caracteres de valor son numéricos, False en caso contrario.
#valor.isalpha()
# Retorna True si todos los caracteres de valor son alfabéticos (no
# numéricos), False en caso contrario.
#valor.isalnum()
# Retorna True si valor es una combinación alfanumérica (caracteres y
# números), False en caso contrario.