class Pajaro:
    pass

tucan = Pajaro()
hornero = Pajaro()

print(tucan)
print(type(tucan))
print(hornero)
print(type(hornero))

# Práctica Clases 1
# Crea una clase llamada Personaje y a continuación, crea un objeto a partir de ella, por ejemplo: harry_potter

class Personaje:
    pass

Harry_Potter = Personaje()

# Práctica Clases 2
# Crea una clase llamada Dinosaurio, y tres instancias a partir de ella: velociraptor, tiranosaurio_rex y braquiosaurio .

class Dinosaurio:
    pass

Velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()

# Práctica Clases 3
# Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: netflix, hbo_max, amazon_prime_video

class PlataformaStreaming():
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

#-----------------------------------------------------------------------------------
#Atributos

class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")


# Práctica Atributos 1
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

class casa():
    
    def __init__(self, color, cantidad_pisos):
        self.color=color
        self.cantidad_pisos=cantidad_pisos
        
casa_blanca = casa("blanco", 4)

print(f"Mi casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")

# Práctica Atributos 2
# Crea una clase llamada Cubo, y asígnale el atributo de clase:

# caras = 6

# y el atributo de instancia:

# color

# Crea una instancia cubo_rojo, de dicho color.

class cubo():
    caras = 6
    def __init__(self, color):
        self.color = color
        
cubo_rojo = cubo("Rojo")


# Práctica Atributos 3
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

# real = False

# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

# especie = "Humano"

# magico = True

# edad = 17

class personaje():
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = personaje("humano", True, "17")
print(f"Harry Potter es {harry_potter.especie}, es magico? {harry_potter.magico}, woow y solo tiene {harry_potter.edad} años")

#---------------------------------------------------------------------------------------

#metodos


class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio')
    
    def volar(self, metros):
        print(f"El pajaro {self.especie} ha volado {metros} metros")
    
    


mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(500)



# Práctica Métodos 1
# Crea una clase Perro. Dicho perro debe poder ladrar.

# Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class perro():

    def ladrar(self):
        print("Guau")

mi_perro = perro()
mi_perro.ladrar()

# Práctica Métodos 2
# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class mago():

    def __init__(self, objeto):
        self.objeto = objeto
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
mi_mago = mago("merlin")

print(f"Adelante {mi_mago.objeto}!!!")
mi_mago.lanzar_hechizo()

# Práctica Métodos 3
# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class alarma():
    def __init__(self, cantidad_minutos):
        self.cantidad_minutos = cantidad_minutos

    def postergar(self):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
cantidad_minutos = input("¿Cuantos minutos vas a posponer la alarma? ")
mi_alarma = alarma(cantidad_minutos)

mi_alarma.postergar()

class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio')
    
    def volar(self, metros):
        print(f"El pajaro {self.especie} ha volado {metros} metros")
        self.piar()

    def pintar_pajaro(self):
        self.color="verde"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Poner {cantidad} huevos")
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira ")

mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(500)

mi_pajaro.alas =False
print(mi_pajaro.alas)

Pajaro.poner_huevos(2)
Pajaro.mirar()



# Práctica Tipos de Métodos 1
# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class mascota():
    def __init__(self):
        pass
        
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

mi_mascota = mascota()
mi_mascota.respirar()


# Práctica Tipos de Métodos 2
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.

class Jugador():
    vivo = False
    def __init__(self):
        pass
    def revivir(vivo):
        vivo = True
        print(vivo)
mi_jugador = Jugador()
mi_jugador.revivir()

# Práctica Tipos de Métodos 3
# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Jugador():
    def __init__(self, nombre, cantidad_flechas):
        self.nombre = nombre
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        
        self.cantidad_flechas -= 1
        print(f"{self.nombre} ha lanzado una flecha. Flechas restantes: {self.cantidad_flechas}")


mi_personaje = Jugador("Arquer", 5)
mi_personaje.lanzar_flecha()  
mi_personaje.lanzar_flecha()  
#-----------------------------------------------------------------------------------------
# herencia 


class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")
    

class Pajaro(Animal):
    pass



print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(2,"amarillo")
piolin.nacer()
print(piolin.edad)
print(piolin.color)



# Práctica Herencia 1
# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

mi_persona = Persona("Juan", 20)

class Alumno(Persona):
    pass

mi_alumno = Alumno("Pedro", 25)
print(mi_alumno.nombre)



# Práctica Herencia 2
# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos

class Mascota():
    def __init__(self, nombre, edad, cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas
class Perro2(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)

# Práctica Herencia 3
# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo():
    def acelerar(self):
        print("acelera")
    def frenar(self):
        print("Frena")
class Automovil(Vehiculo):
    pass
mi_auto = Automovil()
mi_auto.acelerar()
mi_auto.frenar()

#------------------------------------------------------------------------------
#Herencia extendida y multiple 





class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")
    

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo) -> None:
        self.edad = edad
        self.color = color
        self.altura_vuelo= altura_vuelo
    
    
    def hablar(self):
        print("Este animal hace pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros ")

   

print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(2,"amarillo",200)
piolin.nacer()
piolin.hablar()
print(piolin.edad)
print(piolin.color)



class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("ja ja")
    def hablar(self):
        print("que tal")




class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.reir()

mi_nieto.hablar()

print(Nieto.mro())



# Práctica Herencia Extendida 1
# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.

# Completa el código suministrado a continuación para lograrlo

class Padre():
    def reir(self):
        return print("JA JA JA")
mi_padre=Padre()
#mi_padre.reir()

class Madre():
    def __init__(self, vocacion):
        self.vocacion = vocacion
#mi_madre = Madre("Fiscalia")

class Hija(Padre, Madre):
    pass
mi_hija = Hija("Fiscalia")
mi_hija.reir()
print(mi_hija.vocacion)

# Práctica Herencia Extendida 2
# "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)

# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:

# - poner_huevos()

# - tiene_pico = True

# - vertebrado = True

# - venenoso = True

# - nadar()

# - caminar()

# - amamantar()


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave, Vertebrado):
    pass
mi_ornitorrinco = Ornitorrinco()
mi_ornitorrinco.caminar()
#...
#...
#...


# Práctica Herencia Extendida 3
# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"



# [1]: asegúrate de utilizar return seguido de una cadena de texto


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return print("Juego videojuegos en mi tiempo libre")
     
mi_hijo = Hijo()
mi_hijo.hobby()
    
#-----------------------------------------------------------------------------------


# POLIMORFISMO 

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + "Dice muuuuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + "Dice beee")


vaca1= Vaca("Lola")
oveja1 = Oveja("Nube")


vaca1.hablar()
oveja1.hablar()

animales = [vaca1,oveja1]

for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)
animal_habla(vaca1)



# Práctica Polimorfismo 1
# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

# Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

class Polimorfismo():
    def __init__(self, palabra, lista, tupla):
        self.palabra = palabra
        self.lista = lista
        self.tupla = tupla

    def __len__(self):
        return len(self.palabra) + len(self.lista) + len(self.tupla)

polimorfismo = Polimorfismo(palabra, lista, tupla)

for i in [polimorfismo.palabra, polimorfismo.lista, polimorfismo.tupla]:
    print(f"La longitud de {i} es: {len(i)}")



# Práctica Polimorfismo 2
# Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

# Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.


class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()

lista = [mi_mago, mi_arquero, mi_samurai]

for i in lista:
    i.atacar()

def i_atacar(i):
    i.atacar()

i_atacar(mi_arquero)
i_atacar(mi_mago)
i_atacar(mi_samurai)


# Práctica Polimorfismo 3
# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

# Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

import random 

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()


def personaje_defender(mago, arquero, samurai):
    lista_personajes = [mago, arquero, samurai]
    personaje_azar = random.choice(lista_personajes)
    return personaje_azar.defender()  

personaje_defender(mi_mago, mi_arquero, mi_samurai)
#--------------------------------------------------------------------------------------------------

class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD("Pink Floyd","The Wall",24)

print(mi_cd)



# Práctica Métodos Especiales 1
# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return(f'"{self.titulo}", de {self.autor}')

mi_libro = Libro("Hola", "yo", 10)

print(mi_libro)

# Práctica Métodos Especiales 2
# Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero


class Libro2():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)

mi_libro2 = Libro2("Hola", "yo", 10)

print(f"La cantidad de páginas del libro es: {len(mi_libro2)}")

# Práctica Métodos Especiales 3
# Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
    
mi_libro3 = Libro("Hola", "yo", 10)
print(mi_libro3)
