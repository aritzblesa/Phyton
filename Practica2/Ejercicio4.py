evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""
# Se separa el titulo del resumen, para analizarlos por separado
lista = evaluar.split("resumen")

# Se separan las palabras del titulo para contarlas, se le resta 1 ya que "titulo :" no cuenta
palabras_titulo=lista[0].split()
palabras_titulo = len(palabras_titulo)-1

print("Tiene como maximo 10 palabras el titulo?" , "Si" if palabras_titulo <=10 else "No")

# Separamos el articulo de "resumen:" en adelante y luego lo separamos en oraciones
lista = evaluar.split("resumen:")
for elem in lista :
     oraciones = elem.split(".")

# Inicializamos las variables de las distintas dificultades en 0
oraciones_faciles = 0
oraciones_aceptables = 0
oraciones_dificiles = 0
oraciones_muy_dificiles = 0

# Creamos una funcion que sume 1 dependiendo la dificultad de la oracion
def evaluar_cantidad(cant) :
    # Las ponemos como globales para que se pueda modificar su contenido fuera de la funcion
    global oraciones_aceptables, oraciones_dificiles, oraciones_faciles, oraciones_muy_dificiles
    if (cant<=12) :
        oraciones_faciles+=1
    elif(cant<=17) :
        oraciones_aceptables+=1
    elif(cant<=25) :
        oraciones_dificiles+=1
    else:
        oraciones_muy_dificiles+=1

# Recorremos nuestra lista de oraciones y las separamos en palabras para luego evaluar de que dificultad es cada una, usando nuestra funcion creada previamente
for elemento in oraciones :
    oracion = elemento.split()
    evaluar_cantidad(len(oracion))
    
print(f"Cantidad de oraciones faciles: {oraciones_faciles} \n Cantidad de oraciones aceptables: {oraciones_aceptables} \n Cantidad de oraciones dificiles: {oraciones_dificiles} \n cantidad de oraciones muy dificiles: {oraciones_muy_dificiles}")
     