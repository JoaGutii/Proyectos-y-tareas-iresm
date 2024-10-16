Algoritmo matriz4x2
	definir pago_diario, f, c como enteros
	Dimension matriz[4,2]

	matriz[1,2] = 56; matriz[2,2] = 64; matriz[3,2] = 80; matriz[4,2] = 48
	matriz[1,1] = 1; matriz[2,1] = 2; matriz[3,1] = 3; matriz[4,1] = 4

	para f = 1 hasta 4 Hacer
		escribir "Ingrese el numero de empleado: "
		leer empleado
		si empleado >= 1 y empleado <= 4 Entonces
			para c = 2 hasta 2 Hacer
				escribir ("Ingrese la cantidad de dias trabajados por el empleado ")
				leer dias
					si dias >= 0 y dias <= 6
						pago_diario = dias * matriz[f,2]
						Escribir ("Al empleado se le debe pagar: "), pago_diario
					FinSi
			FinPara
		sino
			Escribir "Numero de empleado equivocado"
		FinSi
	FinPara
FinAlgoritmo
