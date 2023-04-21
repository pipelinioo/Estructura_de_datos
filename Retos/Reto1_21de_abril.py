
#Se debe de pedir la palabra al usuario
palabra = input("Ingrese palabra a evaluar:\n")
vocales=["a","e","i","o","u"]

cto_vocales = {}
for vocal in vocales:
    cto_vocales[vocal] = palabra.count(vocal)
#
print("La cantidad de cada vocal en la palabra",palabra,"es:")
print(cto_vocales)
