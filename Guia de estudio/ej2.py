

tuplafrutas =("manzana","platano","pera","naranja","frutilla","manzana")
print("La tupla de frutas original es:",tuplafrutas)
#a
frutassinrepetir=tuple(set(tuplafrutas))
#b
nuevafruta= input("Ingrese una nueva fruta para agregar:")
frutas_actualizadas =frutassinrepetir +(nuevafruta,)
#C
frutas_actualizadas =tuple(f for f in frutas_actualizadas if f !="platano")
#d
cantidaddefrutas =len(frutas_actualizadas)

print("Frutas sin repetir:",frutassinrepetir)
print("Frutas actualizadas:",frutas_actualizadas)
print("Cantidad de frutas:",cantidaddefrutas)
