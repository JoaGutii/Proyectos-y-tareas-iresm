from random import *
def palabra_random(lista_palabras_random):
    palabra_oculta = choice(lista_palabras_random)
    return palabra_oculta

def guiones(mi_palabra_oculta):  
    return ["_"] * len(mi_palabra_oculta)

lista_palabras_random = [ "sol", "luna", "estrella", "nube", "mar", "montaña", "rio", "arbol", "flor", "viento", "cielo", "tierra", "fuego", "agua", "luz", "sombra", "hoja", "pajaro", "animal", "insecto", "nieve", "lluvia", "risa", "grito", "canto", "susurro", "recuerdo", "sueño", "esperanza", "amor", "amistad"]

lista_fallos = []
mi_palabra_oculta = palabra_random(lista_palabras_random)
cantidad_guiones = guiones(mi_palabra_oculta)

print("")
print("Hola bienvenidos al ahorcado, como ya saben es un juego que consta de encontrar letra por letra la palabra oculta, para conseguir esto tendran 6 vidas, se mostrara una serie de guiones que representaran la longitud de la palabra y seguido a esto se les permitira ingresar las letras. Estan listos?? Vamos a jugar!!")

cantidad_letras = len(mi_palabra_oculta)
print("")
print(f"La palabara que buscas tiene {cantidad_letras} letras. ")

print('''        --------|
                |
                o
               ´|´
               / \ ''')

print("Palabra oculta: ", " ".join(cantidad_guiones))

intentos = 6

while intentos > 0:
    letra_ingresada = input("Ingrese su primer intento aquí, por favor: ").lower()

    if letra_ingresada.isalpha() and len(letra_ingresada) == 1: 
        if letra_ingresada in mi_palabra_oculta:
            print(f"¡Es correcto! {letra_ingresada} se encuentra entre las letras que estás buscando.")
            for i, caracter in enumerate(mi_palabra_oculta):
                if letra_ingresada == caracter:
                    cantidad_guiones[i] = letra_ingresada
            print("Palabra oculta: ", " ".join(cantidad_guiones)) 
        else:
            print(f"Incorrecto! {letra_ingresada} no se encuentra en la palabra oculta.")
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
            lista_fallos.append(letra_ingresada)
            print("La lista de letras falladas es: "," ".join(lista_fallos))
    elif "_" not in cantidad_guiones:
        print("¡Felicidades! Has adivinado la palabra:", mi_palabra_oculta)
        break
    else:
        print("Debes ingresar una letra del abecedario y solo una letra.")
