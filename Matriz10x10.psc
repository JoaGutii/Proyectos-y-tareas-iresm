Algoritmo Matriz10x10
	dimension matriz[10,10]
	definir contador, contador2, matriz Como Entero
	matriz[1,1] = 1*9
	contador = 10
	contador2 = 0
	para f=1 hasta 9 Hacer
		contador2 = 0
		contador = contador -1
		para c=1 hasta 10 hacer
			contador2 = contador2 +1
			matriz[f,c] = contador * contador2
			escribir matriz[f,c]
		FinPara
	FinPara

FinAlgoritmo