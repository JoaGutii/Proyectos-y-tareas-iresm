texto=input("Porfavor ingrese un texto de la forma que prefiera: ")

print("Genial!!!! ahora te pedire que ingreses 3 letras y te mostrate que puedo hacer con ello ;)")

letra1=input("Ingrese la primer letra: ")
letra2=input("Ingrese la segunda letra: ")
letra3=input("Por ultimo necesito una tercer letra: ")

print("Perfecto, Gracias a mi super velocidad y a la informacion que me diste puedo decirte que: ")

texto=texto.lower()
letra1=letra1.lower()
letra2=letra2.lower()
letra3=letra3.lower()
mi_lista=[letra1, letra2, letra3]
mostrar1=texto.count(letra1)
mostrar2=texto.count(letra2)
mostrar3=texto.count(letra3)

print(f"Hay {mostrar1} letras {letra1}, tambien hay {mostrar2} letras {letra2} y por ultimo hay {mostrar3} letras {letra3}")
print("Eso solo fue el comienzo, ahora te mostrare mas!!")

lista_texto = list(texto.split())

print("El texto que me diste cuenta con", len(lista_texto), "palabras")

primer_letra = texto[0]
segunda_letra = texto[-1]
print(f"Ademas puedo decirte que el texto que ingresaste comienza con la letra {primer_letra} y termina con la letra {segunda_letra}")

lista_texto = " ".join(lista_texto[::-1])
print(f"Uno de mis ultimos tucos es poder invertir el orden del texto, ¿no me crees? pues mira ´{lista_texto}´")

boolean = "python" in texto
dic = {True : "La palabra python se encuentra en el texto", False : "La palabra python no se encuentra en el texto"}

print(dic[boolean])

print("Gracias por jugar, adios!!!!")
