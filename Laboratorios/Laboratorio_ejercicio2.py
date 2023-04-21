import numpy as np
import random

##Pedimos la cantidad de filas y columnas para la matriz
filas = int(input("Ingrese la cantidad de filas para la matriz:\n"))
columnas = int(input("Ingrese la cantidad de columnas para la matriz:\n"))
#matriz
m1 = np.random.randint(0,10, size=(filas,columnas))
print("Nuestra matriz es:")
print(m1)
#Pedimos el escalar
escalar = int(input("Ingrese el escalar por el cual se multiplicará la matriz:\n"))
#diseñamos la funcion para multiplicar
def multiplicar():
    escalarmulti =np.multiply(m1,escalar)
    return escalarmulti
escalarmulti = multiplicar()
print("El resultado de la multiplicacion del escalar y la matriz es:")
print(escalarmulti)