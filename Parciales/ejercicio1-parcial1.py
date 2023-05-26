
import numpy as np
import random
##matrices

m1 = np.random.randint(0,11,size=(4,4))
m2 =np.random.randint(0,11, size=(4,4))
m3 =np.random.randint(0,11, size=(4,4))

print("Matriz A generada:")
print(m1)
print("Matriz B generada:")
print(m2)
print("Matriz C generada:")
print(m3)

##operacion
m1_3 = np.linalg.matrix_power(m1, 3)
m2_inversa =np.linalg.inv(m2)

resultado1 = np.dot(np.dot(m1_3,m2_inversa),m3)

m1_inversa3 = np.linalg.inv(m1_3)
resultado2 = resultado1 + m1_inversa3
##menos decimales
resultado2 =np.round(resultado2,2)


print("Resultado de la operacion  (A^3· B^(-1)· C) + (A^3)^(-1):")
print(resultado2)



