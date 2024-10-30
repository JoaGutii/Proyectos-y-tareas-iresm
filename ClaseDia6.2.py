# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

# Recuerda importar Path del módulo pathlib, y utilizar el método home()
from pathlib import Path

ruta_base = Path.home()

# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path

from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)

# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario

import os
from pathlib import Path

ruta = Path.home()
print(ruta)

mi_ruta = Path(ruta,'Desktop','Todas las clases','practicas_path.py')

print(mi_ruta)


nombre = input("Dime tu nombre : ")
edad = input("Dime tu edad : ")

os.system('cls')

print(nombre)
print(edad)


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

ruta = Path.home()
print(ruta)

def abrir_leer(archivo):
    
    with open(archivo, 'r') as archivo1:
        contenido = archivo1.read()
        
    return contenido 

contenido_archivo = abrir_leer('a.txt')
print(contenido_archivo)



# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobreescribir(archivo):
       
        with open('b.txt', 'w') as archivo:
            archivo.write('contenido eliminado')
            
            archivo_leer = open('b.txt', 'r')
            contenido = archivo_leer.read()
        return contenido
        
eliminar_contenido = sobreescribir('b.txt')
print(eliminar_contenido)

# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    
    with open('c.txt', 'a') as archivo:
         archivo.write('\nse ha registrado un error de ejecucion')
         archivo.close()
         archivo_leer = open('c.txt', 'r')
         contenido = archivo_leer.read()
         return contenido
contenido = registro_error('c.txt')
print(contenido)

