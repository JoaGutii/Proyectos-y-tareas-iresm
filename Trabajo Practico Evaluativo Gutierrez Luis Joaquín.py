
print("Hola!! Bienvenido, a continuacion vas a ingresar la cantidad de nombres que necesites, en el momento que desees dejar de ingresar numeros solo debes escribir la palabra fin, gracias! ")

nombres = []
contador = 0
while True:
    contador += 1
    nombre = input(f"Ingrese el {contador} nombre ('Fin' para terminar o 'Repetir' para ver los nombres ingresados): ").rstrip()

    nombre = nombre.lower()

    if nombre == "fin":
        break

    elif nombre == "repetir":
        print(nombres)
        contador -= 1

    elif nombre or nombre.isalpha() or nombre.isspace():
        nombres.append(nombre)

print("Perfecto!! ahora tendras un menu en el cual podras elejir la opcion que gustes, estas opciones brindan informacion especifica de los valores que ingresaste. ")

while True:
    desicion = input("Eligue entre las siguientes opciones: \n 1. Mostrar nombres ingresados. \n 2. Ordenar los nombres alfabeticamente. \n 3. Análisis de longitud de los nombres. \n 4. Contar vocales y consonantes \n 5. Contar palabras en cada nombre. \n 6. Inversión de los nombres. \n 7. Mostrar solo los nombres que empiezan con una letra en particular. \n 8. Buscar si un nombre está en la lista. \n 9. Contar cuántos nombres tienen más de 5 caracteres. \n 10. Convertir todos los nombres a mayúsculas o minúsculas. \n 11. Salir \n ingrese su respuesta aquí: ")

    desicion = int(desicion)

    if desicion == 1:
        for nombre in nombres:
            print(nombre)

    elif desicion == 2:
        nombres.sort()
        print("Nombres ordenados alfabéticamente:")
        for nombre in nombres:
            print(nombre)
    
    elif desicion == 3:
        nombre_corto = min(nombres, key=len)
        nombre_largo = max(nombres, key=len)
        print("Nombre mas corto: ", nombre_corto)
        print("Nombre mas largo: ", nombre_largo)

    elif desicion == 4:

        cantidad_letras = 0
        vocales = "aeiou"
        cantidad_vocales = 0
        cantidad_consonantes = 0
        
        
        for nombre in nombres:
                cantidad_letras = len(nombre)
                print(f"{nombre} Contiene {cantidad_letras} letras. ")

        for nombre in nombres:
            cantidad_letras = 0
            cantidad_letras = cantidad_letras + len(nombre)
            for letras in nombre:
                if letras in vocales:
                    cantidad_vocales +=1
                else: 
                    cantidad_consonantes += 1
                
        
        print(f"La cantidad de letras es de {cantidad_letras}, en el caso de las vocales {cantidad_vocales} y de las consonantes {cantidad_consonantes}. ")

    elif desicion == 5:
        for nombre in nombres:
            cantidad_nombres_persona = 1

            for espacio in nombre:
                if espacio == ' ':  
                    cantidad_nombres_persona += 1
                    
            print(f" {nombre} es un nombre compuesto por {cantidad_nombres_persona} nombres")

    elif desicion == 6:
       for nombre in nombres:
           print(nombre[::-1])

    elif desicion == 7:
        nombres_encontrados = []
        letra = input("Con que letra empiezan los nombres que buscas? ").strip().lower()

        for nombre in nombres:

            if nombre.startswith(letra):
                nombres_encontrados.append(nombre)
                
        for nombre in nombres_encontrados:
                    print(f"Se a encontrado el nombre {nombre}")
                    
    elif desicion == 8:
        nombre_a_buscar = input("Que nombre buscas? ").strip().lower()
        if nombre_a_buscar in [nombre for nombre in nombres]:
            print("El nombre que buscas se encuentra en la lista!!!")
                
        else:
            print("El nombre que buscas NO se encuentra en la lista!")           

    elif desicion == 9: 
        contador_nombres_mas_cinco = 0
        for nombre in nombres:
            cantidad_letras = len(nombre)
            if cantidad_letras >= 5:
                print(f"{nombre} tiene 5 o mas de 5 letras")
                contador_nombres_mas_cinco += 1
        print(f"La cantidad de nombres con mas de 5 letras es de {contador_nombres_mas_cinco}")

    elif desicion == 10:
        convertidor = input("Si quieres convertir los nombres en minúscula ingrese el valor: 1 \nSi quieres convertir los nombres en mayúscula ingrese el valor: 2 \n").lower().strip()
        convertidor = int(convertidor)

        for nombre in nombres:
            if convertidor == 1:
                print(nombre.lower())
            elif convertidor == 2:
                print(nombre.upper())
    
    elif desicion == 11:
        print("Gracias por participar de mi demostracion de manejo de análisis básicos de los nombres, manipulación avanzada de cadenas y cálculos específicos.")
        break
