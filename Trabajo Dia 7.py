


import os 
lista1 = ("Lionel", "Messi", 130000)
lista2 = ("Cristiano", "Ronado", 150000)
lista3 = ("Emiliano", "Martinez", 100000)
lista4 = ("Cristian", "Romero", 90000)
mi_diccionario = {40033029 : lista1, 50043076 : lista2, 60032054 : lista3, 20018083 : lista4}

print("Bienvenido a Galicia tu banco de confianza!!! \n")

print("(Numeros de cuenta para usar: 40033029, 50043076, 60032054, 20018083)")

numero_cuenta =int(input("Ingrese su numero de cuenta: "))

if numero_cuenta in mi_diccionario:
    datos_persona = mi_diccionario[numero_cuenta]
    nombre_persona = datos_persona[0]
    apellido_persona = datos_persona[1]
    balance = datos_persona[2]

    class Persona():
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido

    mi_persona = Persona(nombre_persona, apellido_persona)

    class Cliente(Persona):
        
        def __init__(self, numero_de_cuenta, balance):
            self.numero_de_cuenta = numero_de_cuenta
            self.balance = balance

        def __str__(self):
            return (f"Bienvenido {mi_persona.nombre} {mi_persona.apellido}. Tu saldo es de ${mi_cliente.balance}")
        
        def depositar(self):
            cantidad_ingresada = float(input("Ingrese la cantidad de dinero que depositara: "))
            if cantidad_ingresada < 0:
                print("No se pueden ingresar cantidades negativas. ")
            else:    
                mi_cliente.balance = mi_cliente.balance + cantidad_ingresada
                return (f"Tu saldo actual es de {mi_cliente.balance}")

        def retirar(self):
            cantidad_retirada = float(input("Ingrese la cantidad de dinero que retirara: "))
            
            if cantidad_retirada > mi_cliente.balance:
                print("No se puede retirar mas de lo que se tiene de saldo.")
            elif cantidad_retirada < 0:
                print("No se pueden realizar retiros negativos.")
            else:
                mi_cliente.balance = mi_cliente.balance - cantidad_retirada
                return (f"Tu saldo actual es de {mi_cliente.balance}")

        def mostrar_balance(self):
            return (f"Tu saldo es de ${mi_cliente.balance}") 

    mi_cliente = Cliente(numero_cuenta, balance)
    print("")
    print(str(mi_cliente))
    print("")

    input("Ingrese cualquier botos/tacla para continuar: ")

    bucle = True

    while bucle == True:
        os.system('cls')
        print(f"""

            {mi_cliente.mostrar_balance()}

            Estas son las opciones disponibles, por favor eliga una de estas opciones:
            
            1. Depositar
            2. Retirar
            3. Salir
            """)

        bucle_respuesta = False

        respuesta = int(input("Ingrese su respuesta numerica: "))
        
        if respuesta == 1:
            mi_cliente.depositar()
            input("Ingrese cualquier botos/tacla para continuar: ")
        elif respuesta == 2:
            mi_cliente.retirar()
            input("Ingrese cualquier botos/tacla para continuar: ")
        elif respuesta == 3:
            print("")
            print("Adios!! que tengas un muy buen dia/tarde/noche!!!")
            bucle_respuesta = False
            bucle = False
        else: 
            print("Has ingresado un numero incorrecto. Vuelve a intentarlo.")
            input("Presiona Enter para continuar...")
        
else:
    print("Número de cuenta no encontrado.")
