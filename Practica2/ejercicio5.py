frase = input(" Ingrese una frase:" " ")
palabra = input( " Ingrese una palabra:" " ")
listaFrase = frase.split()
cant = 0
for elem in listaFrase:
    if palabra == elem :
        cant+=1

print(f" La cantidad de palabras iguales a {palabra} en la frase que usted ingreso es : {cant} " )