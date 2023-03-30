from collections import Counter
palabra = input ('ingrese una palabra: ').upper()
contador = Counter(palabra)
print(contador)
valor = 0
diccionario = {1: "A, E, I, O, U, L, N, R, S, T", 2: "D, G", 3: "B, C, M, P", 4: "F, H, V, W, Y", 5: "K", 8: "J, X", 10: "Z,Q"}
for elem in contador :
    if elem in diccionario[1] :
        valor += contador[elem] * 1
    elif elem in diccionario[2]:
        valor += contador[elem]* 2
    elif elem in diccionario[3]:
        valor += contador[elem]*3
    elif elem in diccionario[4]:
        valor += contador[elem]*4
    elif elem in diccionario[5]:
        valor += contador[elem]*5
    elif elem in diccionario[8]:
        valor += contador[elem]*8
    else:
        valor += contador[elem]*10

print(valor)


    