Algoritmo CedulaNombres

	definir n como entero
	n = 10
	Dimension nombres[n]
	Dimension cedulas[n]
	Para i=1 hasta n con paso 1 Hacer
		Escribir "Ingrese el nombre ", i
		leer nombres[i]
		Escribir "Ingrese la cedula del alumno anterior: "
		leer cedulas[i]
	FinPara
	Escribir "Ingrese la cedula del alumno que busca: "
	leer cedula_nombre
	encontrar = Falso
	Para i=1 hasta 10-1 Hacer
		si cedula_nombre = cedulas[i] entonces
			nombre_encontrado = i
			Escribir nombre_encontrado
		FinSi
	FinPara
	Escribir "El nombre del alumno correspondiente a la cedula es ", nombres[nombre_encontrado]
	
FinAlgoritmo
