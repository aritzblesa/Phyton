texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

import string
minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
cant_min = 0
cant_may = 0
cant_carac = 0
lista = texto.split()
for elem in lista :
    if elem[0] in mayusculas :
        cant_may += 1
    elif elem[0] in minusculas :
        cant_min += 1
    else :
        cant_carac += 1
print (f"Cantidad palabras con mayuscula {cant_may} \n Cantidad de palabras con minusculas {cant_min} \n Cantidad de caracteres {cant_carac} \n Cantidad total de palabras {cant_may + cant_min}")
