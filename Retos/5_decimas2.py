import random
##funciones
def cmatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz

def sumar_matrices(m1,m2):
    filas =len(m1)
    columnas = len(m1[0])
    result =[]
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = m1[i][j] + m2 [i][j]
            fila.append(suma)
        result.append(fila)
    return result

def resta_matrices(m1,m2):
    filas =len(m1)
    columnas = len(m1[0])
    result =[]
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = m1[i][j] - m2 [i][j]
            fila.append(suma)
        result.append(fila)
    return result

##creadas las funciones, solicitamos por consola las filas y columnas de las matrices
filas = int(input('Ingrese la cantidad de filas que tendrá su matriz:\n'))
columnas = int(input('Ingrese la cantidad de columnas que tendrán sus matrices'))
#matrices
m1=cmatriz(filas,columnas)
m2 =cmatriz(filas,columnas)
##se llama a las funciones
sumar_matrices = sumar_matrices(m1,m2)
resta_matrices = resta_matrices(m1,m2)

#print
print('Nuestra matriz 1:')
for fila in m1:
    print(fila)

print('Nuestra matriz 2:')
for fila in m2:
    print(fila)

print('La suma de matriz 1 y matriz 2 es:')
for fila in sumar_matrices:
    print(fila)

print('La resta para matrices 1 y 2 es:')
for fila in resta_matrices:
    print(fila)

## Felipe Delgado, Felipe Asenjo
