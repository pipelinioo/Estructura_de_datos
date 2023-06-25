# Se define la clase que representa a cada cliente
class Cliente:
    #se inicializan los atributos del objeto cliente
    def __init__(self, ticket, caja): 
        self.ticket = ticket
        self.caja = caja

#Se crea una clase que se encargara de administrar la cola de atención al cliente
class ColaAtencion: 
    # se crean listas vacias que representan las colas de atención
    # se crea una variable que representa la caja que está atendiendo actualmente
    def __init__(self):
        self.cola1 = []
        self.cola2 = []
        self.cola3 = []
        self.cola_actual = 1

    # este metodo recibe un objeto Cliente y lo agrega a la cola correspondiente según 
    # el parametro cola_actual
    def agregar_cliente(self, nuevo_cliente):
        if self.cola_actual == 1:
            nuevo_cliente.caja = 1
            self.cola1.append(nuevo_cliente)
        elif self.cola_actual == 2:
            nuevo_cliente.caja = 2
            self.cola2.append(nuevo_cliente) 
        elif self.cola_actual == 3:
            nuevo_cliente.caja = 3
            self.cola3.append(nuevo_cliente) 

        self.cola_actual = (self.cola_actual % 3) + 1


    # este metodo se encarga de atender el cliente en la cola actual 
    def atender_cliente(self):
        cliente = None

        if self.cola_actual == 1 and self.cola1:
            cliente = self.cola1.pop(0)
        elif self.cola_actual == 2 and self.cola2:
            cliente = self.cola2.pop(0)
        elif self.cola_actual == 3 and self.cola3:
            cliente = self.cola3.pop(0)

        if cliente:
            self.cola_actual = (self.cola_actual % 3) + 1

        return cliente

# Crear una instancia de la cola de atención
cola_atencion = ColaAtencion()

# Menú principal
while True:
    print("\n\nBienvenido a la sistema de atención de clientes :)")
    print("Ingrese una de los siguientes opciones:")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    # dependiendo de la opcion seleccionada en el menú, se utilizan las diferentes
    # funciones de la clase ColaAtencion
    if opcion == "1":
        ticket = input("\nIngrese el número de ticket del cliente: ")
        #caja = input("Ingrese el número de caja para atender al cliente: ")
        cliente = Cliente(ticket, None)
        cola_atencion.agregar_cliente(cliente)
        print("Cliente agregado correctamente")

    elif opcion == "2":
        cliente_atendido = cola_atencion.atender_cliente()
        if cliente_atendido:
            print("\nCliente atendido: Ticket", cliente_atendido.ticket, "- Caja", cliente_atendido.caja)
        else:
            if not cola_atencion.cola1 and not cola_atencion.cola2 and not cola_atencion.cola3:
                print("\nNo hay clientes en ninguna cola.")
            else:
                print("\nNo hay clientes en la cola", cola_atencion.cola_actual)

    elif opcion == "3":
        print("\nHasta luego")
        break

    else:
        print("\nOpción inválida. Por favor, seleccione una opción válida.")