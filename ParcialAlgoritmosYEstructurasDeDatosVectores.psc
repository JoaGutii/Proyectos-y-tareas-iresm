Algoritmo ParcialAlgoritmosYEstructurasDeDatos
	definir i, vector, n, valor_ingresado Como Entero
	Escribir "Por favor ingrese la cantidad de numeros que va a utilizar. "
	leer n
	dimension vector[n]
	valor_ingresado = 0
	suma_todo = 0
	num_menor = 9999999999999
	num_mayor = n
	Para i = 1 hasta n con paso 1 Hacer
		Escribir "Ingrese un valor: "
		leer valor_ingresado
		vector[i] = valor_ingresado
	FinPara
	para i=1 hasta n con paso 1 hacer
		si vector[i]>num_mayor Entonces
			num_mayor = vector[i]
		FinSi
		si vector[i]<num_menor Entonces
			num_menor = vector[i]
		FinSi
	FinPara
	escribir "El numero mayor es: ", num_mayor
	escribir "El numero menor es: ", num_menor
	para i=1 hasta n con paso 1 Hacer
		si vector[i]>5 Entonces
			escribir vector[i] " Es mas grande que 5. "
		FinSi
	FinPara
	para i=1 hasta n con paso 1 Hacer
		suma_todo = suma_todo + vector[i]
	FinPara
	escribir "La suma del vector es de: ", suma_todo
FinAlgoritmo

