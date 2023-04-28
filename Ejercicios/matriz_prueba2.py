import random

filas =int(input("Ingrese la cantidad de filas que tendrá su matriz:\n"))
columnas =int(input("Ingrese la cantidad de columnas que tendrá su matriz:\n"))

m1 =[[0]*columnas for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        m1[i][j] = random.randint(1,5)

for i in range(filas):
    for j in range(columnas): 
        print(m1[i][j])
    print()    

m2 =[[0]*columnas for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        m2[i][j] = random.randint(filas)

for i in range(filas):
    for j in range(columnas):
        print(m2[i][j])
    print()     
