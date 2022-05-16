"""Nombre:Jesús Bracamonte. C.i:29795537"""

"""Defina una función en python que acepte la radio y devuelva el valor del área de un círculo de esas dimensiones. (4 puntos)"""

def calcular(r,pi):
    area = pi * r**2
    return(area)

from math import pi
r = float(input("Digite el valor de radio: "))

area = pi * r ** 2
print("el valor del área de un círculo de esas dimensiones es:{}".format(area))

"""Defina una función en python que acepte 3 valores y devuelva solo el máximo de los tres"""
def valores(num1, num2, num3):
    
    if num1>=num2 and num1>=num3:
        print("Maximo valor es:{}".format(num1))
    elif num2>=num1 and num2>=num3:
        print("Maximo valor es:{}".format(num2))
    elif num3>=num1 and num3>=num2:
        print("Maximo valor es:{}".format(num3))
    return num1, num2, num3

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el terce numero: "))

if num1>=num2 and num1>=num3:
    print("Maximo valor es:{}".format(num1))
elif num2>=num1 and num2>=num3:
    print("Maximo valor es:{}".format(num2))
elif num3>=num1 and num3>=num2:
    print("Maximo valor es:{}".format(num3))

"""Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista"""

lista= [1,2,3,4,5,6,7,8,9]
def impares(lista):
    if len (lista) ==0:
        return 0
    elif lista[0] % 2 !=0:
        return lista[0] + impares(lista[1:])
    else:
        return impares(lista[1:])

print("suma de los impares es:",impares(lista))

"""
Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad
de caracteres de como segundo parámetro. La función debe devolver un nuevo string que consista en 
el string original y el número correcto de caracteres necesarios para que el string se salga centrado.
No se agregan caracteres al final del string."""





