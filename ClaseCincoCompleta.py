# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:

# ,

# :

# %

# _

# #

# Utiliza el método lstrip(). Imprime el resultado en pantalla:

print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.



# Práctica Métodos y Ayuda 2
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

# el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.


# Práctica Métodos y Ayuda 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv) 
if conjuntos_aislados == True:
    print("Los sets forman conjuntos aislados")
else:
    print("Los sets NO forman conjuntos")
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento




# Funciones Propias

def mi_funcion():
    '''esta funcion se encarga de 
    imprimir un saludo en pantalla'''
    print("hola luciano")

mi_funcion()

def mi_funcion(nombre):
    """ esta funcion se encarga de 
    imprimir un saludo en pantalla"""
    print(f"hola {nombre}")

mi_funcion("luis")


# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

# Solo debes definir la función, no debes invocarla luego.
def FuncionSaludo():
    print("¡Hola mundo!")



# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

def Bienvenido(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

nombre_persona = "Joaquín"
Bienvenido(nombre_persona)

# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.


# Práctica Crear Funciones 3
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.
un_numero = 2
def cuadrado(un_numero):
    print(un_numero*un_numero)



# Return 

def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,200)
print(resultado)


# Práctica Return 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
num1 = 3
num2 = 2
total = 0
def potencia(num1, num2):
    total = num1 ** num2
    return total
potencia(num1, num2)




# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

# Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.


def usd_a_eur():
    calcu_euros = dolares*0.90
    print(int(calcu_euros))

dolares = 1000

usd_a_eur()
# Práctica Return 3
# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

# Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

def invertir_palabra():
    palabra_invertida = palabra [::-1]
    palabra_invertida_mayuscula = palabra_invertida.upper()
    print(palabra_invertida_mayuscula)
palabra="Python"

invertir_palabra()



def chequear_3_cifras(lista):
    lista_3_cifras =[]
    for n in lista:
        if n == range(100,1000):
            lista_3_cifras.append(n)
        else:
            continue
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)


# Práctica Funciones Dinámicas 1
# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

# No invoques la función, solo es necesario definirla.

def todos_positivos(lista_numeros):
    if lista_numeros > 0:
        True
    else:
        False
lista_numeros = [1,2,3,-4,-5]


# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista_numeros):
    sum(lista_numeros)
    print(lista_numeros)


# Práctica Funciones Dinámicas 3
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

resultado = cantidad_pares(lista_numeros)
print(f"La cantidad de números pares es: {resultado}")


precios_cafe = [("capuchino",1.5), ("Expresso",2.5), ("Moka",3.5)]

def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio_mayor
            cafe_mas_caro = cafe
        else:
            pass
    return(cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")

from random import shuffle

# lista inicial 
palitos = ['-','--','---','----']
# mezclar palitos 
def mezclar(lista):
    shuffle(lista)
    return lista

# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)
# Comprobar intento 
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Te toco el 8")
    else:
        print("Te has salvado ")
    
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)



# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dado

# La función debe retornar dos valores resultado, que

# Dicha función no debe requerir argumentos para func

# Proporciona el resultado de estos dos dados a una f

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buena

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una j

# Pistas: utiliza el método choice o randint de la bi

from random import *

def lanzar_dados():
    dado1= randint(1,6)
    dado2= randint(1,6)
    print(dado1, dado2)
    suma_dados = dado1 + dado2
    if suma_dados < 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buena suerte")
    else: 
        print(f"La suma de tus dados es {suma_dados}. Parece una j")

lanzar_dados()


# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

lista_numeros = [1,2,15,7,2]
def reducir_lista(lista_numeros):
    nueva_lista = []
    
    for numero in lista_numeros:
        if numero not in nueva_lista:
            nueva_lista.append(numero)

    if nueva_lista:
        nueva_lista.remove(max(lista_numeros))
    
    return nueva_lista
reducir_lista(lista_numeros)
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)

def promedio(lista_reducida): 
    suma_numeros = sum(lista_reducida)
    promedio_total = suma_numeros/len(lista_reducida)
    print(promedio_total)
    return promedio_total
promedio(lista_reducida)


# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

def lanzar_moneda():
    cara_cruz = randint(1, 2)
    if cara_cruz == 1: 
        cara_cruz = print("El resultado es cara. ")
    else:
        cara_cruz = print("El resultado es cruz. ")
    print(cara_cruz)
    return cara_cruz
lanzar_moneda()

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.



def mi_funcion( *args):
    return sum(args)

resultado = mi_funcion(1,2,40,50)
print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg * arg
    print(suma)

suma_cuadrados(1, 2, 3)

# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).



# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    sum1 = 0
    sum2 = 0
    for arg in args:
        if arg < 0:
            sum1 += arg * -1
        else:
            sum2 += arg
    suma_total = sum2 + sum1
    print(suma_total)
suma_absolutos(-2,2)

# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(argn, *args):
    suma = 0
    for arg in args:
        suma += arg
    print(f"{argn}, la suma de tus numeros es {suma}")
numeros_persona("joa", 1,2,3)



def suma  (**kwargs):
    total = 0
    for clave,valor  in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total



print(suma(a=1,b=2,c=3))


def test(num1,num2,*args,**kwargs):

    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]


test(20,10,100,200,300,400,a=1,b=2,c=3)


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)

resultado = cantidad_atributos(nombre="joaquin", edad=22, pais="Argentina")
print(resultado)

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    return print(kwargs.keys())
lista_atributos(nombre="joaquin", edad=22, pais="Argentina")

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for arg, valor in kwargs.items():
        print(f"{arg}: {valor}")
describir_persona("María", color_ojos="azules", color_pelo="rubio")