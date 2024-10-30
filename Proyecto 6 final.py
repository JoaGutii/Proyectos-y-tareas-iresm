#opción 1 preguntar qué categoría elige (carnes, ensaladas, etc.), le va a preguntar qué receta quiere leer, y mostrar su contenido.
#opción 2 se le va a hacer elegir una categoría, pedir que escriba el nombre y el contenido de la nueva receta que quiere crear, archivo en el lugar correcto.
#opción 3 preguntar el nombre de la categoría que quiere crear y va a generar una carpeta nueva con ese nombre.
#opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va a eliminar
#opción 5, le va a preguntar qué categoría quiere eliminar
# Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
# repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se cumpla la condición de que la elección del usuario sea 6
#cada vez que el usuario vuelva al menú inicial, la consola limpie la pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con system para poder reiniciar la pantalla
# Básicamente esto es un programa a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base de datos.
# si prefieres, también puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en tu directorio raíz si no tienes ganas de crearlo tú mismo.

import os
from os import system
from pathlib import Path

lista_categoria = ['Carnes','Ensaladas','Pastas','Postres']

lista_recetas = {'1' : 'Entrecot al Malbec , Matambre a la Pizza', '2' : 'Ensalada Griega , Ensalada Mediterranea', '3' : 'Canelones de Espinaca , Ravioles de Ricotta', '4' : 'Compota de Manzana , Tarta de Frambuesa'}

base = os.getcwd()
print(base)
def categorias_recetas():
        return """
    Categorias:
    1. Carnes.
    2. Ensaladas.
    3. Pastas.
    4. Postres.
                  """

categorias = categorias_recetas()

def open_archivos(archivo, categoria):
    with open(f'Recetas/{categoria}/{archivo}.txt', 'r') as receta:
        return receta.read()

def agregar_receta(categoria, nueva_receta):
     with open(f'Recetas/{categoria}/{nueva_receta}.txt', 'a') as receta:
        return receta.write(nueva_receta)

print("Este es un catalogo de recetas de cocina, dada las siguientes opciones ingrese el numero adecuado para llevar a cavo la funcion que necesite.")

while True:
        
        print("""
    1. Elegir categoria, recetas para leer.
    2. Agregar receta en una categoria.
    3. Crear categoria.
    4. Elegir categoria y eliminar una receta de la misma.
    5. Eliminar categoria.
    6. Finalizar.
    """)
        respuesta = input("Ingrese la opcion que desee: ")
        if respuesta == '1':
            print("Elija la categoria")
            respuesta_opcion1 = input(categorias)
            if respuesta_opcion1 == '1':
                print("""
    1. Entrecot al Malbec.
    2. Matambre a la Pizza.
                     """)
                respuesta_opcion11 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion11 == '1': 
                    print(open_archivos('Entrecot al Malbec', 'Carnes'))
                elif respuesta_opcion11 == '2': 
                     print(open_archivos('Matambre a la Pizza', 'Carnes'))
            elif respuesta_opcion1 == '2':
                print("""
    1. Ensalada Griega.
    2. Ensalada Mediterranea.
                     """)
                respuesta_opcion12 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion12 == '1': 
                    print(open_archivos('Ensalada Griega', 'Ensaladas'))
                elif respuesta_opcion12 == '2': 
                    print(open_archivos('Ensalada Mediterranea', 'Ensaladas'))
            elif respuesta_opcion1 == '3':
                print("""
    1. Canelones de Espinaca.
    2. Ravioles de Ricotta.
                     """)
                respuesta_opcion13 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion13 == '1': 
                    print(open_archivos('Canelones de Espinaca', 'Pastas'))
                elif respuesta_opcion13 == '2': 
                     print(open_archivos('Ravioles de Ricotta', 'Pastas'))
            elif respuesta_opcion1 == '4':
                print("""
    1. Compota de Manzana.
    2. Tarta de Frambuesa.
                 """)
                respuesta_opcion14 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion14 == '1': 
                    print(open_archivos('Compota de Manzana', 'Postres'))
                elif respuesta_opcion14 == '2': 
                     print(open_archivos('Tarta de Frambuesa', 'Postres'))

        elif respuesta == '2':
            print("Elija la categoria: ")
            respuesta_opcion2 = input(categorias)
            if respuesta_opcion2 == '1':       
                nueva_receta = input('Ingrese el nombre de la nueva receta: ')
                agregar_receta('Carnes', nueva_receta)
                print(f"Receta '{nueva_receta}' agregada a la categoría Carnes.")
                contenido_nueva_receta = input(" Ingrese el contenido de la receta. ")
                with open(f'Recetas/Carnes/{nueva_receta}.txt', 'a') as cont_nueva_receta:
                    cont_nueva_receta.write(': ')
                    cont_nueva_receta.write(contenido_nueva_receta)
            elif respuesta_opcion2 == '2':
                nueva_receta = input('Ingrese el nombre de la nueva receta: ')
                agregar_receta('Ensaladas',nueva_receta)
                print(f"Receta '{nueva_receta}' agregada a la categoría Ensaladas.")
                contenido_nueva_receta = input(" Ingrese el contenido de la receta. ")
                with open(f'Recetas/Ensaladas/{nueva_receta}.txt', 'a') as cont_nueva_receta:
                    cont_nueva_receta.write(': ')
                    cont_nueva_receta.write(contenido_nueva_receta)
            elif respuesta_opcion2 == '3':
                nueva_receta = input('Ingrese el nombre de la nueva receta: ')
                agregar_receta('Pastas',nueva_receta)
                print(f"Receta '{nueva_receta}' agregada a la categoría Pastas.")
                contenido_nueva_receta = input(" Ingrese el contenido de la receta. ")
                with open(f'Recetas/Pastas/{nueva_receta}.txt', 'a') as cont_nueva_receta:
                    cont_nueva_receta.write(': ')
                    cont_nueva_receta.write(contenido_nueva_receta)
            elif respuesta_opcion2 == '4':
                nueva_receta = input('Ingrese el nombre de la nueva receta: ')
                agregar_receta('Postres',nueva_receta)
                print(f"Receta '{nueva_receta}' agregada a la categoría Postres.")
                contenido_nueva_receta = input(" Ingrese el contenido de la receta. ")
                with open(f'Recetas/Postres/{nueva_receta}.txt', 'a') as cont_nueva_receta:
                    cont_nueva_receta.write(': ')
                    cont_nueva_receta.write(contenido_nueva_receta)

        elif respuesta == '3':
            respuesta_opcion3 = input("Ingrese el nombre de la categoria que desea crear: ")
            ruta_categoria = f'Recetas/{respuesta_opcion3}'
            lista_categoria.append(respuesta_opcion3)
            os.makedirs(ruta_categoria)

        elif respuesta == '4':
            print("Elija la categoria")
            respuesta_opcion1 = input(categorias)


            if respuesta_opcion1 == '1':
                print("""
    Elige el archivo a eliminar: 
    1. Entrecot al Malbec.
    2. Matambre a la Pizza.
                     """)
                respuesta_opcion11 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion11 == '1': 
                    os.remove('Entrecot al Malbec.txt')
                elif respuesta_opcion11 == '2': 
                     os.remove('Matambre a la Pizza.txt')
            elif respuesta_opcion1 == '2':
                print("""
    Elige el archivo a eliminar: 
    1. Ensalada Griega.
    2. Ensalada Mediterranea.
                     """)
                respuesta_opcion12 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion12 == '1': 
                    os.remove('Ensalada Griega.txt')
                elif respuesta_opcion12 == '2': 
                    os.remove('Ensalada Mediterranea.txt')
            elif respuesta_opcion1 == '3':
                print("""
    Elige el archivo a eliminar: 
    1. Canelones de Espinaca.
    2. Ravioles de Ricotta.
                     """)
                respuesta_opcion13 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion13 == '1': 
                     os.remove('Canelones de Espinaca.txt')
                elif respuesta_opcion13 == '2': 
                     os.remove('Ravioles de Ricotta.txt')
            elif respuesta_opcion1 == '4':
                print("""
    Elige el archivo a eliminar: 
    1. Compota de Manzana.
    2. Tarta de Frambuesa.
                 """)
                respuesta_opcion14 = input("Ingrese la opcion que desee: ")
                if respuesta_opcion14 == '1': 
                     os.remove('Compota de Manzana.txt')
                elif respuesta_opcion14 == '2': 
                     os.remove('Tarta de Frambuesa.txt')

        elif respuesta == '5':
            print("La lista de categorias a eliminar es: ")
            print(", ".join(lista_categoria))
            print("")
            respuesta_opcion3 = input("Ingrese la categoria que desea eliminar: ")

            ruta_categoria = f'Recetas/{respuesta_opcion3}'
            os.rmdir(ruta_categoria) 
            lista_categoria.remove(respuesta_opcion3) 

        elif respuesta == '6':
            print("Gracias por utilizar nustro sistema de recetas, nos veremos pronto, adios!!!!")
            break

        cualquier_tecla = input("Cuando desee continuar pulse cualquier tecla. ")
        system('cls')
