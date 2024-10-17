#Trabajo practico evaluativo de LABORATORIO ALGORITMOS Y ESTRUCTURAS DE DATOS 1 Alumno: Luis Joaquin Gutierrez

print("Hola!! Bienvenido, a continuacion vas a ingresar la cantidad de nombres que necesites, en el momento que desees dejar de ingresar numeros solo debes escribir la palabra fin, gracias! ")
nombres = []
contador = 0

while True:  #Ciclo while para poder ingresar nombres hasta que el usuario quiera
    contador += 1
    nombre = input(f"Ingrese el {contador} nombre ('Fin' para terminar o 'Repetir' para ver los nombres ingresados): ").rstrip() #Le pido al usuario que ingrese los nombres que este quiera agregar a la lista y utiizo el .strip() para poder eliminar espacios que queden al final

    nombre = nombre.lower()  #todo a minuscula

    if nombre == "fin":  #Si se ingresa fin rompemos el ciclo con break
        break

    elif nombre == "repetir": #Repetir para mostras la lista actual y que el contador no avance, se le suma 1 anteriormente y se lo resto para que no cuente
        print(nombres)
        contador -= 1

    elif nombre.replace(" ","").isalpha(): #Cumplir las condiciones de validacion para agregar a la lista
        nombres.append(nombre)

    else: # Si no agrega nada no cuenta el ingreso
        contador -= 1

print("Perfecto!! ahora tendras un menu en el cual podras elejir la opcion que gustes, estas opciones brindan informacion especifica de los valores que ingresaste. ")

while True:
    desicion = input("Eligue entre las siguientes opciones: \n 1. Mostrar nombres ingresados. \n 2. Ordenar los nombres alfabeticamente. \n 3. Análisis de longitud de los nombres. \n 4. Contar vocales y consonantes \n 5. Contar palabras en cada nombre. \n 6. Inversión de los nombres. \n 7. Mostrar solo los nombres que empiezan con una letra en particular. \n 8. Buscar si un nombre está en la lista. \n 9. Contar cuántos nombres tienen más de 5 caracteres. \n 10. Convertir todos los nombres a mayúsculas o minúsculas. \n 11. Salir \n ingrese su respuesta aquí: ")

    desicion = int(desicion) #Transformamos en entero para poder manipular

    if desicion == 1: #Imprimimos la lista en orden
        for nombre in nombres:
            print("Estos son los nombres de la lista: ")
            print(nombre)

    elif desicion == 2: #Con .sort ordenamos alfabeticamente
        nombres.sort()
        print("Nombres ordenados alfabéticamente:")
        for nombre in nombres: #Volvemos a imprimir
            print(nombre)
    
    elif desicion == 3:  #Key=len para medir el tamaño de los elementos de la lista
        nombre_corto = min(nombres, key=len)
        nombre_largo = max(nombres, key=len)
        print("Nombre mas corto: ", nombre_corto)
        print("Nombre mas largo: ", nombre_largo)

    elif desicion == 4: #Gracias a la variable vocales tomamos letra por letra de cada palabra de la lista para determinar si es o no una vocal

        cantidad_letras = 0
        vocales = "aeiou"
        cantidad_vocales = 0
        cantidad_consonantes = 0
        
        
        for nombre in nombres: #Conteo de letras sin espacios 
                cantidad_letras = len(nombre)
                for espacio in nombre:
                    if espacio == ' ':  
                        cantidad_letras -= 1
                print(f"{nombre} Contiene {cantidad_letras} letras. ")
    
        for nombre in nombres: #Conteo de vocales y consonantes sin espacios
            for letras in nombre:
                if letras in vocales:
                    cantidad_vocales +=1
                else: 
                    cantidad_consonantes += 1

        print(f"En el caso de las vocales {cantidad_vocales} y de las consonantes {cantidad_consonantes}. ")

    elif desicion == 5: #Por cada espacio que haya entre 2 nombres contaremos una palabra empezando desde 1
        for nombre in nombres:
            cantidad_nombres_persona = 1

            for espacio in nombre:
                if espacio == ' ':  
                    cantidad_nombres_persona += 1
                    
            print(f" {nombre} es un nombre compuesto por {cantidad_nombres_persona} nombres")

    elif desicion == 6: #Imprimimos todos los nombres al reves 
       for nombre in nombres:
            print("La inversion de los nombres es la siguiente: ")
            print(nombre[::-1])

    elif desicion == 7: #Encontraremos nombres con la funcion startswith y los agregamos a una lista nueva para imprimir
        nombres_encontrados = []
        letra = input("Con que letra empiezan los nombres que buscas? ").strip().lower() #

        for nombre in nombres:

            if nombre.startswith(letra):
                nombres_encontrados.append(nombre)
                
        for nombre in nombres_encontrados:
                    print(f"Se a encontrado el nombre {nombre}")
                    
    elif desicion == 8: #Buscaremos el nombre indicado en cada nombre de la lista nombres, para ello el nombre va a estar con el mismo formato siempre
        nombre_a_buscar = input("Que nombre buscas? ").strip().lower()
        if nombre_a_buscar in [nombre for nombre in nombres]:
            print("El nombre que buscas se encuentra en la lista!!!")
                
        else:
            print("El nombre que buscas NO se encuentra en la lista!")           

    elif desicion == 9: #Contamos las letras de los nombres con len y con un condicional presentamos la respuesta en caso de tener
        contador_nombres_mas_cinco = 0
        for nombre in nombres:
            cantidad_letras = len(nombre)
            if cantidad_letras >= 5:
                print(f"{nombre} tiene 5 o mas de 5 letras. ")
                contador_nombres_mas_cinco += 1
            else:
                print("No hay ningun nombre con 5 o mas letras. ")
        print(f"La cantidad de nombres con mas de 5 letras es de {contador_nombres_mas_cinco}")

    elif desicion == 10:#Le pedimos al usuario que ingrese la opcion que desea, luego con condicionales, utilizanco lower y upper, daremos la respuesta que eliga el usuario nombre por nombre1
        convertidor = input("Si quieres convertir los nombres en minúscula ingrese el valor: 1 \nSi quieres convertir los nombres en mayúscula ingrese el valor: 2 \n").lower().strip()
        convertidor = int(convertidor)

        for nombre in nombres:
            if convertidor == 1:
                print("Aqui tienes la lista de nombres en minuscula")
                print(nombre.lower())
            elif convertidor == 2:
                print("Aqui tienes la lista de nombres en mayuscula")
                print(nombre.upper())
    
    elif desicion == 11:#Opcion 11 termina el ciclo con un break
        print("Gracias por participar de mi demostracion de manejo de análisis básicos de los nombres, manipulación avanzada de cadenas y cálculos específicos.")
        break

    else:               #Los numeros ingresados deben estar dentro de las opciones
        print("Opcion no valida, por favor ingrese un numero que se precente entre las opciones. ")

