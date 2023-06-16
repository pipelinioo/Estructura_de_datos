
class Pila:
    def __init__(self):
        self.items=[]
    def vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.vacia():
            return self.items.pop()

    def tope(self):
        if not self.vacia():
            return self.items[-1]

    def imprimirpila(self):
        print("Pila de documentos:")
        for documento in reversed(self.items):
            print(documento)
#a 
def listado_doc(pila):
    pila.imprimirpila()
#b
def agregardocs(pila):
    pila.apilar("Avance Tesis")
    pila.apilar("Proyecto Integrador")
#c
def ultimoelemento(pila):
    if not pila.vacia():
        ultimoelemento = pila.tope()
        print("Ultimo elemento superior de la pila:", ultimoelemento)
#d
def eliminar_docsuperior(pila):
    if not pila.vacia():
        documentoeliminado = pila.desapilar()
        print("Documento eliminado:", documentoeliminado)
#e
def pilaactualizada(pila):
    pila.imprimirpila()

# f
def verificarpilavacia(pila):
    if pila.vacia():
        print("La pila de documentos está vacía")
    else:
        print("La pila de documentos no está vacía")

pila_documentos = Pila()
documentos = ["Informe Final", "Guia de Estudio", "Tesis 4", "Seminario Osorno"]
for documento in documentos:
    pila_documentos.apilar(documento)

# funciones
listado_doc(pila_documentos)
agregardocs(pila_documentos)
listado_doc(pila_documentos)
ultimoelemento(pila_documentos)
eliminar_docsuperior(pila_documentos)
listado_doc(pila_documentos)
verificarpilavacia(pila_documentos)