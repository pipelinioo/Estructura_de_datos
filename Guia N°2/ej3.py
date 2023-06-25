import math
#se importa math y se define la clase Nodo
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
#cada nodo de la lista enlazada tiene un dato
#y una referencia al nodo siguiente
class lista_Enlazada:#se define la clase y tiene un atributo 'cabeza'
                    #que es la referencia al primer nodo
    def __init__(self):
        self.cabeza=None

    def agregarDato(self,dato):#este metodo recibe una cadena de datos separados por coma
                                #los datos se convierten en una lista de numeros
                                #se recorre la lista de datos y se crea un nuevo nodo para cada dato
                                #además, si la lista está vacía el nuevo nodo se convierte en la cabeza de la lista
        Datos=[float(d.strip())for d in datos.split(",")]
        for dato in Datos:
            nuevoNodo=Nodo(dato)
            if self.cabeza is None:
                self.cabeza=nuevoNodo
            else:
                actual=self.cabeza
                while actual.siguiente:
                    actual=actual.siguiente
                actual.siguiente=nuevoNodo
    
    def calcularMedia(self):#este calcula la media de los datos de la lista
                            #si está vacía la lista devuelve 0
                            #si no recorre la lista sumando los datos y el numero de elementos
                            #para finalmente dividirlos y obtener la media
        if self.cabeza is None:
            return 0
        suma=0
        contador=0
        actual=self.cabeza
        while actual:
            suma += actual.dato
            contador+=1
            actual=actual.siguiente
        return suma / contador

    def calcularDesvEstandar(self):#calcula la desviacion estandar de los datos de la lista
        if self.cabeza is None:
            return 0
        media =self.calcularMedia()
        suma_cuadrados=0
        contador=0
        actual=self.cabeza
        while actual:
            suma_cuadrados+=(actual.dato - media)**2
            contador+=1
            actual=actual.siguiente
        desvEstandar=math.sqrt(suma_cuadrados/contador)
        #se divide la suma de los cuadrados entre el contador
        #se calcula la raíz cuadrada utilizando 'math.sqrt'
        return desvEstandar
    
    def imprimirLista(self):#imprime los elementos de la lista enlazada
        if self.cabeza is None:
            print("La lista está vacia")
        else:
            actual=self.cabeza
            while actual is not None:
                print(actual.dato,end=" ")
                actual=actual.siguiente
            print()

    def estaVacia(self):
        return self.cabeza is None

lista= lista_Enlazada()

while True:
    print("____Menú____")
    print("1. Agregar dato\n")
    print("2. Calcular media\n")
    print("3. Calcular desviacion estandar\n")
    print("4. Imprimir Lista\n")
    print("5. Verificar si la lista se encuentra vacía\n")
    print("6. Salir\n")

    opcion=input("ingrese una opción:")

    if opcion == "1":
        datos=input("Ingrese datos separados por comas: ")
        lista.agregarDato(datos)
    elif opcion == "2":
        media =lista.calcularMedia()
        print("La media es:",media)
    elif opcion == "3":
        desviacion = lista.calcularDesvEstandar()
        print("La desviación estándar es:",desviacion)
    elif opcion == "4":
        lista.imprimirLista()
    elif opcion == "5":
        if lista.estaVacia():
            print("La lista está vacía")
        else:
            print("La lista no está vacía")
    elif opcion == "6":
        break
    else:
        print("Intente nuevamente")