#Elabore un programa para evaluar la nota de un estudiante,
#segun su ponderacion. Si el estudiante saco mas de 90 pero menor 
# a 100, Mostrar un mensaje que diga: Saliste muy bien
#Si saco exactamente 100 que imprima el mensaje: Perfecto
#Si saco entre 75 y 89: que muestre el mensaje B+
#Si saco entre 50 y 74 que diga: pasaste de vaina
#Si saca entre 0 y 49 que muestre el mensaje: Fuiste a calentar
#pupitre todo el semestre. Raspado
#Validar que solo acepte valores entre 0 y 100.

nota = int(input("Introduzca la nota: "))

""" if nota == 100: 
    print("Perfecto")
elif nota < 100 and nota >= 90:
    print("Saliste muy bien")
elif nota >= 75 and nota < 90:
    print("B+")
elif nota >= 50 and nota <= 74:
    print("Pasaste de vaina")
elif nota < 50 and nota >=0: print("Fuiste a calentar pupitre")
else: print("Valor invalido")

 """
if nota <= 0 or nota > 100:
    print("Valor invalido")
elif nota == 100:
    print("Perfecto")
elif 90 <= nota < 100:
    print("Saliste muy bien")
elif 75 <= nota < 90:
    print("B+")
elif 50 <= nota <= 74:
    print("Pasaste de vaina")
elif 0 <= nota <= 49:
    print("Fuiste a calentar pupitre")