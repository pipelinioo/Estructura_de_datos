
class CancionNodo:#se define el nodo que representará la cancion
    def __init__(self,titulo,artista):#contiene dos atributos que guardaran el nombre
        self.titulo= titulo         #y artista de la cancion
        self.artista= artista
        self.siguiente= None#dos punteros que apuntan al siguiente y anterior nodo
        self.anterior= None

class ListaReproduccion: #se define la lista enlazada doble
    def __init__(self):
        self.primero=None#se refiere al primer nodo de la lista
        self.ultimo= None#al ultimo nodo

    def estavacia(self):#si el primer nodo no existe la lista esta vacia
        return self.primero is None

    def agregarCancion(self):
        titulo=input("Ingrese el titulo de la canción:\n")#se pide el nombre y artista de la cancion
        artista=input("Ingrese el nombre del artista de la canción:\n")
        nuevaCancion=CancionNodo(titulo,artista)#se agrega como nueva cancion que es un objeto de CancionNodo
        if self.estavacia():#si la lista esta vacia se agrega la nueva cancion como el primer elemento
            self.primero=nuevaCancion
            self.ultimo=nuevaCancion
        else:           #sino se establecen los punteros correspondientes a la nueva cancion agregada
            nuevaCancion.anterior =self.ultimo
            self.ultimo.siguiente= nuevaCancion
            self.ultimo= nuevaCancion

    def eliminarCancion(self):
        titulo=input("Ingrese el titulo de la canción a eliminar:\n")#cancion a eliminar
        actual=self.primero
        while actual is not None:#recorre el nodo con la cancion ingresada
            if actual.titulo == titulo:
                if actual.anterior is not None:#ajusta los punteros para redifinir los nodos anteriores
                    actual.anterior.siguiente = actual.siguiente#y siguientes en funciuon del nodo a eliminar
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.primero:
                    self.primero = actual.siguiente
                if actual == self.ultimo:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente

    def printCanciones(self):#recorre la lista desde el primer nodo hasta el ultimo y los imprime
        actual = self.primero
        while actual is not None:
            print(f"Título: {actual.titulo}, Artista: {actual.artista}")
            actual = actual.siguiente
    def printCancionVecina(self,titulo):
        actual = self.primero
        while actual is not None:#recorre la lista encontrando el nombre del titulo seleccionado
            if actual.titulo==titulo:
                cancionActual=actual#si se encuntra se imprime la cancion con su nombre y artista, junto con los nodos anterio y siguiente
                cancionAnterior=actual.anterior.titulo if actual.anterior else "No hay canción anterior"#sino existe nodo anterior o siguiente se especifica
                cancionSiguiente= actual.siguiente.titulo if actual.siguiente else "No hay canción siguiente"
                print(f"Canción seleccionada: {cancionActual.titulo} - {cancionActual.artista}")
                print(f"Canción anterior: {cancionAnterior}")
                print(f"Canción siguiente: {cancionSiguiente}")
                break
            actual=actual.siguiente        

lista=ListaReproduccion()
#agregar cancion a lista vacia
print("--Ingrese las datos para su lista de reproducción--")
lista.agregarCancion()
lista.agregarCancion()
lista.agregarCancion()
lista.agregarCancion()
#print lista
print("--Lista 'Best Canciones'--")
lista.printCanciones()
#eliminar canciond e la lista
print("--Eliminar canción--")
lista.eliminarCancion()
print("--Lista 'Best Canciones' actualizada")
lista.printCanciones()
#ver posicion anterior y siguiente de una cancion
tituloSeleccionado = input("Ingrese el titulo de la canción que desea seleccionar de la lista: ")
lista.printCancionVecina(tituloSeleccionado)

