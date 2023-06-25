class Almacen:#se define la clase Almacen que inicializa dos listas vacias
                #'productosRecibidos' y 'productosParaDespachar'
    def __init__(self):
        self.productosRecibidos= []
        self.productosParaDespachar= []
    
    def agregarProducto(self,producto):#este metodo recibe un producto como argumento
                                        #y lo agrega a la lista 'productosRecibidos'
        self.productosRecibidos.append(producto)
        print("Producto agregado con éxito")

    def DespacharProducto(self):#este verifica si hay productos para despacho
        if len(self.productosParaDespachar)>0:
            producto=self.productosParaDespachar.pop(0)#si hay un producto, extrae el primero de la lista utilizando pop
            print("Producto despachado:",producto)
        else:
            print("No hay productos disponibles para despacho")
        
    def pilaVacia(self):#este verifica si la lista 'productosRecibidos' está vacía
        if len(self.productosRecibidos)==0:
            print("La pila de productos para despacho está vacía")
        else:
            print("La pila tiene productos para despacho")
        
    def colaVacia(self):#este verifica si la lista 'productosParaDespachar' está vacía
        if len(self.productosParaDespachar)==0:
            print("La cola  de productos para despachar está vacia")
        else:
            print("La cola tiene productos para despacho")

    def imprimirProductosRecibidos(self):#este imprime la lista de productos recibidos
        print("Lista de productos recibidos:")
        for producto in self.productosRecibidos:
            print(producto)

    def imprimirProductosDespacho(self):#imprime la lista de productos para despacho
        print("Lista de productos para despachar:")
        for producto in self.productosParaDespachar:
            print(producto)

    def MostrarTotalProductos(self):#calcula la cantidad total de productos en el almacen
                                    #sumando el tamaño de las listas
        total_productos=len(self.productosRecibidos)+len(self.productosParaDespachar)
        print("Cantidad de productos en Almacen:",total_productos)

almacen=Almacen()

while True:
    print("----Menú----")
    print("1. Agregar producto\n")
    print("2. Despachar producto\n")
    print("3. Verificar si la pila de productos está vacía \n")
    print("4. Verificar si la cola de productos está vacía\n")
    print("5. Imprimir lista de productos recibidos\n")
    print("6. Imprimir lista de productos para despachar\n")
    print("7. Mostrar cantidad de productos en el almacén\n")
    print("8. Salir\n")

    opcion=input("ingrese una opción:\n")

    if opcion =="1":
        numeroProductos=int(input("Ingrese la cantidad de productos:"))
        for _ in range(numeroProductos):
            producto=input("Ingrese el nombre del producto:")
            almacen.agregarProducto(producto)
    elif opcion =="2":
        almacen.DespacharProducto()
    elif opcion =="3":
        almacen.pilaVacia()
    elif opcion=="4":
        almacen.colaVacia()
    elif opcion=="5":
        almacen.imprimirProductosRecibidos()
    elif opcion=="6":
        almacen.imprimirProductosDespacho()
    elif opcion=="7":
        almacen.MostrarTotalProductos()
    elif opcion=="8":
        break
    else:
        print("Intente nuevamente")