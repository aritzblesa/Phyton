import string
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
palabra = input ('ingrese una palabra: ').lower()
seguir = True
indice = 0
while ( (seguir) and (indice < len(palabra)) ) :
    if (palabra[indice]) in minusculas :
        pos = minusculas.index(palabra[indice])
        minusculas.pop(pos)
        indice += 1
    else:    
        seguir = False
print(seguir)