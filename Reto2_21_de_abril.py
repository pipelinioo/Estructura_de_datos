import array
import random
numero =random.randint(10,30)
arreglo = array.array('i', [random.randint(0, 100) for _ in range(numero)])
print(arreglo)

busqueda = int(input("Ingrese el elemento a buscar dentro del arreglo:\n"))
verificar = False
for elemento in arreglo:
    if elemento == busqueda:
        verificar = True
        break
if verificar:
    print("El elemento",busqueda,"ha sido encontrado en el arreglo")
else:
    print("El elemento",busqueda,"no ha sido encontrado en el arreglo")


##Integrantes:Natalia Carrillanca
        ##### Felipe Delgado