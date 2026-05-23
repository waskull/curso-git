#Elaborar un programa que calcule el monto por la estadia 
#de un vehiculo en un estacionamiento, el costo base por estar
#en el estacionamiento es 100bs.
#Si el vehiculo estuvo exactamente una hora, se debe de agregar
#un extra de 40bs
#Si el vehiculo estuvo entre 1 y 4 horas, se debe de pagar un extra
#de 100bs. 
#Si el vehiculo estuvo mas de 5 horas, entonces debera de pagar
#250bs.
#Cuando el conductor va a pagar el monto, tiene como opcion
#el pago en efectivo o pago movil. Si paga con efectivo 
#tendra un descuento del 10%. Con pago movil el descuento es 0%
#Calcular el monto total

monto = 100

horas = int(input("Introduce las horas del vehiculo en el estacioamiento"))

if horas < 0:
    print("Valor erroneo, saliendo del programa")
    exit()

if horas == 1:
    monto+=40

if horas>1 and horas < 5:
    monto+=100

if horas > 5:
    monto+= 250

tipo_pago = input("Introduce el tipo de pago. 1-Pago Movil, 2-Efectivo").strip().lower()

if tipo_pago == "1" or tipo_pago=="pago movil":
    print(f"El total a pagar es: {monto}")
elif tipo_pago == "2" or tipo_pago=="efectivo":
    monto = monto - (monto * 0.1)
    print(f"El total a pagar es: {monto}")
else:
    print("Metodo de pago invalido")
