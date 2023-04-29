import numpy as np

##debo pedir la cantidad de filas y columnas
filas = int(input("Ingrese la cantidad de filas que tendra su Matriz:\n"))
columnas = int(input("Ingrese la cantidad de columnas que tendra su matriz\n"))

##creamos la primera matriz con zero
matriz1 = np.zeros((filas,columnas))
print("Ingrese los elementos de la primera matriz, 1 por 1:\n")
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = int(input(f"Elemento [{i}][{j}]")) ## i y j demuestran la ubicacion del numero que le proporcionamos
#matriz 2 es lo mismo
matriz2 = np.zeros((filas,columnas))
print("Ingrese los elementos de la segunda matriz, 1 por 1:\n")
for i in range(filas):
    for j in range(columnas):
        matriz2[i][j] = int(input(f"Elemento [{i}][{j}]"))

##las funcioness
def suma_matrices():
    matriz_suma =np.add(matriz1,matriz2)
    return matriz_suma
def resta_matrices():
    matriz_resta =np.subtract(matriz1,matriz2)
    return matriz_resta

matriz_suma =suma_matrices()
matriz_resta =resta_matrices()

print("Matriz suma de matriz 1 y matriz 2:")
print(matriz_suma)

print("Matriz resta entre matriz 1 matriz 2:")
print(matriz_resta)

##Felipe Asenjo, Felipe Delgado