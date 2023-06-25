
class Nodo():                     #En esta clase se crean los nodos para el arbol jerarquico      
    def __init__(self,datos,cargo):#cada nodo almacenara datos, y cargo del empleado, cada empleado seria un nodo
        self.datos=datos
        self.cargo=cargo
        self.subordinados=[]
    def agregarSubordinado(self,subordinado):#funcion para agregar subordinado al nodo con append
        self.subordinados.append(subordinado)
    def eliminarSubordinado(self,subordinado):#eliminar subordinado con remove
        self.subordinados.remove(subordinado)


class ArbolJerarquia:#representa el arbol jerarquico
    def __init__(self,datos,cargo):
        self.raiz=Nodo(datos,cargo)#nodo raiz del arbol (CEO)

    def agregarEmpleado(self,datos,cargo,jefeDirecto):#agregar empleado
        empleado=Nodo(datos,cargo)#Nuevo nodo con datos del empleado
        jefe=self.buscarEmpleado(jefeDirecto)#se asigna su jefe directo
        if jefe is None:    #sino existe un jefe directo da msj de error
            print("El Jefe directo no existe, No se pudo agregar el empleado")
        else:
            jefe.agregarSubordinado(empleado)# si existe un jefe directo para el empleado se agrega exitosamente
            print(f"El empleado {datos} ha sido ingresado exitosamente")# y se asigna como su subordinado
    
    def eliminarEmpleado(self,datos):#eliminar empleados
        if datos==self.raiz.datos:#si el dato ingresado coincide con el CEO da msj de error
            print("No se puede eliminar al CEO")
            return
        
        empleado=self.buscarEmpleado(datos)#se busca el empleado segun el nombre ingresado
        if empleado is None:#sino no existe da msj de error
            print("El empleado no existe.")
        else:
            jefe=self.buscarJefeDirecto(datos)#si existe se busca su jefe directo
            jefe.eliminarSubordinado(empleado)#y se elimina como su subordinado
            for subordinado in empleado.subordinados:#ciclo for por si se elimina un empleado con subordinados
                jefe.agregarSubordinado(subordinado)#se agregan dichos subordinados al jefe directo del empleado eliminado
            print(f"El empleado {datos} ha sido eliminado exitosamente")

    def buscarRecursivo(self,nodo,datos):#busqueda recursiva desde los nodos
        if nodo is None:#sino existe nodo return
            return None
        if nodo.datos==datos:#si el nodo coincide con los datos retorna
            return nodo
        for subordinado in nodo.subordinados:#se busca en for por los nodos de subordinados(o sea todos los empleados debajo del CEO)
            resultado=self.buscarRecursivo(subordinado,datos)#se almacena el resultado encontrado en variable resultado
            if resultado is not None:
                return resultado#sino encuentra devuelve None
        return None
    def buscarEmpleado(self,datos):#se utiliza esta funcion para realizar la busqueda recursiva
        return self.buscarRecursivo(self.raiz,datos)#comienza desde la raiz

    def buscarJefeRecursivo(self,nodo,datos):#misma funcion que busqueda recursiva, pero para buscar el jefe directo del empleado
        if nodo is None:#sino existe return
            return None
        for subordinado in nodo.subordinados:#busqueda recursiva desde un nodo dado
            if subordinado.datos==datos:#verifica si los subordinados de ese nodo buscado coinciden
                return nodo#retorna el nodo
            resultado=self.buscarJefeRecursivo(subordinado,datos)#da el resultado correspondiente del jefe del subordinado
            if resultado is not None:
                return resultado
        return None#sino no lo encuentra retorna None
    
    def buscarJefeDirecto(self,datos):#se usa la busqueda del jefe directo
        return self.buscarJefeRecursivo(self.raiz,datos)#inicia desde el nodo raiz
    def mostrarRecursivo(self,nodo,nivel):#muestra la jerarquia de empleados
        if nodo is None:#sino exiuste nodo devuelve none
            return
        sangria=" "*nivel#sangria segun el nivel de jerarquia del empleado
        print(f"{sangria}-{nodo.datos}-({nodo.cargo})")#imprime los datos con la sangria, su nombre, y cargo
        for subordinado in nodo.subordinados:#llamada a cada subordinado(empleados)
            self.mostrarRecursivo(subordinado,nivel+1)#para emplear la funcion e imprimir por cada uno
    def mostrarJerarquia(self):#se usa para llamar la funcion mostrar recursiva
        self.mostrarRecursivo(self.raiz,0)#comienza desde la raiz

def mostrar_menu():#funcion para imprimir el menu
    print("----- MENÚ -----")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Mostrar jerarquia")
    print("4. Buscar empleado")
    print("5. Buscar jefe directo")
    print("0. Salir")

            #empleados iniciales
arbol = ArbolJerarquia("Luis", "CEO")#nodo raiz, o sea el CEO
arbol.agregarEmpleado("Jorge", "Gerente", "Luis")#jefes
arbol.agregarEmpleado("Annais", "Supervisor", "Jorge")
arbol.agregarEmpleado("Natalia", "Supervisor", "Jorge")
arbol.agregarEmpleado("Franco", "Empleado", "Annais")#empleados, y sus jefes a cargo
arbol.agregarEmpleado("Felipe", "Empleado", "Annais")
arbol.agregarEmpleado("Niska", "Empleado", "Natalia")
arbol.agregarEmpleado("Vicho", "Empleado", "Natalia")


while True:#ciclo para el menu
    mostrar_menu()#se imprime el menu
    opcion = input("Ingrese la opcion deseada: ")# recibe la opcion seleccionada para el menu
    if opcion=="1":#si coincide con 1
        nombre=input("Ingrese el nombre del empleado: ")#nombre del empleado a agregar
        cargo=input("Ingrese el cargo del empleado: ")#cargp
        jefe=input("Ingrese el nombre del jefe directo: ")#cual sera su jefe directo
        arbol.agregarEmpleado(nombre, cargo, jefe)#se agrega el empleado al arbol

    elif opcion=="2":#si coincide con 2
        nombre=input("Ingrese el nombre del empleado a eliminar:\n ")#ingresar empleado a eliminar
        arbol.eliminarEmpleado(nombre)#se llama la funcion y se elimina si coincide el nombre

    elif opcion=="3":#si coincide con 3
        arbol.mostrarJerarquia()#imprime la jerarquia del arbol

    elif opcion=="4":#si coincide con 4
        nombre = input("Ingrese el nombre del empleado a buscar:\n ")#empleado a buscar
        empleado = arbol.buscarEmpleado(nombre)#se ingresa el nombre buscado a la funcion buscar empleado
        if empleado is None:#sino coincide da mensaje de no existe
            print("El empleado no existe")
        else:
            print(f"Nombre: {empleado.datos}")#si coincide imprime su nombre y cargo
            print(f"Cargo: {empleado.cargo}")

    elif opcion=="5":#si concide con 5
        nombre=input("Ingrese el nombre del empleado para obtener su jefe directo:\n ")#nombre del empleado para recibir su jefe directo
        jefeDirecto = arbol.buscarJefeDirecto(nombre)#se ingresa el nombre dado a la funcion buscarJefeDirecto
        if jefeDirecto is None:#sino lo encuentra da msj de error
            print("El empleado no existe o no tiene un jefe directo.")
        else:                   #si lo encuntra imprime los datos  imprime el nombre y cargo del jefe directo encontrado
            print(f"Nombre del jefe directo: {jefeDirecto.datos}")
            print(f"Cargo del jefe directo: {jefeDirecto.cargo}")

    elif opcion=="0":#si coincide con 0 se sale del programa
        print("Saliendo del programa...")
        break
    else:          #sino concinde con las opciones da error y deja seleccionar nuevamente
        print("Opción inválida. Intente nuevamente.")

  

