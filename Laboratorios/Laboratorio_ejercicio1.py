import numpy as np
import random

##primero pedimos la cantidad de filas y columnas
filas =int(input("Ingrese la cantidad de filas que tendrán las matrices:\n"))
columnas =int(input("Ingrese la cantidad de columnas que tendrán las matrices:\n"))

##procedemos a crear nuestras matrices
m1 = np.random.randint(0,5, size=(filas,columnas)) ##random.randint nos permite generar numeros ENTEROS aleatorios
m2 = np.random.randint(0,5, size=(filas, columnas))##en donde especificamos el rango, y el tamaño de las filas y columnas
print("Nuestra matriz 1 es:")
print(m1)
print("Nuestra matriz 2 es:")
print(m2)
##realizamos la funcion de suma
def suma_matriz():
    suma_matrices = np.add(m1,m2)
    return suma_matrices
suma_matrices =suma_matriz()
print("La suma entre matriz 1 y 2 es:")
print(suma_matrices)

##pedimos la matriz 3
filas3 =int(input("Ingrese la cantidad de filas que tendrá la tercera matriz:\n"))
columnas3 =int(input("Ingrese la cantidad de columnas que tendrá la tercera matriz:\n"))

m3 =np.random.randint(0,5, size=(filas3,columnas3))
print("Nuestra matriz 3 es:")
print(m3)
##hacemos la funcion resta
def resta_matriz():
    resta_matrices = np.subtract(suma_matrices,m3)
    return resta_matrices
resta_matrices =resta_matriz()
print("La resta entre el resultado de la suma",suma_matrices,"y la matriz 3 es:")
print(resta_matrices)
