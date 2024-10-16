Algoritmo sin_titulo
	//Elaborar un juego que permita al usuario ingresar un número. 
	//El programa buscará un numero al azar y comparará los mismos.
	//En caso de que sean iguales el usuario acertó por lo que tendrá 10 tiros mas.
	//En caso de que no sean iguales descontaremos un tiro.
	//El total de tiros al comienzo es de 5.
	//Deberemos comunicar cada acierto, desacierto y la cantidad de tiros.
	//Implementar un sistema de puntaje
	
	definir n, a, tiros Como Entero
	tiros = 5; puntos = 0; a = 0; desaciertos = 0
	mientras tiros <> 0 hacer
		a =  aleatorio (1,10)
		Escribir "Ingrese un numero del 1 al 10"
		leer n
		si n >= 1 y n <=10 entonces
			escribir "El numero secreto era: ", a
			si a = n Entonces
				escribir n, " Es correcto, has acertado el numero aleatorio!! +10 tiros + 1 punto"
				tiros = tiros + 10
				puntos = puntos + 1
			sino
				escribir n, " Es incorrecto!! ese no es el numero que buscas ;) "
				desaciertos = desaciertos + 1
				tiros = tiros - 1
			FinSi
			escribir "Tienes ", puntos, " puntos, ", desaciertos," desaciertos y un total de ", tiros, " tiros. "
		fin si
	fin mientras
	
	
	
	
	
	
FinAlgoritmo
