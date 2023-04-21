import numpy as np

filas = int(input("Ingrese la cantidad de filas de las matrices: "))
columnas = int(input("Ingrese la cantidad de columnas de las matrices: "))

# Crear la primera matriz y llenarla
matriz1 = np.zeros((filas, columnas))
print("Ingrese los elementos de la primera matriz:")
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = int(input(f"Elemento [{i}][{j}]: "))

# Crear la segunda matriz y llenarla
matriz2 = np.zeros((filas, columnas))
print("Ingrese los elementos de la segunda matriz:")
for i in range(filas):
    for j in range(columnas):
        matriz2[i][j] = int(input(f"Elemento [{i}][{j}]: "))

def sumar_matrices():
    matriz_suma = np.add(matriz1, matriz2)
    return matriz_suma

def restar_matrices():
    matriz_resta = np.subtract(matriz1, matriz2)
    return matriz_resta

matriz_suma = sumar_matrices()
matriz_resta = restar_matrices()

print("Matriz suma:")
print(matriz_suma)

print("Matriz resta:")
print(matriz_resta)
