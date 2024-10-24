def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    num_min = 0
    num_max = 0
    num_int = 0
    resta_1 = 0
    num_max = max(num1, num2, num3)
    num_min = min(num1, num2, num3)
    if suma > 15:
        print(max(num1, num2, num3))
    elif suma < 10:
        print(min(num1, num2, num3))
    else:
        resta_1 = suma - num_min
        num_int = resta_1 - num_max
       
        print(num_int)
    
devolver_distintos(5,2,4)

def palabras(palabra):
    letras = set(palabra)
    print(sorted(letras))

palabras("entretenido")

def doble0(*args):
    doble = False
    for arg in range(1, len(args)):
        if args[arg] == 0 and args[arg - 1] == 0:
            doble = True
    print(doble)

doble0(1,2,3,4,5,6,0,0,9)

def contar_primos(n):

    list_primos = []

    for numero in range(2, n + 1):
        if numero < 2:
            continue
        es_primo = True
        for numero_primo in range(2, int(numero**0.5) + 1):
            if numero % numero_primo == 0:
                es_primo = False
                break
        if es_primo:
            list_primos.append(numero)
            
    print(list_primos)

contar_primos(10)