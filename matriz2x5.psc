Algoritmo matriz2x5
	//Solicitar a un usuario que ingrese valores para una matriz de 2 x 5 y determinar cual fué el numero mayor mediante una búsqueda.
	definir contador Como Entero
	
	dimension matriz[2,5]
	contador = -900000
	para f=1 hasta 2 Hacer
		para c=1 hasta 5 Hacer
			Escribir "Ingrese los valores de la matriz: "
			leer matriz[f,c]
			si matriz[f,c] > contador Entonces
				contador = matriz[f,c]
			FinSi
		FinPara
	FinPara
	Escribir("El numero mayor de la matriz es: "), contador
	
FinAlgoritmo

