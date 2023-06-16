
colaproductos =[]
#a
def agregar(producto):
    colaproductos.append(producto)
    print("Producto agregado:",producto)

#b
def eliminar1erproducto():
    if len(colaproductos)>0:
        primerproducto= colaproductos.pop(0)
        print("Primer producto eliminado:",primerproducto)
    else:
        print("La cola de productos esta vacia")
#c
def mostrarproductos():
    if len(colaproductos)>0:
        print("Productos en la cola son;")
        for producto in colaproductos:
            print(producto)
    else:
        print("La cola de productos esta vacia")
#d
def invertirproductos():
    colaproductos.reverse()
    print("Orden de los productos ha sido invertido")
#e
def eliminarproductos():
    colaproductos.clear()
    print("Se han eliminado todos los productos de la cola")
#agregar productos a la cola
agregar("Manzanas")
agregar("Leche")
agregar("Pan")
agregar("Cereales")
agregar("Yogurth")
agregar("Pasta")
#funciones##
mostrarproductos()
eliminar1erproducto()
invertirproductos()
mostrarproductos()
eliminarproductos()
mostrarproductos()