#Determinar si un numero es par o impar

""" numero = int(input("Introduzca el numero: "))

if numero % 2 == 0: print("El numero es par")
else: print("El numero es impar") """

#Simular un cajero automatico, donde el usuario seleccione una
#operacion(deposito, retiro, o salir), el cajero iniciara con un
#saldo inicial de 20 bolivares, realizar las operaciones pertinentes
#Si el usuario introduce una opcion invalida, debe de indicarse
#con un error

saldo = 20
monto = 0

operacion = input(f"""
                  BIENVENIDO AL CAJERO BANCAMIGA
                  
                Su saldo actual es: {saldo} bolivares
                  Seleccione la opcion a realizar:
                  1) Deposito
                  2) Retiro
                  3) Salir
""").strip().lower()

if operacion == "deposito" or operacion == "1":
    monto = int(input("Introduzca el monto a depositar"))
    saldo+= monto
    print(f"Su saldo ahora es: {saldo}")

elif operacion == "retiro"  or operacion == "2":
    monto = int(input("Introduzca el monto a retirar"))
    if monto > saldo:
        print("No se vista que no va para el baile, esta pelando bola")
    else:
        saldo-=monto 
        print(f"Su saldo ahora es: {saldo}")
elif operacion == "salir"  or operacion == "3":
    print("Saliendo del programa")
    exit()
else:
    print("Operacion Incorrecta. Siga intentando. No hay sistema")