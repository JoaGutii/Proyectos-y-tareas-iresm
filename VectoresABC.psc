Algoritmo VectoresABC
	Definir n Como Entero
	Escribir "Ingrese el tamaño del vector: "
	Leer n
	Dimension A[n]
	Dimension B[n]
	Dimension c[n]
	Para i<-1 Hasta n Con Paso 1 Hacer
		Escribir "Ingrese el elemento numerico entero ", i
		leer A[i]
		si A[i]%2 = 1 entonces
			B[i] = A[i]
		FinSi
		si A[i]%3 = 0 Entonces
			C[i] = A[i]
		FinSi
	Fin para
	Escribir "Los numeros Impares son "
	para i=1 hasta n hacer
		si B[i]<>0
			escribir B[i]
			finsi
	FinPara
	Escribir "Los numeros multiplos de 3 son: "
	para i=1 hasta n hacer
		si C[i]<>0
			Escribir C[i]
		FinSi
	FinPara

	
FinAlgoritmo
