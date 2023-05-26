import numpy as np
import random

##matrices

m1 = np.random.randint(0,11,size=(3,3))
m2 = np.random.randint(10,31,size=(3,3))
m3 = np.random.randint(-11,0,size=(3,3))

print("Matriz aleatoria A:")
print(m1)
print("Matriz aleatoria B:")
print(m2)
print("Matriz aleatoria C:")
print(m3)

##demostracion propiedad
## (A+B)*C
suma1 = m1+m2
mult1 =np.dot(suma1,m3)
##A*C+B*C
mult2 =np.dot(m1,m3)
mult3= np.dot(m2,m3)
suma2 = mult2+mult3

print("La propiedad  (A+B)·C = A·C + B·C:")
print("(A+B)·C")
print(mult1)
print("A·C + B·C")
print(suma2)
print("Se comprueba que la propiedad se cumple")