
pacientes =[]

for i in range(1):
    paciente ={}
    print("Ingrese la información del paciente:",i+1)
    paciente["Nombre"]=input("Nombre:")
    paciente["Edad"]=int(input("Edad:"))
    paciente["Peso"]=float(input("Peso:"))
    sintomas =input("Sintomas(separado por comas):")
    paciente["Sintomas"]=sintomas.split(",")
    pacientes.append(paciente)

seguirbusq = True
while seguirbusq:
    nombrebuscado = input("Ingrese el nombre del paciente a buscar(o 'salir' para terminar):")

    if nombrebuscado.lower()=="salir":
        break
    encontrado=False
    for paciente in pacientes:
        if paciente["Nombre"] == nombrebuscado:
            print("Ficha personal del paciente:")
            print("Nombre:", paciente["Nombre"])
            print("Edad:", paciente["Edad"])
            print("Peso:", paciente["Peso"])
            print("Sintomas:", paciente["Sintomas"])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un paciente con el nombre indicado.")
    
    otrabusqueda = input("Desea realizar otra busqueda? (s/n):")
    if otrabusqueda.lower()!="s":
        seguirbusq=False