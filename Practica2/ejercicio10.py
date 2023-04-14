
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


# Inciso A 
def creacion_Diccionario(notas_1,notas_2,nombres):
    '''Genera y retorna un diccionario relacionando los nombres de los estudiantes con sus notas'''
    nombres_lista = nombres.split(",")
    dicc = {}
    i = 0
    todas = list(zip(notas_1,notas_2))
    for elem in nombres_lista :
        dicc[elem] = todas[i]
        i+=1
    return dicc

dicc=creacion_Diccionario(notas_1,notas_2,nombres)
print(f"Alumnos: {dicc}")


# Inciso B
def calcularpromedio_est(dicc):
    '''Calcula el promedio de cada alumno y lo devuelve en una estructura adecuada'''
    promedio_estudiante = {}
    for elem in dicc :
        promedio = sum(dicc[elem])
        promedio_estudiante[elem] = promedio / 2
    return promedio_estudiante

promedio_esudiante = calcularpromedio_est(dicc)
print(f" Promedios del curso : {promedio_esudiante}")


# Inciso C
def calcularpromedio_curso(promedio_estudiante):
    '''Calcula el promedio de todos los estudiantes del curso y lo retorna'''
    suma = 0
    for elem in promedio_esudiante.values() :
        suma  += elem
    promedio_curso = suma / len(promedio_esudiante)
    return promedio_curso

promedio_curso = calcularpromedio_curso(promedio_esudiante)
print(f" El promedio del curso es : {promedio_curso} ")


# Inciso D
def mejorpromedio(promedio_estudiante):
    '''Calcula e imprime al estudiante con mayor promedio y cual es ese promedio'''
    promedio_mas_alto = max(promedio_esudiante.values())
    for clave, valor in promedio_esudiante.items() :
        if valor == promedio_mas_alto :
         return print(f" El promedio mas alto es {promedio_mas_alto} y el estudiante el cual lo obtuvo fue {clave}")

mejorpromedio(promedio_esudiante)


# Inciso E 
def calcular_peor_nota(dicc) :
    '''Calcula la nota del peor estudiante y la imprime, junto a su nombre'''
    peor = min(dicc.values())
    for elem in dicc :
        if peor == dicc[elem]:
            peor_alu = elem
    print(f" La nota mas baja es {min(peor)} y el estudiante que la obtuvo fue {peor_alu}")
        
peor_nota =  calcular_peor_nota(dicc)
