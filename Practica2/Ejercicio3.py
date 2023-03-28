import string
jupyter_info = """  JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones."""
letra = input("Ingrese una letra" " " )
# Se itera hasta que no se ingrese correctamente una letra
while not(letra in string.ascii_letters):
    letra = input("Usted no ingreso una letra, vuelva a intentarlo" " ")
# Se transforma tanto la letra como el texto a minuscula para que no haya errores de compatibildad
letra=letra.lower()
jupyter_info=jupyter_info.lower()
print(f" Su letra es: {letra}")
# Se separa el texto en palabras
lista = jupyter_info.split()
# Se recorre el texto buscando palabras que empiecen por la letra ingresada por teclado, en caso de encontrarse, se imprime
for elem in lista:
    if elem.startswith(letra):
        print(elem)