
class Videos :
    def __init__(self, titulo, autor, duracion):
        self.titulo=titulo
        self.autor=autor
        self.duracion=duracion

class Nodo:
    def __init__(self, video):
        self.video=video
        self.siguiente=None

class ListaReproduccion:
    def __init__(self):
        self.cabeza=None

    def estaVacia(self):
        return self.cabeza is None

    def agregarVideo(self, video):
        nuevoNodo=Nodo(video)
        if self.estaVacia():
            self.cabeza=nuevoNodo
            nuevoNodo.siguiente=self.cabeza
        else:
            nodoActual=self.cabeza
            while nodoActual.siguiente!=self.cabeza:
                nodoActual=nodoActual.siguiente
            nodoActual.siguiente=nuevoNodo
            nuevoNodo.siguiente=self.cabeza

    def printListaVideos(self):
        if self.estaVacia():
            print("La lista de videos esta vacia")
        else:
            nodoActual = self.cabeza
            while True:
                print("Titulo:", nodoActual.video.titulo)
                print("Autor:", nodoActual.video.autor)
                print("Duracion:", nodoActual.video.duracion)
                print("--------------------")
                nodoActual=nodoActual.siguiente
                if nodoActual==self.cabeza:
                    break

    def buscarVideo(self, titulo):
        if self.estaVacia():
            print("La lista de videos está vacía")
            return None
        nodoActual=self.cabeza
        videoEncontrado=None  # Variable para almacenar el video encontrado
        while True:
            if nodoActual.video.titulo==titulo:
                videoEncontrado=nodoActual.video
                break
            nodoActual=nodoActual.siguiente
            if nodoActual==self.cabeza:
                break
            if videoEncontrado is not None:
                print("Video encontrado:")
                print("Titulo del video:", videoEncontrado.titulo)
                print("Autor:", videoEncontrado.autor)
                print("Duracion:", videoEncontrado.duracion)
                print("--------------------")
            else:
                print("El video no se encontró en la lista")
            return videoEncontrado


    def eliminarVideo(self, titulo):
        if self.estaVacia():
            print("La lista de videos está vacía")
            return
        if self.cabeza.video.titulo==titulo:
            if self.cabeza.siguiente==self.cabeza:
                self.cabeza=None
            else:
                nodoActual=self.cabeza
                while nodoActual.siguiente!=self.cabeza:
                    nodoActual = nodoActual.siguiente
                nodoActual.siguiente=self.cabeza.siguiente
                self.cabeza=self.cabeza.siguiente
            print("El video se eliminó de la lista")
            return
        nodoActual=self.cabeza
        while nodoActual.siguiente!=self.cabeza:
            if nodoActual.siguiente.video.titulo==titulo:
                nodoActual.siguiente=nodoActual.siguiente.siguiente
                print("El video se elimino de la lista")
                return
            nodoActual=nodoActual.siguiente
        print("El video no se encontró en la lista")


lista = ListaReproduccion()

#crear videos y agregarlos a la lista
video1 = Videos("hola", "Autor1", "5:30")
video2 = Videos("hola2", "Autor2", "5:45")
video3 = Videos("hola3", "Autor3", "8:15")
lista.agregarVideo(video1)
lista.agregarVideo(video2)
lista.agregarVideo(video3)
#mostrar la lista con los videos agregados
lista.printListaVideos()
#buscar un video
lista.buscarVideo(video1.titulo)
#eliminar un video
lista.eliminarVideo(video2.titulo)
#mostrar lista nuevamente actualizada
lista.printListaVideos()

