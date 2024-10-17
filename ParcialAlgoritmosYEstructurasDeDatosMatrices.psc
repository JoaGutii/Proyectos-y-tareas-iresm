Algoritmo sin_titulo
    definir matriz, articulo, cantidad, buscar Como Caracter
    definir n, f Como Entero
    dimension matriz[5,2]
    articulo = ""
    cantidad = ""
    f = 1
    n = 0
    Escribir "Para ingresar un articulo -- 1."
    Escribir "Para buscar un articulo -- 2."
    Escribir "Para imprimir todos los artículos que fueron cargados previamente -- 3."
    Escribir "Terminar -- 4."
    leer n
    mientras n <> 4 Hacer
        si n = 1 Entonces
            si f <= 5 Entonces
                Escribir "Ingresar articulo: "
                leer articulo
                articulo = minusculas(articulo)
                matriz[f,1] = articulo
                Escribir "Ingresar cantidad: "
                leer cantidad
                matriz[f,2] = cantidad
                f = f + 1
            Sino
                Escribir "No se pueden ingresar más artículos."
            FinSi
        FinSi
        si n = 2 Entonces
            Escribir "Ingrese el articulo que desea buscar: "
            leer buscar
            buscar = minusculas(buscar)
            encontrado = Falso
            para f=1 hasta f-1 con paso 1 Hacer
                si matriz[f,1] = buscar Entonces
                    Escribir "Aquí está el artículo que buscabas: ", matriz[f,1], " y esta es su stock: ", matriz[f,2]
                    encontrado = Verdadero
                FinSi
            FinPara
            si no encontrado Entonces
                Escribir "Artículo no encontrado."
            FinSi
        FinSi
        si n = 3 Entonces
            Escribir "Artículos cargados:"
            para f=1 hasta f-1 con paso 1 Hacer
                Escribir "Artículo: ", matriz[f,1], " Cantidad: ", matriz[f,2]
            FinPara
        FinSi
        Escribir "Para ingresar un articulo -- 1."
        Escribir "Para buscar un articulo -- 2."
        Escribir "Para imprimir todos los artículos que fueron cargados previamente -- 3."
        Escribir "Terminar -- 4."
        leer n
    Fin Mientras
Fin Algoritmo
