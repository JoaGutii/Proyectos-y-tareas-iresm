Algoritmo IngresarTabla
	//Elaborar un programa que informe la tabla de multiplicar de un numero ingresado por el usuario.
	definir i, matriz, n Como Entero
	dimension matriz[2*10]
	matriz[1*1] = 1; matriz[1*2] = 2; matriz[1*3] = 3; matriz[1*4] = 4; matriz[1*5] = 5; matriz[1*6] = 6; matriz[1*7] = 7; matriz[1*8] = 8; matriz[1*9] = 9; matriz[1*10] = 10
	para f=2 hasta 2 Hacer
		Escribir "Ingrese el numero que desee transformar en su tabla: "
		leer n
		para c=1 hasta 10 Hacer
			matriz[f*c] = n
			matriz[f*c] = c * n
			escribir matriz[f*c]
		FinPara
	FinPara
	
FinAlgoritmo
