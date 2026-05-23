#Condicionales

#Elabore una solucion donde se le solicite al usuario la nota y
#se determine si esta aprobado o no, si tiene mayor o igual a 5 
#puntos esta aprobado, de lo contrario si tiene menos de 5 esta
# reprobado. Se debe de validar que la nota no exceda el valor de 10
#ni sea inferior a 0.

nota = float(input("Ingrese la nota del estudiante: "))

if nota > 10 or nota < 0:
    print("Valores fuera del rango permitido")
else:
    if nota >= 5: 
        print("Estas aprobado")
    else:
        print("Estas raspado")

#Metodo 2
if nota > 10 or nota < 0:
    print("Valores fuera del rango permitido")
elif nota >= 5:
    print("Estas aprobado")
elif nota <5:
        print("Estas raspado")

#Metodo 3: 
if nota > 10 or nota < 0:
    print("Valores fuera del rango permitido")
if nota >= 5:
    print("Estas aprobado")
if nota <5:
        print("Estas raspado")