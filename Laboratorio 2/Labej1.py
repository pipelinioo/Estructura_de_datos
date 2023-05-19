import random
import numpy as np

filasm1 = random.randint(2, 5)
columnasm1 = random.randint(2, 5)

m1 = []
m2 = []
## m1
for i in range(filasm1):
    fila = []
    for j in range(columnasm1):
        fila.append(int(input(f"Ingrese el elemento para matriz 1 ({i+1},{j+1}): ")))
    m1.append(fila)
### m2
for i in range(filasm1):
    fila = []
    for j in range(columnasm1):
        fila.append(int(input(f"Ingrese el elemento para matriz 2 ({i+1},{j+1}): ")))
    m2.append(fila)
##prints
print("Matriz 1:")
for fila in m1:
    print(fila)

print("Matriz 2:")
for fila in m2:
    print(fila)

#resta m1 y m2
resultado = []
for i in range(filasm1):
    fila = []
    for j in range(columnasm1):
        elemento = m1[i][j] - m2[i][j]
        fila.append(elemento)
    resultado.append(fila)

print("El resultado entre la resta de Matriz 1 y Matriz 2 es:")
for fila in resultado:
    print(fila)

# m3
filas1 = int(input("Ingrese la misma cantidad de filas que la matriz resultado:\n "))
columnas1 = int(input("Ingrese la misma cantidad de columnas que la matriz resultado:\n "))
m3 = []
for i in range(filas1):
    fila = []
    for j in range(columnas1):
        fila.append(int(input(f"Ingrese el elemento para matriz 3 ({i+1},{j+1}): ")))
    m3.append(fila)

# multi*
resulmultiplicacion = np.multiply(resultado, m3)

print("La multiplicación entre la matriz resultado y la matriz 3 es:")
for fila in resulmultiplicacion:
    print(fila)
