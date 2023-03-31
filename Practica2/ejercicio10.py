
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]



nombres = nombres.split()
dicc = {}
i = 0

# Inciso A 
for elem in nombres :
    if (i<len(notas_2)):
        tupla = (notas_1[i], notas_2[i])
        i+=1
        dicc[elem] = tupla
#print(dicc)

# Inciso B
promedio_estudiante = {}
for elem in dicc :
    promedio = sum(dicc[elem])
    promedio_estudiante[elem] = promedio / 2
#print(promedio_estudiante)

# Inciso C
suma = 0
for elem in promedio_estudiante :
    suma  += sum(dicc[elem])
promedio_curso = suma / len(promedio_estudiante)
#print(promedio_curso)

# Inciso D
promedio_mas_alto = max(promedio_estudiante.values())
for clave, valor in promedio_estudiante.items() :
    if valor == promedio_mas_alto :
         #print(f" El promedio mas alto es {promedio_mas_alto} y el estudiante el cual lo obtuvo fue {clave}")
         break

# Inciso E 
peor_nota = min(valor for tupla in dicc.values() for valor in tupla)
nombre_peor_nota = min_key = min(dicc, key=lambda k: dicc[k][1])
print(f" La peor nota es {peor_nota} y la obtuvo {nombre_peor_nota}")