import random

##funciones##

##crea una matriz con elementos aleatorios del 1 al 10 con dimensiones dimxdim
def crearmatriz(dim):
    matriz= []
    for _ in range(dim):
        fila = [random.randint(1, 10) for _ in range(dim)]
        matriz.append(fila)
    return matriz

##funcion para imprimir matrices
def printmatriz(matriz):
    for fila in matriz:
        print(fila)
    print()

# funcion para inversa usando metodo de gauss
def inversa(matriz):
    dim=len(matriz)
    identidad = [] ###creamos la matriz identidad
    for i in range(dim):
        filaidentidad = [1 if j == i else 0 for j in range(dim)]
        identidad.append(filaidentidad)
    
    # #se mueve la matriz identidad a la derecha de la original
    for i in range(dim):
        matriz[i] += identidad[i]
    
    ##eliminación Gaussiana
    for i in range(dim):
        pivot = matriz[i][i]
        for j in range(i+1, dim):
            factor = matriz[j][i] / pivot
            for k in range(i, 2*dim):
                matriz[j][k] -= matriz[i][k] * factor
    
    # eliminación hacia atrás
    for i in range(dim-1, -1, -1):
        pivot = matriz[i][i]
        for j in range(i-1, -1, -1):
            factor = matriz[j][i] / pivot
            for k in range(i, 2*dim):
                matriz[j][k] -= matriz[i][k] * factor
    
    # se normalizanlas filas de la matriz invertida
    for i in range(dim):
        divisor = matriz[i][i]
        for j in range(dim, 2*dim):
            matriz[i][j] /= divisor
    
    #  matriz invertida
    inversa = [fila[dim:] for fila in matriz]
    
    return inversa

##ejecucion del programita##
# se crea la matriz con dimensiones 3 ,5
dimension= random.randint(3, 5)
m1 = crearmatriz(dimension)

#print
print("Matriz original:")
printmatriz(m1)

#  la matriz invertida
matriz_inversa = inversa(m1)
print("Matriz inversa:")
printmatriz(matriz_inversa)
