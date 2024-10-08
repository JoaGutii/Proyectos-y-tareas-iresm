
#""""""""""""""""""""""""""""""""" Proyecto Dia 4 """""""""""""""""""""""""""""""""""#
from random import randint

nombre = input("Hola bienvenido a mi juego de adivinar el numero. Para comenzar te pedire que ingreses tu nombre: ")

print(f"perfecto {nombre}, el juego consiste en lo siguiente, pensare en un numero aleatorio del 1 al 100 y tu tendras 8 intentos para averiguar que numero es. Tranquilo te ayudare un poco a lo largo del juego para que puedas lograrlo, ok? A jugar!!!!!!")
numero_aleatorio = randint(1,100)

intentos = 8
numintentos = 0
numero = 0
for intento in range(1, intentos + 1):
        numintentos = numintentos +1
        numero = int(input(f"Intento {intento}: ¿Cuál es tu número? "))
        if numero < numero_aleatorio:
            print("Incorrecto!!! el numero que buscas es mayor ;) ")
        elif numero > numero_aleatorio:
            print("Incorrecto!!! el numero que buscas es menor ;) ")
        elif numero > 100:
            print("El numero ingresado no es valido, tiene que ser menor o igual a ´100´ y mayor a ´0´")
        elif numero == numero_aleatorio:
            print(f"Felicidades has ganado!!! El numero aleatorio era {numero_aleatorio} y lo has conseguido en {numintentos}")
            break
        else:
            print("Por favor, ingresa un número válido.")
else:
     print(f"Lo siento, {nombre}. No has adivinado el número. Era {numero_aleatorio}.")

