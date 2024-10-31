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

diccionario_recetas = {1 : 'Entrecot al Malbec , Matambre a la Pizza', 2 : 'Ensalada Griega , Ensalada Mediterranea', 3 : 'Canelones de Espinaca , Ravioles de Ricotta', 4 : 'Compota de Manzana , Tarta de Frambuesa'}

base = os.getcwd()
print(base)

def categorias_recetas():
    return "\n".join(lista_categoria)
categorias = categorias_recetas()

def open_archivos(archivo, categoria):
    with open(f'Recetas/{categoria}/{archivo}.txt', 'r') as receta:
        return receta.read()

def agregar_receta(categoria, nueva_receta):
     with open(f'Recetas/{categoria}/{nueva_receta}.txt', 'a') as receta:
        return receta.write(nueva_receta)

def punto1(respuesta_opcion1):

    if respuesta_opcion1 in lista_categoria:
        print(diccionario_recetas[lista_categoria.index(respuesta_opcion1) + 1])
        receta = input("Ingrese el nombre de la receta que desea leer: ")
        print(open_archivos(receta, respuesta_opcion1))
    else:
        print("Opción no válida.")

def punto2(respuesta_opcion):
    a = 0
    nueva_receta = input('Ingrese el nombre de la nueva receta: ')
    agregar_receta(respuesta_opcion, nueva_receta)
    contenido_nueva_receta = input(" Ingrese el contenido de la receta. ")
    with open(f'Recetas/{respuesta_opcion}/{nueva_receta}.txt', 'a') as cont_nueva_receta:
        cont_nueva_receta.write(': ')
        cont_nueva_receta.write(contenido_nueva_receta)
    print(f"Receta '{nueva_receta}' agregada a la categoría Carnes.")
    if respuesta_opcion == "Carnes":
        a = 1
    elif respuesta_opcion == "Ensaladas":
        a = 2
    elif respuesta_opcion == "Pastas":
        a = 3
    elif respuesta_opcion == "Postres":
        a = 4
    diccionario_recetas[a] = diccionario_recetas[a] + " , " + nueva_receta
    return diccionario_recetas

def punto4(respuesta_opcion4):
    if respuesta_opcion4 in lista_categoria:
        print(diccionario_recetas[lista_categoria.index(respuesta_opcion4) + 1])
        receta = input("Ingrese el nombre de la receta que desea eliminar: ")
        os.remove(f'Recetas/{respuesta_opcion1}/{receta}.txt')
    else:
        print("Opción no válida.")

def mensaje1():
    return "Debe ingresar el nombre de la categoria tal cual como aparece arriba: "
mensaje = mensaje1()

print("Este es un catalogo de recetas de cocina, dada las siguientes opciones ingrese el numero adecuado para llevar a cavo la funcion que necesite.")

while True:
        
        print("""
    1. Elegir categoría para leer recetas.
    2. Agregar receta en una categoría.
    3. Crear categoría.
    4. Eliminar receta de una categoría.
    5. Eliminar categoría.
    6. Finalizar.
    """)
        respuesta = input("Ingrese la opcion que desee: ")
        print()
        contador = 0

        if respuesta == '1':
            print("Elija la categoria")
            
            while contador != 1:
                respuesta_opcion1 = input(f"{categorias}\n{mensaje} \nIngrese su respuesta: " )
                if respuesta_opcion1 in categorias:
                    punto1(respuesta_opcion1)
                    contador += 1
                else: 
                    print()
                    print("Ingresaste mal la categoria, vuelve a intentarlo: ")
                    print()


        elif respuesta == '2':
            print("Elija la categoria: ")
            while contador != 1:
                respuesta_opcion2 = input(f"{categorias}\n{mensaje} \nIngrese su respuesta: " )
                if respuesta_opcion2 in categorias:
                    punto2(respuesta_opcion2)
                    contador += 1
                else: 
                    print()
                    print("Ingresaste mal la categoria, vuelve a intentarlo: ")
                    print()

        elif respuesta == '3':
            respuesta_opcion3 = input("Ingrese el nombre de la categoria que desea crear: ")
            ruta_categoria = f'Recetas/{respuesta_opcion3}'
            lista_categoria.append(respuesta_opcion3)
            os.makedirs(ruta_categoria)


        elif respuesta == '4':
            print("Elija la categoria")
            while contador != 1:
                respuesta_opcion4 = input(f"{categorias}\n{mensaje} \nIngrese su respuesta: " )
                if respuesta_opcion4 in categorias:
                    punto4(respuesta_opcion4)
                    print(f"La receta a sido eliminada de la categoría Carnes.")
                    contador += 1
                else: 
                    print()
                    print("Ingresaste mal la categoria, vuelve a intentarlo: ")
                    print()


        elif respuesta == '5':
            print("La lista de categorias a eliminar es: ")
            print(", ".join(lista_categoria))
            print("")
            respuesta_opcion3 = input("Ingrese la categoria que desea eliminar tal cual como aparece arriba: ")

            ruta_categoria = f'Recetas/{respuesta_opcion3}'
            os.rmdir(ruta_categoria) 
            lista_categoria.remove(respuesta_opcion3) 

        elif respuesta == '6':
            print("Gracias por utilizar nustro sistema de recetas, nos veremos pronto, adios!!!!")
            break

        cualquier_tecla = input("Cuando desee continuar pulse cualquier tecla. ")
        system('cls')
